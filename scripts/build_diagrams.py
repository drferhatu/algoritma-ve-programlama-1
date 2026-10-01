#!/usr/bin/env python
"""Graphviz diyagramlarını SVG'ye derler.

content/diagrams/<ad>.dot  →  public/diagrams/<ad>.svg   (public/diagrams git'e girmez)

- Değişmemiş dosyalar atlanır (kaynak mtime ≤ SVG mtime); --force ile hepsi yeniden üretilir.
- `dot` bulunamazsa anlaşılır hata verir ve 1 ile çıkar (yerelde: brew install graphviz;
  CI'da: sudo apt-get install -y graphviz).
- Hatalı DOT dosyalarında dosya adı ve dot'un hata mesajı basılır; bitişte 1 ile çıkar.
- Türkçe karakterler için -Gcharset=utf8, yazı tipi Helvetica (düğüm/kenar/grafik).

Kullanım:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/build_diagrams.py [--force]
Saf Python; tek dış bağımlılık `dot` ikilisidir (subprocess ile çağrılır).
MDX'te kullanım: <Diagram name="h02-atm" caption="ATM para çekme akışı" dot />
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "content" / "diagrams"
OUT_DIR = ROOT / "public" / "diagrams"
FONT = "Helvetica"
DOT_ARGS = ["-Tsvg", "-Gcharset=utf8", "-Gbgcolor=transparent", f"-Gfontname={FONT}", f"-Nfontname={FONT}", f"-Efontname={FONT}"]


def find_dot() -> str | None:
    for cand in (shutil.which("dot"), "/opt/homebrew/bin/dot", "/usr/local/bin/dot", "/usr/bin/dot"):
        if cand and Path(cand).exists():
            return cand
    return None


def main() -> int:
    force = "--force" in sys.argv
    dot = find_dot()
    if not dot:
        print("✗ Graphviz `dot` bulunamadı. Kurulum: macOS → brew install graphviz · Ubuntu → sudo apt-get install -y graphviz")
        return 1
    if not SRC_DIR.exists():
        print(f"· {SRC_DIR.relative_to(ROOT)} yok; üretilecek diyagram yok.")
        return 0
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sources = sorted(p for p in SRC_DIR.glob("*.dot") if not p.name.startswith("."))
    built = skipped = failed = 0
    for src in sources:
        out = OUT_DIR / (src.stem + ".svg")
        if not force and out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
            skipped += 1
            continue
        r = subprocess.run([dot, *DOT_ARGS, str(src)], capture_output=True)
        if r.returncode != 0 or not r.stdout:
            failed += 1
            msg = (r.stderr or b"").decode("utf-8", "replace").strip() or f"dot çıkış kodu {r.returncode}"
            print(f"✗ {src.relative_to(ROOT)}:\n    " + msg.replace("\n", "\n    "))
            if out.exists():
                out.unlink()  # eski SVG'yi bırakma; site 'üretilmedi' uyarısı göstersin
            continue
        out.write_bytes(r.stdout)
        built += 1
        print(f"✓ {src.name} → {out.relative_to(ROOT)}")
    # kaynağı silinmiş diyagramların SVG'lerini temizle
    stale = [p for p in OUT_DIR.glob("*.svg") if not (SRC_DIR / (p.stem + ".dot")).exists()]
    for p in stale:
        p.unlink()
        print(f"· eski SVG silindi: {p.relative_to(ROOT)}")
    print(f"\n{built} üretildi, {skipped} güncel (atlandı), {failed} hatalı, {len(sources)} toplam")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
