# Hafta 9 · Poll Everywhere soru seti (20 Kasım; metotlar I)

Öğretim üyesi notu (siteye girmez). Ders 60 dakikalık shot akışıyla, yedi kapsülle işleniyor (`docs/hafta-09-ders-senaryosu.md`); sorular akışa göre yerleşti: açılış hikayesi → 2. kapsül (tanım ve çağrı) → 4. kapsül (return ile println) → 5. kapsül (imza) → kapanış. Toplam 5 soru (kapanış iki parçalı); ★ işaretliler en etkilileri. Her iki şubede aynı set; sonuçları ayrı kaydet. Bütün çıktılar `content/weeks/hafta-09.mdx` içindeki kodlarla aynıdır.

---

## Açılış hikayesi (left-pad anlatıldıktan sonra, "tamamı kaç satırdı?" demeden hemen önce, 4. dk)

**1. Çoktan seçmeli: Silindiğinde binlerce projeyi durduran `left-pad` kaç satırlık bir koddu?**
Tür: Multiple Choice · Tek seçim · Sonuç hemen açık (ısınma)
- 11
- 110
- 1.100
- 11.000
Not: Birinci şık doğru. Bu soru bilgi ölçmüyor, beklentiyi kırıyor: "interneti durduran kod" deyince çoğunluk büyük bir sayı seçer. Oylamayı hikayede satır sayısını söylemeden **önce** aç; sonuç ekrandayken "on bir" de. Büyük sayıları seçenlere dön: "yazılım dünyası devasa programlardan değil, küçük ve adı konmuş parçalardan kurulu." Ardından açık soruyu bırak: "o on bir satırı yazabilir miydiniz?" Cevabı dersin sonuna sakla.

## 2. kapsül, ilk metot (dört satırlık `cizgi()` tanımı tahtaya yazıldıktan sonra, rol canlandırmasından ÖNCE, 15. dk)

**2. Çoktan seçmeli: Programda `cizgi` metodunun tanımı yazılı ama `main` içinde hiç çağrılmıyor. Program çalışınca çizgiyle ilgili ekrana ne çıkar?**
```java
static void cizgi() {
    System.out.println("--------------------");
}

public static void main(String[] args) {
    System.out.println("Basla");
    System.out.println("Bitti");
}
```
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra rol canlandırması, sonra sonucu aç)
- Hiçbir şey; yalnızca Basla ve Bitti yazılır
- Bir çizgi yazılır
- Program derlenmez
- Sonsuza kadar çizgi yazılır
Not: Birinci şık doğru: tanım bir tariftir, çağrılmadıkça çalışmaz. "Bir çizgi" diyenler **tanımı çağrı sanıyor**; metodun dosyada yazılı olmasının çalışması için yettiğini düşünüyorlar. Bu yüzde yüksekse rol canlandırmasında `cizgi` gönüllüsüne "sana seslenilmedikçe konuşma" de ve `main` onu hiç çağırmadan programı bitirsin; sınıf sessizliği görsün. "Derlenmez" diyenler kullanılmayan kodu hata sanıyor; Java için sorun değil. "Sonsuz çizgi" şakacı şık; seçen çıkarsa geçen haftanın sonsuz döngüsünü hatırlat ve geç.

## 4. kapsül, return ile println (izleme sorusu yansıtılıp iki dakikalık sessiz çalışma bittikten sonra, cevap açılmadan önce, 33. dk)

**3. ★ Çoktan seçmeli: Bu programın yazdığı ikinci satır hangisidir?**
```java
static int iki(int x) {
    x = x * 2;
    System.out.println("icerde " + x);
    return x + 1;
}

public static void main(String[] args) {
    int a = 3;
    int b = iki(a);
    System.out.println(a + " " + b);
}
```
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce kağıtta izle, sonra oyla, sonra kartı aç)
- 3 7
- 6 7
- 6 6
- 3 6
Not: Birinci şık doğru. İlk satır `icerde 6`, ikinci satır `3 7`. "6 7" diyenler **metodun `a`'yı değiştirdiğini** düşünüyor; bu, haftanın en değerli yanılgısı ve 10. haftanın pass by value açılışının malzemesi: "metot `a`'nın kendisini değil, değerinin bir kopyasını aldı." "3 6" diyenler `return x + 1`'deki `+ 1`'i atlıyor ya da metodun yazdırdığı değerle döndürdüğü değeri aynı sanıyor; otomat benzetmesine dön: "ekranda gösterdiği 6, elinize verdiği 7." "6 6" diyenler iki yanılgıyı birlikte taşıyor. "6 7" yüzdesini mutlaka kaydet.

## 5. kapsül, imza (`bolum(10, 4)` çalıştırılıp `2.5` görüldükten sonra, ikinci çağrı çalıştırılmadan önce, 39. dk)

**4. ★ Çoktan seçmeli: `bolum(4, 10)` çağrısı ne döndürür?**
```java
static double bolum(double bolunen, double bolen) {
    return bolunen / bolen;
}
```
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra Run)
- 2.5
- 0.4
- 0
- Derleme hatası
Not: İkinci şık doğru: argümanlar **sırayla** parametrelere konur, 4 bölünen olur, 10 bölen. "2.5" diyenler sıranın önemsiz olduğunu ya da programın "büyüğü küçüğe böleceğini" düşünüyor; Mars hikayesine geçişin tam yeri: "ikisi de derlendi, ikisi de çalıştı, biri yanlış." "0" diyenler 3. haftanın tam sayı bölmesini hatırlıyor; iyi bir refleks, ama parametreler `double` olduğu için 4 ve 10 ondalıklı sayıya dönüşüyor; bunu söyle ve tebrik et. "Derleme hatası" diyenler `int` argümanın `double` parametreye verilemeyeceğini sanıyor; verilebilir. Ardından `bolum(10)` yazıp gerçek derleme hatasını göster: derleyici sayıyı ve tipi denetler, sırayı ve birimi denetleyemez.

## Kapanış (`solaDoldur` kodu okunduktan sonra, kapanış duyurularından önce, 57. dk)

**5a. Çoktan seçmeli (çoklu seçim): Bugün hangi kapsül hâlâ bulanık? En fazla iki tane seçin.**
Tür: Multiple Choice · Çoklu seçim (en fazla 2) · Sonuç hemen açık
- 1 Hazır metotlar ve Math
- 2 İlk metot, çalışma akışı, parametre
- 3 return ve asalMi
- 4 return ile println farkı
- 5 İmza bir sözleşmedir
- 6 Metot metodu çağırır
- 7 LeetCode'a metot göndermek
- Hiçbiri, hepsi net
Not: En çok işaretlenen iki kapsülü yüksek sesle söyle ve sakinleştir: "bu konu sınavda yok; Lab 9'da ve haftaya üstünden yeniden geçeceğiz." 4. kapsül yüksek çıkarsa beklenen bir şey; Lab 9'un `fizzBuzz` görevi tam bunu çalıştırıyor, lab sorumlu hocasına ilet. 3. kapsül yüksek çıkarsa 10. haftanın açılışında `asalMi`'nin üç `return`'ünü iki dakikada yeniden izlet.

**5b. ★ Açık uçlu: Salı günkü sınav için en çok neye ihtiyacın var?**
Tür: Open-Ended (Text Wall) · Anonim
Not: Bu duvar hafta sonu göndereceğin vize planı mesajını belirliyor. Cevapları aynı gün oku ve kümelere ayır: "iç içe döngü izleme" (planın 16. ve 21. günleri), "break/continue" (17. gün), "nereden başlayacağımı bilmiyorum" (ikinci tur tek başına yeter: günde 25 dakika), "örnek soru" (hoca sınava benzer soru yayımlamıyor; 21 Kasım'daki "kendi deneme kağıdını yazdır" bloğuna yönlendir), "zaman yetmiyor" (dört iz tablosu, yarım saat). En sık geçen iki ihtiyaca göre WhatsApp kanalından kısa bir mesaj yaz. "Moral" ya da "korkuyorum" türü cevaplar gelirse kapanış cümlesini ona göre söyle: "Sekiz haftadır her kodu önce tahmin edip sonra çalıştırdınız; sınav o tahminin Run düğmesi olmayan hali."

---

### Kurulum ipuçları

- 2., 3. ve 4. sorularda "Show results" kapalı başlasın; önce oy, sonra gösteri (rol canlandırması / kart / Run), sonra sonuç. 1. ve 5a soruları sonuç açık.
- 2., 3. ve 4. sorulardaki kod bloklarını Poll Everywhere'e görsel olarak ekle (metin olarak girilirse girintiler bozulur).
- 3. soruyu izleme için verilen iki dakika **bittikten sonra** aç; soru açıkken kağıtta çalışmasınlar, cevaplarını işaretlesinler.
- 5a'da çoklu seçim açık ve "en fazla 2 seçim" sınırı konmuş olsun; 5b'de küfür filtresini aç.
- 2. sorunun "bir çizgi", 3. sorunun "6 7" ve 4. sorunun "2.5" yüzdelerini iki şube için ayrı kaydet; üçünü de lab sorumlu hocasına ilet.
- İnternet yoksa: şıkları tahtaya yaz, el kaldırt, sayıları senaryo belgesinin kenarına not et; 5b'yi küçük kağıtlara yazdırıp çıkışta topla.
