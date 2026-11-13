# Hafta 8 · Poll Everywhere soru seti (13 Kasım; döngüler II)

Öğretim üyesi notu (siteye girmez). Ders 12 kapsülle işleniyor (`docs/hafta-08-ders-senaryosu.md`); sorular kapsüllere göre yerleşti: 1. kapsül (saat) → 4. kapsül (iz tablosu) → 5. kapsül (maliyet) → 7. kapsül (break) → 11. kapsül (FizzBuzz) → kapanış. Toplam 6 soru (kapanış iki parçalı); ★ işaretliler en etkilileri. Her iki şubede aynı set; sonuçları ayrı kaydet. Bütün sayılar `content/weeks/hafta-08.mdx` içindeki kodların gerçek çıktılarıdır.

---

## 1. kapsül, saat (akrep/yelkovan korosundan sonra, "Saat" kutusu çalıştırılmadan önce, 8. dk)

**1. Çoktan seçmeli: Dış döngü 2 kez, iç döngü 3 kez dönecek şekilde yazılmış iç içe döngünün gövdesindeki `println` kaç satır yazar?**
Tür: Multiple Choice · Tek seçim · Sonuç hemen açık (ısınma)
- 5
- 6
- 8
- 9
Not: İkinci şık doğru: 2 × 3 = 6 (çıktı `0:0, 0:1, 0:2, 1:0, 1:1, 1:2`). "5" diyenler iki sınırı **topluyor**; iç döngünün her dış turda baştan döndüğünü henüz görmediler, koroya geri dön: "yelkovan ikinci kez de üç saydı." "8" diyenler 2³ düşünüyor, "9" diyenler 3 × 3; ikisi de sınırları karıştırıyor. Ardından 24 × 60 = 1440'ı sor, sözle.

## 4. kapsül, iz tablosu (kod yansıtıldıktan sonra, üç dakikalık sessiz çalışmadan ÖNCE, 20. dk)

**2. ★ Çoktan seçmeli: Bu kodun son satırı ne yazar?**
```java
int toplam = 0;
for (int i = 1; i <= 3; i++) {
    for (int j = i; j <= 3; j++) {
        toplam = toplam + j;
    }
}
System.out.println("Toplam: " + toplam);
```
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra üç dakika iz tablosu, sonra Run, en son sonucu aç)
- Toplam: 6
- Toplam: 12
- Toplam: 14
- Toplam: 18
Not: Üçüncü şık doğru: (1,1) 1, (1,2) 3, (1,3) 6, (2,2) 8, (2,3) 11, (3,3) 14. "18" diyenler iç döngüyü her seferinde `j = 1`'den başlatıyor (3 × (1+2+3)); en yaygın hata bu olacak, `j = i`'yi parmakla göster. "6" diyenler iç döngüyü yalnızca bir dış tur için çalıştırıyor ya da tur sayısını (6) cevap sanıyor. "12" diyenler `i`'yi topluyor ya da bir turu atlıyor. İz tablosundan sonra aynı soruyu **yeniden oylat** (Poll Everywhere'de "clear responses"); iki sonucun farkı "tablo tutmanın" kanıtı, yüksek sesle söyle.

## 5. kapsül, maliyet ("El sıkışma sayacı" n = 1000 ve n = 10000 için çalıştırıldıktan hemen önce, 30. dk)

**3. ★ Çoktan seçmeli: Herkesin herkesle el sıkıştığı bir grupta kişi sayısı 10 katına çıkarsa el sıkışma sayısı yaklaşık kaç katına çıkar?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra 1000 ve 10000 ile Run)
- 10 kat
- 20 kat
- 100 kat
- 1000 kat
Not: Üçüncü şık doğru: 1000 kişi 499.500, 10.000 kişi 49.995.000; tam 100,09 kat. "10 kat" diyenler tek döngü gibi düşünüyor; bu yüzde GTA hikayesinin giriş cümlesi: "Rockstar'daki ekip de böyle düşündü." "20 kat" diyenler "iki döngü, iki katı" diyor: toplama ile çarpmanın karışması, Poll 1'deki "5" hatasının aynısı. "1000 kat" diyenler üç iç içe döngüyü tarif ediyor; "üçüncü bir döngü ekleseydik haklıydınız" de. Sonuçtan sonra tahtaya: `n × 10 → iş × 100`.

## 7. kapsül, break ("Üçün katlarını atla" çalıştırıldıktan sonra, "Çarpımı 42" kutusundan önce, 42. dk)

**4. Çoktan seçmeli: İç içe iki `for` döngüsünün iç döngüsünde çalışan bir `break` neyi bitirir?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra "Çarpımı 42" kutusunda bayrağı silip çalıştır)
- Yalnızca iç döngüyü
- Yalnızca dış döngüyü
- İki döngüyü birden
- Programın tamamını
Not: Birinci şık doğru. "İki döngüyü birden" en çok işaretlenecek yanlış; kanıtı kutuda: `&& !bulundu` parçasını sil, Run: `6 x 7 = 42`'den sonra `7 x 6 = 42` de yazılıyor, demek ki dış döngü sürmüş. Bayrağın neden gerektiği buradan çıkar. "Programın tamamını" diyenler `break` ile programın bitmesini karıştırıyor; "program döngüden sonraki satırla devam eder" de. Bu soru mülakat kartının (break/continue) ilk yarısı; kartın kendisi evde.

## 11. kapsül, FizzBuzz (üç dakikalık kağıtta FizzBuzz bittikten sonra, bir çözüm çalıştırılmadan önce, 64. dk)

**5. ★ Çoktan seçmeli: Bir FizzBuzz çözümünde else-if merdiveninin EN ÜSTÜNDE `i % 3 == 0` kontrolü var; `i % 15 == 0` kontrolü onun altında. Program 15 için ne yazar?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra gönüllünün kodunu ya da bu hatalı sürümü Playground'da çalıştır)
- Fizz
- Buzz
- FizzBuzz
- 15
Not: Birinci şık doğru: 15, `i % 3 == 0` koşuluna takılır, `Fizz` yazar ve merdivenin geri kalanına bakılmaz. "FizzBuzz" diyenler bütün koşulların sırayla denendiğini sanıyor; 4. haftanın else-if kuralını hatırlat: "ilk doğru dal çalışır, gerisi atlanır." "Buzz" ve "15" diyenler az olur; olursa merdiveni tahtada 15 için elle izlet. Bu yüzdeyi kaydet: kağıtta FizzBuzz'ı kaç kişinin bu hatayla yazdığının göstergesi ve Lab 8'in FizzBuzz görevinde beklenecek hata. Kapanış cümlesi: "en özel koşul en üstte."

## Kapanış (son 3 dakika; antrenman sahası tablosundan sonra)

**6a. Çoktan seçmeli (çoklu seçim): Bugünün kapsüllerinden hangisi hâlâ bulanık? (En fazla iki tane işaretleyin.)**
Tür: Multiple Choice · Çoklu seçim · Sonuç hemen açık
- 1 İç içe döngü (saat)
- 2 Çarpım tablosu
- 3 Desen (üçgen)
- 4 İz tablosu
- 5 Maliyet (el sıkışma)
- 6 break ve asal
- 7 continue ve bayrak
- 8 Basamak döngüsü
- 9 EBOB ve Euclid
- 10 Monte Carlo
- 11 FizzBuzz
- 12 Antrenman sahası
Not: En çok işaretlenen iki kapsülü yüksek sesle söyle: "o kapsülün Dene şeridi bu akşam ilk işiniz." Kısa geçilen kapsüller (2, 7, 8, 10) yüksek çıkarsa beklenen bir şey; mutlaka listesinden biri (özellikle 4 ya da 9) yüksek çıkarsa 9. haftanın açılışında iki dakikalık tekrar yap ve vize planının 16-17 Kasım günlerini hatırlat. Sonuçları lab sorumlu hocasına ilet; Lab 8'de o kapsüllerin görevlerinde (2 → çarpım tablosu, 3 → üçgen, 6 → asal, 9 → EBOB, 11 → FizzBuzz, 10 → bonus pi) daha çok soru beklesin.

**6b. ★ Açık uçlu: Bugün sınıfta olmasaydım neyi kaçırırdım?**
Tür: Open-Ended (Text Wall) · Anonim
Not: Bu haftanın asıl ölçüsü bu duvar. "El sıkışma", "koro", "üç dakikalık iz tablosu", "91'i sırayla bölmek", "kağıtta Euclid: 85'e karşı 3", "ayakta FizzBuzz", "GTA hikayesi" gelirse Sınıfta şeritleri tutmuş demektir. "Hiçbir şey, sayfada var" gelirse hangi etkinliğin kısaldığına bak ve 9. haftada o türden bir etkinliği öne al. En iyi üç cümleyi sakla: 9. haftanın açılışı ve MÜDEK kanıtı için.

---

### Kurulum ipuçları

- 2., 3., 4. ve 5. sorularda "Show results" kapalı başlasın; önce oy, sonra gösteri (iz tablosu / Playground), sonra sonuç. 1. ve 6a soruları sonuç açık.
- 2. soruyu iki kez oylatacaksın: ilk oylamanın ekran görüntüsünü al, cevapları temizle, iz tablosundan sonra yeniden aç. İki ekran görüntüsünü yan yana sakla.
- 2. sorudaki kod bloğunu Poll Everywhere'e görsel olarak ekle (metin olarak girilirse girintiler bozulur); görseli sayfadaki "İz tablosu alıştırması" kutusundan, iç `println` satırı çıkarılmış halde al.
- 6a'da çoklu seçim açık ve "en fazla 2 seçim" sınırı konmuş olsun; 6b'de küfür filtresini aç.
- 3. sorunun "10 kat", 4. sorunun "iki döngüyü birden" ve 5. sorunun "FizzBuzz" yüzdelerini iki şube için ayrı kaydet; üçünü de lab sorumlu hocasına ilet.
- İnternet yoksa: şıkları tahtaya yaz, el kaldırt, sayıları senaryo belgesinin kenarına not et.
