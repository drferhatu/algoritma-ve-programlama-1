#!/usr/bin/env python
"""14 haftalık Algoritma ve Programlama I için content/weeks/hafta-XX.md ve
content/labs/lab-XX.md İSKELETLERİNİ üretir.

Yalnızca ilk iskelet içindir: var olan bir dosyanın üzerine YAZMAZ (--force verilmedikçe).
Böylece elle yazılmış ders notları ve lab yönergeleri korunur.

Başlıklar/konular için öncelik sırası:
  1. --titles <dosya.json>  → [{"week":1,"title":"...","topic":"...","description":"...","labTitle":"..."}, ...]
  2. Bu dosyadaki TOPICS listesi (varsayılan ders planı özeti)
Modül ataması content/data/modules.json'dan, tarih notları schedule.json'dan okunur.

Kullanım:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/generate_week_files.py [--weeks] [--labs] [--force] [--titles konu.json]
  (bayrak verilmezse hem weeks hem labs üretilir)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEEKS_OUT = ROOT / "content" / "weeks"
LABS_OUT = ROOT / "content" / "labs"
DATA = ROOT / "content" / "data"
TOTAL_WEEKS = 14

MODULES = json.loads((DATA / "modules.json").read_text(encoding="utf-8"))
try:
    SCHEDULE = {r["week"]: r for r in json.loads((DATA / "schedule.json").read_text(encoding="utf-8"))["weeks"]}
except Exception:  # noqa: BLE001
    SCHEDULE = {}
try:
    MILESTONES = {m["week"]: m["id"] for m in json.loads((DATA / "course.json").read_text(encoding="utf-8")).get("portfolio", {}).get("milestones", [])}
except Exception:  # noqa: BLE001
    MILESTONES = {}

# Varsayılan ders planı (içerik ekibi --titles ile ezebilir)
TOPICS = [
    dict(week=1, title="Algoritma Nedir? İlk Java Programı", topic="Algoritma kavramı, akış şeması, Java çalışma ortamı ve ilk program"),
    dict(week=2, title="Değişkenler, Veri Tipleri ve Aritmetik", topic="Değişken, ilkel tipler, operatörler, tip dönüşümü"),
    dict(week=3, title="Girdi/Çıktı ve Koşullu İfadeler", topic="Scanner ile girdi, if/else, mantıksal operatörler"),
    dict(week=4, title="Çok Yollu Karar: switch ve İç İçe Koşullar", topic="switch, iç içe if, karar tabloları"),
    dict(week=5, title="Döngüler I: while ve do-while", topic="Tekrar yapıları, sayaç ve toplayıcı deseni"),
    dict(week=6, title="Döngüler II: for ve İç İçe Döngüler", topic="for döngüsü, iç içe döngüler, desen çizme"),
    dict(week=7, title="Metotlar I: Parçala ve Yönet", topic="Metot tanımlama, parametre, dönüş değeri"),
    dict(week=8, title="Ara Sınav ve Genel Tekrar", topic="Ara sınav haftası"),
    dict(week=9, title="Metotlar II ve Kapsam", topic="Aşırı yükleme, kapsam, özyinelemeye giriş"),
    dict(week=10, title="Diziler I", topic="Tek boyutlu diziler, dolaşma, arama"),
    dict(week=11, title="Diziler II ve Sıralama", topic="Çok boyutlu diziler, temel sıralama algoritmaları"),
    dict(week=12, title="Karakter Dizileri (String)", topic="String işlemleri, karakter dizileriyle algoritmalar"),
    dict(week=13, title="Sınıf ve Nesneye Giriş", topic="Sınıf, nesne, alan, metot; basit modelleme"),
    dict(week=14, title="Dönem Projesi ve Portfolyo Sunumları", topic="Portfolyo teslimi, sunumlar ve genel değerlendirme"),
]


def module_of(week: int):
    for m in MODULES:
        if week in m["weeks"]:
            return m
    raise KeyError(f"modules.json'da {week}. hafta yok")


def q(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def yaml_field(name: str, items) -> str:
    """'name:' + girintili liste; boş listede 'name: []'."""
    if not items:
        return f"{name}: []"
    return f"{name}:\n" + "\n".join(f"  - {q(i)}" for i in items)


def render_week(t: dict) -> str:
    n = t["week"]
    m = module_of(n)
    s = SCHEDULE.get(n, {})
    exam = s.get("status") == "sinav"
    fm = [
        "---",
        f"week: {n}",
        f"title: {q(t['title'])}",
        f"topic: {q(t['topic'])}",
        f"description: {q(t.get('description') or t['topic'] + '.')}",
        f"module: {m['id']}",
        "semester: 1",
        f"exam: {'true' if exam else 'false'}",
        "status: taslak",
        'changeNote: ""',
        yaml_field("tags", t.get("tags", ["java"])),
        yaml_field("objectives", t.get("objectives", [])),
        yaml_field("tools", t.get("tools", ["Java 21", "Java Playground"])),
    ]
    if n in MILESTONES:
        fm.append(f"milestone: {MILESTONES[n]}")
    fm.append("---")
    body = [
        "## Haftanın Bulmacası", "",
        "> [!not] Bu bölüm bir `<Puzzle>` bileşeniyle değiştirilecek (dosyayı .mdx yapın).", "",
        "## Ders Notları", "",
        f"> [!not] Haftanın ders planı başlığı: **{t['topic']}**", "",
        "Ders notları ilerleyen haftalarda buraya eklenecektir.", "",
        "## Temel Kavramlar", "", "- **Kavram** — açıklama", "",
        "## Örnekler", "", "- Örnek", "",
        "## Alıştırma", "", "Bu hafta evde deneyeceğiniz küçük program.", "",
        "## Haftanın Özeti", "", "Özet.", "",
    ]
    return "\n".join(fm) + "\n\n" + "\n".join(body)


def render_lab(t: dict) -> str:
    n = t["week"]
    fm = [
        "---",
        f"week: {n}",
        f"title: {q(t.get('labTitle') or f'Lab {n}: ' + t['title'])}",
        f"description: {q(t.get('labDescription') or f'{n}. haftanın konusunun laboratuvar uygulaması.')}",
        "status: taslak",
        yaml_field("objectives", t.get("labObjectives", [])),
        yaml_field("tools", t.get("labTools", ["Java 21", "Bir metin editörü / IDE"])),
        f"deliverable: {q(t.get('deliverable') or 'Çalışan .java dosyanızı portfolyo klasörünüze ekleyin.')}",
    ]
    if n in MILESTONES:
        fm.append(f"milestone: {MILESTONES[n]}")
    fm.append("---")
    body = [
        "## Hazırlık", "", "Lab öncesi yapılacaklar.", "",
        "## Adımlar", "", "1. Adım", "2. Adım", "",
        "## Teslim", "", "Teslim kuralı frontmatter'daki `deliverable` alanında; burada ayrıntı verilebilir.", "",
    ]
    return "\n".join(fm) + "\n\n" + "\n".join(body)


def write_all(out: Path, prefix: str, render, topics, force: bool):
    out.mkdir(parents=True, exist_ok=True)
    written = skipped = 0
    for t in topics:
        path = out / f"{prefix}-{t['week']:02d}.md"
        if (path.exists() or path.with_suffix(".mdx").exists()) and not force:
            skipped += 1
            continue
        path.write_text(render(t), encoding="utf-8")
        written += 1
    print(f"{prefix}: yazıldı {written}, atlandı (mevcut) {skipped} → {out.relative_to(ROOT)}")


def main():
    args = sys.argv[1:]
    force = "--force" in args
    topics = TOPICS
    if "--titles" in args:
        p = Path(args[args.index("--titles") + 1])
        override = {t["week"]: t for t in json.loads(p.read_text(encoding="utf-8"))}
        topics = [{**t, **override.get(t["week"], {})} for t in TOPICS]
    assert [t["week"] for t in topics] == list(range(1, TOTAL_WEEKS + 1)), f"{TOTAL_WEEKS} hafta olmalı"
    do_weeks = "--weeks" in args or "--labs" not in args
    do_labs = "--labs" in args or "--weeks" not in args
    if do_weeks:
        write_all(WEEKS_OUT, "hafta", render_week, topics, force)
    if do_labs:
        write_all(LABS_OUT, "lab", render_lab, topics, force)


if __name__ == "__main__":
    main()
