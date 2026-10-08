# Hafta 3 · Poll Everywhere soru seti

Öğretim üyesi notu (siteye girmez). Sıra, ders akışına göre: tipler → taşma → pizza → Scanner → kapanış. Toplam 5 soru; ★ işaretliler en etkilileri. Her iki şubede aynı set; sonuçları ayrı kaydet.

---

## Tipler bloğu (tablo gösterildikten sonra, Büyük Resim'den önce)

**1. ★ Çoktan seçmeli: Bir kantin uygulamasında ürün fiyatını hangi tipte tutarsınız?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (Büyük Resim'de açıklanacak)
- `int` (lira cinsinden, kuruşu atarız)
- `double` (45.50 gibi)
- `int` (kuruş cinsinden, 4550)
- `String` ("45,50 TL")
Not: Çoğunluk `double` der ve bu beklenen cevaptır; sonucu gösterip "Büyük Resim'de buna döneceğiz" de, açıklama yapma. Kantin bloğunda `0.1 + 0.2` sonucunu gösterdikten sonra sonucu yeniden aç: "Yüzde X'iniz banka olsaydı ay sonunda kasa tutmazdı." Üçüncü şık doğru. 4. haftada bu yüzdeyi hatırlat.

## Taşma (Playground'da çalıştırmadan hemen önce)

**2. ★ Çoktan seçmeli: Java'da `int buyuk = 2147483647;` yazıp `buyuk + 1` yazdırırsanız ne olur?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra çalıştır)
- 2147483648 yazar
- Program çöker, hata mesajı verir
- javac derlemez
- Eksi bir sayı yazar
Not: Dördüncü şık doğru (-2147483648). İkinci şıkkı seçenlere: "Keşke çökseydi; Ariane 5 tam da bunu bekliyordu, ama sayaç sessizce başa döner." Üçüncü şıkkı seçenlere: "javac bilmez; toplama çalışma zamanında yapılıyor." `2147483648` yazanlar kumbaranın kapasitesini unutmuş; Playground'da çalıştırıp göster.

## Pizza (Playground'da çalıştırmadan hemen önce)

**3. ★ Çoktan seçmeli: Java'da `7 / 2` kaç?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra çalıştır)
- 3
- 3.5
- Hata verir
- 4
Not: Doğru: 3. Geçen hafta hata avında `81.0`'ı gördüler, bu yüzden 3 diyenler artmış olmalı; 1. haftadaki aynı soruya göre değişimi söyle. 3.5 diyenlere pizza sahnesi: "bıçak yok." 4 diyenler yuvarlama bekliyor: "Java kesmekle yuvarlamayı ayırır; `(int) 3.9` için aynı tuzak az sonra." Sonra "`7 / 2.0` kaç?" diye sözlü sor, 3.5 cevabını al.

## Scanner (Enter tuzağını göstermeden hemen önce)

**4. ★ Çoktan seçmeli: Klavyede `19` yazıp Enter'a bastığınızda programa kaç karakter gider?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme
- 1 (sayı 19)
- 2 (1 ve 9)
- 3 (1, 9 ve Enter)
- Enter karakter değildir, yalnızca "gönder" demektir
Not: Üçüncü şık doğru. Dördüncü şıkkı seçenler çoğunlukta çıkarsa ders yerine oturmuş demek, çünkü tuzağın sebebi tam olarak bu inanç. Sonucu gösterdikten sonra terminalde `Tuzak.java`'yı çözüm satırı yorumlanmış halde çalıştır, boş adı göster, sonra "Enter nerede kaldı?" diye sor. Lab 3 Görev 5'e bağla.

## Kapanış (son 3 dakika)

**5. ★ Açık uçlu: Bugünden aklında kalan tek cümle?**
Tür: Open-Ended (Text Wall) · Anonim
Not: 4. haftanın açılışında bu duvardan 2-3 cümle okuyarak başla. "Enter da bir karakter", "bıçak yok", "kumbara taşınca eksiye düşer", "= kopyalama" cümleleri gelirse hikayeler tutmuş demektir. "double para" ya da "kuruş" geçen cümleleri lab sorumlu hocasıyla paylaş; Lab 3 bonus görevi (ParaUstu) için motivasyon.

---

### Kurulum ipuçları

- 2., 3. ve 4. sorularda "Show results" kapalı başlasın; önce oy, sonra çalıştır, sonra sonuç. Dersin "önce tahmin, sonra çalıştır" ritüeli.
- 1. soruyu tipler bloğunda sor ama sonucunu Büyük Resim'e kadar sakla; iki kez açılan tek soru bu.
- 5. soruda küfür filtresini aç.
- 1., 3. ve 4. soruların sonuçlarını iki şube için ayrı ekran görüntüsü olarak al; 3. sorunun "3.5" yüzdesini 1. haftadaki sözlü yoklamayla karşılaştır, 1. sorunun "double" yüzdesini 4. haftada ve vize öncesi (9. hafta) tekrar göster.
