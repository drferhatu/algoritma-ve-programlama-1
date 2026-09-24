#!/usr/bin/env python
"""İçerik ve derleme doğrulaması (Algoritma ve Programlama I, 14 hafta).

Kontroller:
  1. content/weeks altında 1..14 haftaların tamamı var mı, numaralar tekil mi?
     Her haftanın 'module' alanı modules.json'daki bir modülle eşleşiyor ve o modülün
     'weeks' listesinde yer alıyor mu? 'milestone' varsa course.json → portfolio'da tanımlı mı?
  2. content/labs altındaki lab-XX dosyaları: week 1..14 aralığında ve tekil mi, status geçerli mi,
     'milestone' tanımlı mı? (Her hafta için lab zorunlu değildir; eksikler uyarı olarak listelenir.)
  3. schedule.json: 14 satır, theory/lab tarihleri (A/B) geçerli mi, lab tarihi teori tarihinden
     SONRA mı (+1 hafta kuralı), status değerleri geçerli mi?
  4. course.json: sections (A/B), assistant, aiPolicy (kirmizi/sari/yesil), portfolio alanları var mı?
  5. Defter tanımlı haftalarda notebooks/*.ipynb ve public/notebooks/*.html var mı?
  6. (dist varsa) Üretilen HTML'deki iç bağlantılar mevcut dosyalara gidiyor mu?

Kullanım:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/validate_content.py [--strict]
  --strict: uyarıları da hata sayar (eksik lab dosyası, eksik tarih vb.)
"""
import json
import re
import sys
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
WEEKS_DIR = ROOT / "content" / "weeks"
LABS_DIR = ROOT / "content" / "labs"
DATA = ROOT / "content" / "data"
DIST = ROOT / "dist"
BASE = "/algoritma-ve-programlama-1"
TOTAL_WEEKS = 14
SECTIONS = ("A", "B")
STATUSES = {"normal", "tatil", "ertelendi", "sinav"}

errors: list[str] = []
warnings: list[str] = []


def load_json(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def frontmatter(path: Path) -> dict:
    """Basit YAML frontmatter okuyucu: yalnızca üst düzey 'anahtar: değer' satırları."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        errors.append(f"{path.name}: frontmatter yok")
        return {}
    fm: dict = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if mm and mm.group(2) != "":
            fm[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    return fm


def md_files(d: Path):
    return sorted(list(d.glob("*.md")) + list(d.glob("*.mdx"))) if d.exists() else []


def check_course():
    c = load_json("course.json")
    secs = {s.get("id") for s in c.get("sections", [])}
    if secs != set(SECTIONS):
        errors.append(f"course.json: sections A ve B tanımlı olmalı (bulunan: {sorted(secs)})")
    if not c.get("assistant", {}).get("name"):
        errors.append("course.json: assistant.name eksik")
    levels = {l.get("id") for l in c.get("aiPolicy", {}).get("levels", [])}
    if levels != {"kirmizi", "sari", "yesil"}:
        errors.append(f"course.json: aiPolicy.levels kirmizi/sari/yesil olmalı (bulunan: {sorted(levels)})")
    ms = c.get("portfolio", {}).get("milestones", [])
    ids = [m.get("id") for m in ms]
    if len(ids) != len(set(ids)):
        errors.append(f"course.json: portfolio.milestones id'leri tekil değil: {ids}")
    for m in ms:
        if not (1 <= int(m.get("week", 0)) <= TOTAL_WEEKS):
            errors.append(f"course.json: kilometre taşı {m.get('id')} haftası 1..{TOTAL_WEEKS} dışında")
    print(f"✓ course.json: {len(secs)} şube, {len(ids)} kilometre taşı ({', '.join(ids)})")
    return set(ids)


def check_weeks(milestones: set):
    modules = load_json("modules.json")
    mod_by_id = {m["id"]: m for m in modules}
    seen: dict[int, str] = {}
    for p in md_files(WEEKS_DIR):
        fm = frontmatter(p)
        try:
            n = int(fm.get("week", -1))
        except ValueError:
            errors.append(f"{p.name}: week sayısal değil")
            continue
        if n in seen:
            errors.append(f"{p.name}: hafta {n} zaten {seen[n]} dosyasında")
        seen[n] = p.name
        if not fm.get("title"):
            errors.append(f"{p.name}: title eksik")
        mod = fm.get("module")
        if mod not in mod_by_id:
            errors.append(f"{p.name}: bilinmeyen modül '{mod}'")
        elif n not in mod_by_id[mod]["weeks"]:
            errors.append(f"{p.name}: hafta {n}, modül {mod} 'weeks' listesinde yok")
        if fm.get("semester", "1") != "1":
            errors.append(f"{p.name}: semester 1 olmalı (tek yarıyıllık ders)")
        if fm.get("status", "taslak") not in {"taslak", "hazir"}:
            errors.append(f"{p.name}: geçersiz status '{fm.get('status')}'")
        ms = fm.get("milestone")
        if ms and ms not in milestones:
            errors.append(f"{p.name}: milestone '{ms}' course.json → portfolio.milestones içinde yok")
    missing = sorted(set(range(1, TOTAL_WEEKS + 1)) - set(seen))
    if missing:
        (warnings if not seen else errors).append(f"Eksik haftalar: {missing}")
    extra = sorted(set(seen) - set(range(1, TOTAL_WEEKS + 1)))
    if extra:
        errors.append(f"Beklenmeyen hafta numaraları: {extra}")
    union = sorted(w for m in modules for w in m["weeks"])
    if union != list(range(1, TOTAL_WEEKS + 1)):
        errors.append(f"modules.json haftaları 1..{TOTAL_WEEKS}'ü tam kapsamıyor: {union}")
    print(f"✓ {len(seen)}/{TOTAL_WEEKS} hafta dosyası, {len(modules)} modül")


def check_labs(milestones: set):
    seen: dict[int, str] = {}
    for p in md_files(LABS_DIR):
        fm = frontmatter(p)
        try:
            n = int(fm.get("week", -1))
        except ValueError:
            errors.append(f"{p.name}: week sayısal değil")
            continue
        if not (1 <= n <= TOTAL_WEEKS):
            errors.append(f"{p.name}: week {n} 1..{TOTAL_WEEKS} dışında")
        if n in seen:
            errors.append(f"{p.name}: hafta {n} labı zaten {seen[n]} dosyasında")
        seen[n] = p.name
        if not fm.get("title"):
            errors.append(f"{p.name}: title eksik")
        if fm.get("status", "taslak") not in {"taslak", "hazir"}:
            errors.append(f"{p.name}: geçersiz status '{fm.get('status')}'")
        ms = fm.get("milestone")
        if ms and ms not in milestones:
            errors.append(f"{p.name}: milestone '{ms}' course.json → portfolio.milestones içinde yok")
    missing = sorted(set(range(1, TOTAL_WEEKS + 1)) - set(seen))
    if missing:
        warnings.append(f"Lab dosyası olmayan haftalar (sitede 'hazırlanıyor' kutusu görünür): {missing}")
    print(f"✓ {len(seen)}/{TOTAL_WEEKS} lab dosyası")


def _iso(s: str, where: str):
    if not s:
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        errors.append(f"{where}: geçersiz tarih '{s}' (YYYY-AA-GG olmalı)")
        return None


def check_schedule():
    sch = load_json("schedule.json")["weeks"]
    nums = [r["week"] for r in sch]
    if nums != list(range(1, TOTAL_WEEKS + 1)):
        errors.append(f"schedule.json hafta sırası 1..{TOTAL_WEEKS} değil: {nums}")
    dated = 0
    prev_theory: dict[str, date] = {}
    for r in sch:
        w = r["week"]
        if r.get("status", "normal") not in STATUSES:
            errors.append(f"schedule hafta {w}: geçersiz status '{r.get('status')}'")
        if "date" in r and "theory" not in r:
            errors.append(f"schedule hafta {w}: eski 'date' alanı; 'theory': {{A,B}} ve 'lab': {{A,B}} kullanın")
            continue
        theory = r.get("theory", {}) or {}
        lab = r.get("lab", {}) or {}
        for s in SECTIONS:
            t = _iso(theory.get(s, ""), f"schedule hafta {w} theory.{s}")
            l = _iso(lab.get(s, ""), f"schedule hafta {w} lab.{s}")
            if t:
                dated += 1
                if s in prev_theory and prev_theory[s] >= t:
                    errors.append(f"schedule hafta {w} theory.{s}: {t} önceki haftadan sonra değil")
                prev_theory[s] = t
            if t and l:
                if l <= t:
                    errors.append(f"schedule hafta {w} lab.{s}: lab ({l}) teoriden ({t}) SONRA olmalı (+1 hafta kuralı)")
                elif l - t > timedelta(days=13):
                    warnings.append(f"schedule hafta {w} lab.{s}: lab teoriden {(l - t).days} gün sonra; +1 hafta kuralını kontrol edin")
            elif t and not l and r.get("status", "normal") == "normal":
                warnings.append(f"schedule hafta {w}: lab.{s} tarihi boş")
    print(f"✓ takvim: {dated}/{TOTAL_WEEKS * len(SECTIONS)} teori tarihi girilmiş")


def check_notebooks():
    n = 0
    for p in md_files(WEEKS_DIR):
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^notebook:\n(?:  .*\n)*?  file:\s*(\S+)", text, re.M)
        if not m:
            continue
        n += 1
        f = m.group(1).strip('"')
        if not (ROOT / f).exists():
            errors.append(f"{p.name}: defter dosyası yok: {f}")
        html = ROOT / "public" / "notebooks" / (Path(f).stem + ".html")
        if not html.exists():
            errors.append(f"{p.name}: gömülü görünüm yok: {html.relative_to(ROOT)} (scripts/build_notebooks.py çalıştırın)")
    print(f"✓ {n} haftada Java defteri tanımlı")


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for key in ("href", "src"):
            if key in a and a[key]:
                self.links.append(a[key])


def check_dist():
    if not DIST.exists():
        print("· dist yok, bağlantı kontrolü atlandı (npm run build sonrası çalıştırın)")
        return
    pages = list(DIST.rglob("*.html"))
    broken = set()
    for page in pages:
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for link in parser.links:
            u = urlsplit(link)
            if u.scheme or link.startswith("#") or link.startswith("mailto:"):
                continue
            page_url = "/" + page.relative_to(DIST).as_posix().replace("index.html", "")
            path = unquote(urlsplit(urljoin(BASE + page_url, link)).path)
            if not path.startswith(BASE + "/") and path != BASE:
                broken.add((page.relative_to(DIST).as_posix(), link, "base dışı"))
                continue
            rel = path[len(BASE):].lstrip("/")
            target = DIST / rel
            ok = target.exists() or (target / "index.html").exists() or (target.with_suffix(".html")).exists()
            if not ok:
                broken.add((page.relative_to(DIST).as_posix(), link, "hedef yok"))
    for b in sorted(broken):
        errors.append(f"kırık bağlantı: {b[0]} → {b[1]} ({b[2]})")
    week_pages = [p for p in pages if "haftalar/hafta-" in p.as_posix()]
    n_weeks = len(md_files(WEEKS_DIR))
    if len(week_pages) != n_weeks:
        errors.append(f"dist'te {len(week_pages)} hafta sayfası var, {n_weeks} bekleniyor")
    for p in pages:
        t = p.read_text(encoding="utf-8")
        if "Ã" in t or "Å" in t:
            errors.append(f"{p.relative_to(DIST)}: olası karakter kodlama hatası")
            break
    print(f"✓ dist: {len(pages)} sayfa, {len(week_pages)} hafta sayfası, bağlantılar tarandı")


def main():
    strict = "--strict" in sys.argv
    milestones = check_course()
    check_weeks(milestones)
    check_labs(milestones)
    check_schedule()
    check_notebooks()
    check_dist()
    if warnings:
        print("\n! UYARILAR:")
        for w in warnings:
            print("  -", w)
    if errors or (strict and warnings):
        print("\n✗ HATALAR:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("\nTüm kontroller geçti.")


if __name__ == "__main__":
    main()
