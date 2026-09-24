#!/usr/bin/env python
"""Haftalık Java defterlerini üretir ve sitede gömülmek üzere HTML'e çevirir.

- notebooks/hafta-XX.ipynb dosyalarını (yoksa) bu dosyadaki tanımlardan oluşturur.
- notebooks/ altındaki TÜM defterleri isteğe bağlı çalıştırır (--execute) ve HTML'e çevirir.
- Çalıştırma için Jupyter'de "java" çekirdeği (IJava) gerekir. Çekirdek yoksa uyarı verilir,
  çalıştırma atlanır ve defterdeki mevcut çıktılarla HTML üretilir.
- Hata veren hücreler defteri durdurmaz (allow_errors): bilerek hatalı hücreler ders materyalidir.
- nbconvert ile public/notebooks/<ad>.html üretir (site içinde iframe olarak gömülür).
  Çalıştırılan defter diske yazılmaz (--save verilmedikçe).

Kullanım:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/build_notebooks.py [--execute] [--save] [--force]

Java çekirdeği kurulumu (yerel, ferhat_ml ortamı):
  curl -sSL -o /tmp/ijava.zip https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip
  cd /tmp && unzip -o -q ijava.zip && /opt/miniconda3/envs/ferhat_ml/bin/python install.py --sys-prefix
  /opt/miniconda3/envs/ferhat_ml/bin/jupyter kernelspec list     # "java" görünmeli

GitHub Actions (ubuntu, JDK 21) için aynı adımlar; bkz. .github/workflows/deploy.yml.
"""
import sys
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

ROOT = Path(__file__).resolve().parent.parent
NB_DIR = ROOT / "notebooks"
OUT_DIR = ROOT / "public" / "notebooks"
REPO = "drferhatu/algoritma-ve-programlama-1"
KERNEL = "java"

md, code = new_markdown_cell, new_code_cell

# --------------------------------------------------------------------------
# HAFTA 1 - Algoritma Düşüncesi ve İlk Java
# --------------------------------------------------------------------------
WEEK01 = [
md("""# Hafta 1 · Algoritma Düşüncesi ve İlk Java

**YMT1101 Algoritma ve Programlama I** · Fırat Üniversitesi Yazılım Mühendisliği · Doç. Dr. Ferhat Uçar

Bu defter, dersin ilk saatinde birlikte **çalıştırıp okuduğumuz** kodların kaydıdır. Bugün kod yazmıyoruz;
her hücreyi çalıştırıyor, çıktısına bakıyor ve "ne oldu?" sorusunu cevaplıyoruz.

Kodlar JShell tarzındadır: sınıf ve `main` yazmadan doğrudan satır satır çalışır. Kendiniz denemek isterseniz
herhangi bir hücreyi kopyalayıp [Java Playground](https://dev.java/playground/) sayfasına yapıştırmanız yeterli;
kurulum gerekmez.

> Amaç bugün Java öğrenmek değil; *bir bilgisayara adım adım tarif vermenin* nasıl bir şey olduğunu görmek.
"""),

md("""## 1 · Merhaba

Bilgisayara bir şey söyletmenin en kısa yolu `System.out.println(...)`. Tırnak içindeki metni ekrana yazar
ve satırı bitirir. Satır sonundaki `;` Java'da cümlenin noktasıdır."""),
code('System.out.println("Merhaba! Bu dersin ilk satırı.");'),
md("""Metni bir kutuya koyup isim verebiliriz. Aşağıdaki `ad` bir **değişken**: bir değeri isimle saklar.
`+` işareti iki metni uç uca ekler."""),
code('''String ad = "Ferhat";
System.out.println("Merhaba " + ad + ", Algoritma ve Programlama dersine hoş geldin.");'''),

md("""## 2 · Değişken ve hesap

Sayılar için iki temel tip var: `int` (tam sayı) ve `double` (ondalıklı sayı). Bilgisayar bunları farklı saklar
ve farklı hesaplar. Aşağıdaki iki bölmeden **hangisi 3, hangisi 3.5 verir?** Çalıştırmadan önce tahmin edin."""),
code('''int a = 7;
int b = 2;
double c = 2.0;

System.out.println("7 / 2   = " + (a / b));
System.out.println("7 / 2.0 = " + (a / c));'''),
md("""İki tam sayının bölümü yine tam sayıdır; küsurat **atılır**, yuvarlanmaz. Bu, ileride en çok hata yapılan yerlerden biri.

Kalanı bulmak için `%` (mod) operatörü var. "17'yi 5'e bölünce kaç artar?" sorusunun cevabı:"""),
code('''System.out.println("17 % 5 = " + (17 % 5));
System.out.println("20 % 5 = " + (20 % 5));
System.out.println("9 % 2  = " + (9 % 2) + "   (tek sayı: kalan 1)");'''),

md("""## 3 · Karar

Program her zaman düz bir yol izlemez; bazen bir soruya göre yön değiştirir. `if` ... `else` yapısı bunu sağlar.
`sayi % 2 == 0` ifadesi "ikiye bölünce kalan sıfır mı?" diye sorar; `==` karşılaştırma, `=` atamadır."""),
code('''int sayi = 17;

if (sayi % 2 == 0) {
    System.out.println(sayi + " çift sayıdır.");
} else {
    System.out.println(sayi + " tek sayıdır.");
}'''),
md("""> **Deneyin:** `sayi` değerini 18, 0 ve -7 yapıp hücreyi yeniden çalıştırın. Sonuç beklediğiniz gibi mi?"""),

md("""## 4 · Tekrar

Bilgisayarın asıl gücü aynı işi bıkmadan tekrarlamak. `for` döngüsü üç parçadan oluşur:
başlangıç (`int i = 1`), devam koşulu (`i <= 10`) ve her turdaki adım (`i++`, yani "i'yi bir artır")."""),
code('''for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}'''),
md("""Şimdi aynı döngüyü bir şey **biriktirmek** için kullanalım: 1'den 100'e kadar sayıların toplamı.
`toplam` değişkeni sıfırdan başlar, her turda üstüne `i` eklenir."""),
code('''int toplam = 0;
for (int i = 1; i <= 100; i++) {
    toplam = toplam + i;
}
System.out.println("1'den 100'e toplam: " + toplam);'''),
md("""> Gauss bunu döngü kurmadan, `100 * 101 / 2` formülüyle bulmuştu. İki yol da doğru; biri hesap, biri fikir.
> Hangisinin "daha iyi" olduğu sorusu bu dersin sonuna doğru (verimlilik) tekrar karşımıza çıkacak."""),

md("""## 5 · Bilerek hata

Programcılığın ilk becerisi hata mesajından korkmamak. Aşağıdaki hücrede **iki hata** var:
ilk satırda noktalı virgül eksik, ikinci satırda hiç tanımlanmamış bir değişken kullanılıyor.
Çalıştırın ve mesajı **sonuna kadar** okuyun: bilgisayar size tam olarak neyi beğenmediğini söylüyor."""),
code('''int yas = 20
System.out.println("Yaş: " + yaş);'''),
md("""`';' expected` demek "burada noktalı virgül bekliyordum". Java önce bunu görür ve durur; ikinci hata (`yaş`
tanımlı değil, çünkü değişkenin adı `yas`) ancak ilki düzeltilince ortaya çıkar. Hata mesajı bir ceza değil,
bir **ipucu**. Düzeltilmiş hali:"""),
code('''int yas = 20;
System.out.println("Yaş: " + yas);'''),

md("""## 6 · Bir algoritma: Babil karekök yöntemi

Algoritma, bir işi adım adım yapan **tarif**tir. Yaklaşık 4000 yıl önce Babilliler karekökü şöyle buluyordu:

1. Bir tahminle başla (mesela sayının kendisi).
2. Tahmin ile "sayı bölü tahmin"in ortalamasını al; bu yeni tahmin olsun.
3. Tahmin yeterince iyi olana kadar 2. adımı tekrarla.

Kaç kez tekrarlayacağımızı önceden bilmiyoruz, o yüzden `for` yerine `while` kullanıyoruz:
"koşul doğru olduğu sürece tekrar et"."""),
code('''double sayi = 25;
double tahmin = sayi;          // 1. adım: ilk tahmin
int adim = 0;

while (Math.abs(tahmin * tahmin - sayi) > 0.000001) {   // 3. adım: yeterince iyi değilse devam
    tahmin = (tahmin + sayi / tahmin) / 2;              // 2. adım: ortalama al
    adim++;
    System.out.println("Adım " + adim + ": tahmin = " + tahmin);
}

System.out.println("Sonuç: " + tahmin + "  (" + adim + " adımda)");'''),
md("""> Beş altı adımda 5'e ulaştı. Tarifin her satırı koda birebir karşılık geliyor; **kod, tarifin yazıya dökülmüş hali.**
> `sayi` değerini 2 yapın: hiç bitmeyecek gibi görünen bir sayıya bilgisayar nasıl yaklaşıyor?"""),

md("""## 7 · Bir bulmaca: nehri geçen çiftçi

Bir çiftçi, bir kurt, bir keçi ve bir lahana nehrin bir kıyısında. Kayığa çiftçiyle birlikte yalnızca **bir** şey sığıyor.
Çiftçi yanlarında değilken kurt keçiyi, keçi de lahanayı yer. Hepsini sağ salim karşıya nasıl geçirir?

Bunu önce kağıt üzerinde çözün. Sonra şunu düşünün: bu çözümü bilgisayara nasıl **tarif** ederiz?
Bilgisayarın deneme yanılma yapıp çözümü kendisinin bulması için ne söylememiz gerekir?

Aşağıda hazır bir çözüm var. Bugün sadece çalıştırıp çıktısını okuyoruz; **13. haftada bu programı siz yazacaksınız.**
O zamana kadar diziler, metotlar ve arama fikri elimizde olacak."""),
code('''import java.util.*;

// Durum: 4 elemanlı boolean dizisi. false = sol kıyı, true = sağ kıyı.
// Sıra: [0] çiftçi, [1] kurt, [2] keçi, [3] lahana
String[] isim = {"çiftçi", "kurt", "keçi", "lahana"};

// Çiftçi yanlarında değilken kurt-keçi ya da keçi-lahana aynı kıyıda kalamaz
boolean guvenli(boolean[] d) {
    if (d[1] == d[2] && d[0] != d[2]) return false;
    if (d[2] == d[3] && d[0] != d[2]) return false;
    return true;
}

// Deneme yanılma: her olası hamleyi dene, çıkmaza girersen geri al
boolean coz(boolean[] d, Set<String> gorulen, List<String> hamleler) {
    if (d[0] && d[1] && d[2] && d[3]) return true;              // herkes karşıda: bitti
    if (!gorulen.add(Arrays.toString(d))) return false;         // bu durumu daha önce gördük
    for (int y = 0; y < 4; y++) {                               // y = 0: çiftçi tek başına gider
        if (d[y] != d[0]) continue;                             // yolcu çiftçiyle aynı kıyıda olmalı
        boolean[] yeni = d.clone();
        yeni[0] = !yeni[0];                                     // çiftçi karşıya
        if (y != 0) yeni[y] = !yeni[y];                         // yanında yolcu varsa o da
        if (!guvenli(yeni)) continue;
        String yon = yeni[0] ? "karşıya" : "geri";
        String kim = (y == 0) ? "tek başına" : isim[y] + " ile";
        hamleler.add("Çiftçi " + kim + " " + yon);
        if (coz(yeni, gorulen, hamleler)) return true;
        hamleler.remove(hamleler.size() - 1);                   // olmadı, hamleyi geri al
    }
    return false;
}

List<String> hamleler = new ArrayList<>();
coz(new boolean[4], new HashSet<>(), hamleler);
for (int i = 0; i < hamleler.size(); i++) System.out.println((i + 1) + ". " + hamleler.get(i));'''),
md("""> Yedi hamle. Bilgisayara "çözümü" söylemedik; sadece **kuralları** (neyin güvenli olduğu) ve **deneme yöntemini**
> (bir hamle yap, olmadıysa geri al) tarif ettik. Çözümü kendisi buldu. Algoritma düşüncesi tam olarak bu."""),

md("""## 8 · Bugün ne gördük?

| Bölüm | Ne yaptık | Hangi haftada derinleşecek |
|---|---|---|
| 1 | İlk `println`, `String` değişken | Hafta 2 |
| 2 | `int` / `double`, bölme ve `%` | Hafta 2-3 |
| 3 | `if` / `else` ile karar | Hafta 4 |
| 4 | `for` döngüsü, biriktirme | Hafta 5-6 |
| 5 | Hata mesajı okuma | Her hafta |
| 6 | `while` ile bir algoritma (Babil) | Hafta 6-7 |
| 7 | Dizi, metot, deneme yanılma ile arama | Hafta 8-13 |

**Eve ödev (isteğe bağlı, 10 dk):** [Java Playground](https://dev.java/playground/)'ı açın, 3. bölümdeki karar
hücresini yapıştırıp `sayi` değerini değiştirerek çalıştırın. Sonra 4. bölümdeki toplamı 1'den 1000'e çıkarın.
Bir hata alırsanız mesajı okuyun; gelecek hafta ilk beş dakikada bu hataları konuşacağız.
"""),
]

NOTEBOOKS = {"hafta-01": ("Hafta 1 · Algoritma Düşüncesi ve İlk Java", WEEK01)}

# Çıktı gizleme: ders anına kadar sitedeki gömülü görünümde hücre ÇIKTILARI gösterilmez
# (kod görünür, çıktı "önce tahmin edin" kutusuyla saklanır). Saat geçince derleme
# çıktıları açar; GitHub Actions her Cuma akşamı ve her push'ta yeniden derler.
# Depoya kaydedilen .ipynb dosyalarında çıktı tutulmaz (--save verilmedikçe).
from datetime import datetime, timezone, timedelta
TR = timezone(timedelta(hours=3))
REVEAL_AFTER = {
    "hafta-01": datetime(2026, 9, 25, 16, 0, tzinfo=TR),
}


def outputs_hidden(name):
    t = REVEAL_AFTER.get(name)
    return t is not None and datetime.now(TR) < t


def strip_outputs(nb):
    import copy
    nb = copy.deepcopy(nb)
    for c in nb.cells:
        if c.cell_type == "code":
            c.outputs = []
            c.execution_count = None
    return nb


def build(name, title, cells, force=False):
    path = NB_DIR / f"{name}.ipynb"
    if path.exists() and not force:
        print(f"· {path.name} mevcut, korunuyor")
    else:
        nb = new_notebook(cells=cells, metadata={
            "kernelspec": {"name": KERNEL, "display_name": "Java", "language": "java"},
            "language_info": {"name": "Java", "file_extension": ".jshell", "mimetype": "text/x-java-source",
                              "codemirror_mode": "java", "pygments_lexer": "java"},
            "title": title,
        })
        nbformat.write(nb, path)
        print(f"✓ {path.name} yazıldı")
    return path


def kernel_available():
    from jupyter_client.kernelspec import KernelSpecManager, NoSuchKernel
    try:
        KernelSpecManager().get_kernel_spec(KERNEL)
        return True
    except NoSuchKernel:
        return False


def execute(path, save=False):
    from nbclient import NotebookClient
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=300, kernel_name=KERNEL, allow_errors=True,
                            resources={"metadata": {"path": str(path.parent)}})
    client.execute()
    for c in nb.cells:  # IJava her println'i ayrı parça gönderir; ardışık stdout parçalarını birleştir
        if c.cell_type == "code":
            merged = []
            for o in c.outputs:
                if (merged and o.output_type == "stream" and merged[-1].output_type == "stream"
                        and o.name == merged[-1].name):
                    merged[-1].text += o.text
                else:
                    merged.append(o)
            c.outputs = merged
    if save:
        nbformat.write(nb, path)
    errs = [o for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.get("output_type") == "error"]
    print(f"✓ {path.name} çalıştırıldı ({len(errs)} hata hücresi)")
    return nb


def to_html(path, nb=None):
    from nbconvert import HTMLExporter
    exp = HTMLExporter(template_name="lab")
    exp.exclude_input_prompt = True
    exp.exclude_output_prompt = True
    if nb is None:
        nb = nbformat.read(path, as_version=4)
    hidden = outputs_hidden(path.stem)
    if hidden:
        nb = strip_outputs(nb)
        t = REVEAL_AFTER[path.stem]
        nb.cells.insert(1, nbformat.v4.new_markdown_cell(
            f"> **Çıktılar şimdilik gizli.** Her hücrenin ne yazdıracağını önce kendiniz tahmin edin, "
            f"derste birlikte çalıştıracağız. Çıktılar {t.strftime('%d.%m.%Y %H.%M')} sonrasında bu sayfada görünür."))
    body, _ = exp.from_notebook_node(nb)
    # site zeminiyle uyum ve iframe içinde ferah görünüm
    body = body.replace("</head>", """<style>
      body{background:#fff !important;margin:0}
      .jp-Notebook{padding:16px 20px !important;max-width:100% !important}
      .jp-Cell{padding:0 !important}
      .jp-InputArea-editor{border-radius:10px;border:1px solid #e3ddd2}
      .jp-RenderedHTMLCommon{font-family:Manrope,system-ui,sans-serif;color:#10262e}
      .jp-RenderedHTMLCommon table{font-size:13px}
      .jp-OutputArea-output pre{white-space:pre-wrap}
    </style></head>""")
    out = OUT_DIR / f"{path.stem}.html"
    out.write_text(body, encoding="utf-8")
    print(f"✓ {out.relative_to(ROOT)} ({len(body)//1024} KB){' [çıktılar gizli]' if hidden else ''}")


def main():
    force = "--force" in sys.argv
    run = "--execute" in sys.argv
    save = "--save" in sys.argv
    NB_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, (title, cells) in NOTEBOOKS.items():
        build(name, title, cells, force)
    if run and not kernel_available():
        print(f"! Jupyter'de '{KERNEL}' çekirdeği yok; çalıştırma atlanıyor, defterlerdeki mevcut çıktılar kullanılacak.\n"
              f"  Kurulum: bkz. bu dosyanın başlığı (IJava).", file=sys.stderr)
        run = False
    for p in sorted(NB_DIR.glob("*.ipynb")):
        nb = execute(p, save=save) if run else None
        to_html(p, nb)
    print(f"\nDefter kaynağı: https://github.com/{REPO}/blob/main/notebooks/<ad>.ipynb")


if __name__ == "__main__":
    main()
