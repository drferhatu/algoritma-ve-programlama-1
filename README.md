# Algoritma ve Programlama I — Ders Web Sitesi

Fırat Üniversitesi Teknoloji Fakültesi Yazılım Mühendisliği **YMT1101 Algoritma ve Programlama I** (Java, 2026–2027 Güz, 14 hafta, A ve B şubeleri) dersinin web sitesi.
Site tamamen statiktir, GitHub Pages üzerinde yayımlanır ve tüm ders içeriği koddan ayrı Markdown/JSON dosyalarında tutulur.

Canlı adres: `https://drferhatu.github.io/algoritma-ve-programlama-1/` · Depo: `drferhatu/algoritma-ve-programlama-1`

## Teknoloji

| Katman | Seçim | Neden |
|---|---|---|
| Çatı | [Astro 5](https://astro.build) | Sıfır istemci JavaScript varsayılanı, içerik koleksiyonları, statik çıktı |
| Stil | [Tailwind CSS 4](https://tailwindcss.com) | Tasarım sistemi tek CSS dosyasında token olarak (`src/styles/global.css`) |
| İçerik | Markdown/MDX + JSON | Haftalar ve lablar Markdown, künye/modüller/takvim JSON |
| Kod | Shiki | ```java blokları derlemede renklendirilir; `CodeTry` ile kopyalanır |
| Defterler | Jupyter + [IJava](https://github.com/SpencerPark/IJava) | Derste çalıştırılan Java defterleri sitede gömülü görünür |
| Arama | [Pagefind](https://pagefind.app) | Derleme sonrası tamamen statik arama dizini |
| Dağıtım | GitHub Actions → GitHub Pages | `main` dalına her push'ta otomatik derleme ve yayın |

## Klasör yapısı

```
content/
  data/course.json        künye, şubeler, asistan, amaç, öğrenim çıktıları, değerlendirme, aiPolicy, portfolio, kaynaklar
  data/modules.json       modüller (başlık, haftalar, renk, özet)
  data/schedule.json      haftalık teori ve lab tarihleri (A/B) ve durumlar (tatil/ertelendi/sınav)
  weeks/hafta-01.mdx …    14 haftalık teori dosyası (her hafta tek dosya; .md veya .mdx)
  labs/lab-01.md …        14 laboratuvar dosyası (haftanın sayfasında "Laboratuvar" sekmesi)
  guides/*.md             rehberler (/rehber/<ad>; liste /rehberler)
  announcements/*.md      duyurular
notebooks/hafta-XX.ipynb  Java (IJava) defterleri
src/
  pages/                  rotalar: index, ders-hakkinda, ders-akisi, haftalar/, laboratuvar/ (→ hafta#lab), rehberler, rehber/, kaynaklar, duyurular, arama
  components/             Roadmap, WeekCard, Toc, WeekPager, NotebookEmbed, CodeTry, Puzzle, AiPolicy, Portfolio, AiTools, Channels …
  layouts/BaseLayout.astro
  lib/site.ts             yardımcılar: href, şube/asistan/portfolyo erişimi, takvim (getTheoryDate, getLabDates, theoryLine, labLine), tarih biçimi
  lib/remark-callouts.mjs Markdown uyarı kutuları ([!not], [!uyari], [!ornek], [!neden], [!nerede], [!tanim])
  lib/rehype-base-links.mjs  Markdown'daki /haftalar/... bağlantılarına base yolunu ekler
  styles/global.css       tasarım sistemi (lacivert #1f2a44 + Java turuncusu #e76f00)
scripts/
  generate_week_files.py  hafta ve lab iskeletlerini üretir (mevcut dosyaları ezmez)
  validate_content.py     içerik + derleme doğrulaması (haftalar, lablar, takvim, defter, kırık bağlantı)
  build_notebooks.py      defterleri IJava ile çalıştırır ve HTML'e çevirir (kernel yoksa mevcut çıktıları kullanır)
  make_qr.py              iletişim kanalları için karekod üretir
public/                   favicon, og.png, robots.txt, .nojekyll, qr/
.github/workflows/deploy.yml  Java 21 + IJava + Node 22 ile GitHub Pages dağıtımı
```

## Yerel geliştirme

Gereksinim: Node.js 22+.

```bash
npm install
npm run dev        # http://localhost:4321/algoritma-ve-programlama-1/  (arama dev'de çalışmaz)
npm run build      # dist/ üretir ve Pagefind dizinini oluşturur
npm run preview    # dist/ klasörünü yerelde sunar (arama dâhil)
npm run check      # TypeScript / Astro tip denetimi
```

Python scriptleri için `ferhat_ml` conda ortamı kullanılır:

```bash
/opt/miniconda3/envs/ferhat_ml/bin/python scripts/validate_content.py          # içerik doğrulaması
/opt/miniconda3/envs/ferhat_ml/bin/python scripts/generate_week_files.py       # eksik hafta/lab iskeletleri
/opt/miniconda3/envs/ferhat_ml/bin/python scripts/build_notebooks.py --execute # defterleri çalıştır + HTML
```

## Veri sözleşmesi

### `content/data/course.json`

TIP sitesindeki alanlara ek olarak:

```json
"sections": [
  { "id": "A", "theory": "Cuma 09.15", "lab": "Çarşamba 13.15" },
  { "id": "B", "theory": "Cuma 13.15", "lab": "Perşembe 15.15" }
],
"assistant": { "name": "Arş. Gör. Ömer Miraç Kökçam", "role": "Laboratuvar" },
"aiPolicy": { "intro": "...", "levels": [ { "id": "kirmizi|sari|yesil", "label": "...", "where": "...", "rule": "...", "why": "..." } ] },
"portfolio": { "intro": "...", "milestones": [ { "id": "KT1", "week": 5, "title": "...", "desc": "..." } ], "rules": [ "..." ] }
```

`classTime` varsa künyede gösterilir; yoksa `sections`'tan üretilir. `aiTools` yapısı TIP ile aynıdır (Kaynaklar sayfasındaki araç kartları).

### `content/data/schedule.json` — teori ve lab tarihleri

```json
{ "week": 1,
  "theory": { "A": "2026-09-25", "B": "2026-09-25" },
  "lab":    { "A": "2026-09-30", "B": "2026-10-01" },
  "status": "normal", "note": "İlk ders" }
```

- **+1 hafta kuralı:** lab, aynı haftanın teorisinden **sonra** (ertesi Çarşamba A / Perşembe B) yapılır. `validate_content.py` lab tarihinin teoriden sonra olduğunu denetler.
- `status`: `normal` | `tatil` | `ertelendi` | `sinav`. Normal dışı durumlar kartlarda ve hafta sayfasında etiket olarak görünür; `note` kısa açıklamadır.
- Tarih boş bırakılırsa sitede yalnızca hafta numarası ve şube saati görünür.
- `src/lib/site.ts` eski tek `date` alanını geriye dönük olarak teori tarihine çevirir, ancak yeni içerik yalnızca `theory`/`lab` kullanmalıdır.

### `content/weeks/hafta-XX.md(x)` — teori

```yaml
---
week: 5
title: "Döngüler I: while ve do-while"     # sitede görünen başlık
topic: "Tekrar yapıları ..."                # resmî ders planındaki satır
description: "..."                          # kart ve meta açıklaması
module: m1                                  # modules.json'daki modül kimliği
semester: 1                                 # her zaman 1
exam: false                                 # true ise "Sınav" etiketi
status: taslak                              # taslak → "Hazırlık aşamasında" kutusu; notlar bitince hazir
changeNote: ""                              # dolu ise "Program değişikliği" uyarısı
milestone: KT1                              # isteğe bağlı; portfolyo kilometre taşı kutusu ve rozetleri
tags: [...]
objectives: [...]
tools: [...]
notebook: { file: notebooks/hafta-05.ipynb, title: "...", embed: true, placement: auto }   # isteğe bağlı
resources: [ { title: "…", url: "https://…", note: "…" } ]
---
```

Hafta sayfasında iki sekme vardır: **Teori** (bu dosya) ve **Laboratuvar** (`labs/lab-XX.md`). `#lab` hash'i ile doğrudan lab sekmesi açılır (`/haftalar/hafta-05#lab`; `/laboratuvar/lab-05` de oraya yönlendirir). JavaScript yoksa iki bölüm alt alta görünür.

### `content/labs/lab-XX.md` — laboratuvar

```yaml
---
week: 5
title: "Lab 5: Döngülerle sayı oyunları"
description: "..."
status: taslak                 # taslak | hazir
objectives: [...]
tools: [...]
deliverable: "Sayi.java dosyasını portfolyo klasörünüze ekleyin."   # isteğe bağlı; "Teslim" kutusu
milestone: KT1                 # isteğe bağlı
---
## Adımlar
...
```

Lab sekmesinde asistan adı, her iki şubenin lab tarihi, hedefler, gövde ve teslim kuralı gösterilir. Lab dosyası yoksa "Bu haftanın laboratuvar içeriği hazırlanıyor" kutusu çıkar.

## MDX bileşenleri

`.mdx` dosyalarında içe aktarmadan kullanılabilir (hafta ve lab gövdelerine `NotebookEmbed`, `CodeTry`, `Puzzle` otomatik sağlanır); `.md` dosyalarında bileşen kullanılamaz.

### `CodeTry` — kopyalanabilir Java kod bloğu

````mdx
<CodeTry title="Merhaba dünya" hint="Sınıf adı dosya adıyla aynı olmalı.">
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Merhaba");
    }
}
```
</CodeTry>
````

Üstte başlık, sağda **Kopyala** (kopyalanınca "Kopyalandı") ve **Java Playground'da dene ↗** (`https://dev.java/playground/`); altta `hint`. Kod bloğu Shiki ile normal renklendirilir.

### `Puzzle` — haftanın bulmacası

```mdx
<Puzzle title="Nehri geçen kurt, kuzu, lahana" kind="bulmaca">
Bir kayık bir seferde **tek** yolcu alıyor. Sıra ne olmalı?
</Puzzle>
```

`kind`: `bulmaca` (varsayılan) · `insan-bilgisayar` (kâğıt üstünde çalıştırma) · `tahmin` (çıktıyı tahmin et).

### Uyarı kutuları (Markdown)

```markdown
> [!neden] Neden önemli?
> ...
```

Türler: `not`, `uyari`, `ornek`, `neden`, `nerede`, `tanim`. Başka bir haftaya bağlantı için kök yol yazın; base otomatik eklenir: `[5. hafta](/haftalar/hafta-05)`.

## Java defterleri (Jupyter + IJava)

Derste çalıştırılan defterler `notebooks/hafta-XX.ipynb` dosyalarıdır ve **IJava** çekirdeğiyle çalışır. `scripts/build_notebooks.py --execute` defterleri çalıştırıp `public/notebooks/hafta-XX.html` üretir; IJava kernel'i bulunamazsa çalıştırmayı atlar ve defterdeki mevcut çıktıları HTML'e çevirir. Sitede `NotebookEmbed` bileşeni "GitHub'da gör" ve "Tam ekran" bağlantılarıyla gömülü görünümü gösterir (Colab yoktur; kod denemek için Java Playground önerilir).

Yerelde IJava kurulumu:

```bash
# Java 21 kurulu olmalı (java -version)
curl -sSL -o ijava.zip https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip
unzip -q ijava.zip -d ijava
/opt/miniconda3/envs/ferhat_ml/bin/python ijava/install.py --sys-prefix
```

## İçerik bakımı

- **Yeni hafta / lab iskeleti:** `generate_week_files.py` var olan dosyalara dokunmaz; `--weeks` / `--labs` ile sınırlanabilir, `--titles konu.json` ile başlıklar verilebilir, `--force` mevcutları **ezer**.
- **Tarih/tatil/erteleme:** `schedule.json` ilgili satırı; `note` alanı sayfada uyarı olarak görünür.
- **Duyuru:** `content/announcements/<ad>.md` (`title`, `date`, `pinned`, `kind: bilgi|onemli|sinav`).
- **Rehber:** `content/guides/<ad>.md` (`title`, `description`, `order`) → `/rehber/<ad>`, listesi `/rehberler`.
- **Karekodlar:** `course.json → channels` değişirse `scripts/make_qr.py`.
- Yayına almadan önce: `npm run build && /opt/miniconda3/envs/ferhat_ml/bin/python scripts/validate_content.py`.

## GitHub Pages dağıtımı

1. Depo: `drferhatu/algoritma-ve-programlama-1`. Ayarlar → Pages → Source: **GitHub Actions**.
2. `main` dalına push edildiğinde `.github/workflows/deploy.yml` çalışır: Java 21 (Temurin), Python bağımlılıkları, IJava kernel kurulumu, `build_notebooks.py --execute`, `npm ci`, `npm run build`, `validate_content.py` ve `dist/` yayını. IJava kurulumu başarısız olursa iş akışı durmaz; defterler mevcut çıktılarıyla çevrilir.
3. Base yolu `astro.config.mjs` içinde `/algoritma-ve-programlama-1`. Depo adı değişirse bu değeri, `public/robots.txt` ve `scripts/validate_content.py` içindeki `BASE` sabitini güncelleyin. Özel alan adına geçilirse `SITE_URL` ve `BASE_PATH=/` ortam değişkenleriyle derleyin.
