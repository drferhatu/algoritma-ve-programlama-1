# Hafta 7 · Poll Everywhere soru seti (6 Kasım; bayramdan ötelenen döngüler I dersi)

Öğretim üyesi notu (siteye girmez). Sıra, ders akışına göre: neden döngü → do-while en az kaç kez → gözcü toplanır mı → for mu while mi → kapanış. Toplam 5 soru; ★ işaretliler en etkilileri. Her iki şubede aynı set; sonuçları ayrı kaydet.

---

## while bloğu (dört satırlık Merhaba tahtada izlendikten sonra, "1'den 10'a toplam" çalıştırılmadan önce, 10-12. dk)

**1. Çoktan seçmeli: Ekrana 100 kez "Merhaba" yazdırmak için döngüyle en az kaç satır kod gerekir?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra tahtadaki dört satırı say)
- 100
- 10
- 4
- 1
Not: Üçüncü şık doğru (başlangıç, while satırı, println, adım; süslü parantezleri saymıyoruz). "1" diyenler: for ile de en az iki satır (for satırı + println); yine de "tek satır" hissi doğru yönde, for bölümünde hatırlat. "100" diyen varsa bulmacanın gönüllüsü. Dersin mesajı: satır sayısı değil, "bir kez yaz, yüz kez çalıştır"; bu soru ısınma.

## do-while bloğu ("Hiç mi, en az bir mi?" kutusu çalıştırılmadan hemen önce, 22. dk)

**2. ★ Çoktan seçmeli: `para = 50` iken `do { ... } while (para < 20);` döngüsünün gövdesi kaç kez çalışır?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra Playground'da çalıştır)
- 0 kez, çünkü 50 zaten 20'den büyük
- Tam 1 kez
- Sonsuz kez
- Derleme hatası
Not: İkinci şık doğru; gövde koşuldan önce çalışır. Birinci şıkkı seçenler while ile karıştırıyor: "while böyle yapardı; do-while önce yapar sonra sorar; otomat." Sonucu gösterdikten sonra sözlü ek soru: "Aynı kodu while ile yazsaydım?" → 0. Bu soru dersin "en az bir kez" cümlesinin ölçüsü; Lab 7 Görev 4'te do-while yerine while yazanların oranını tahmin ettirir.

## Gözcü bloğu (Kasa.java çalıştırıldıktan sonra, "gövdenin başında okuyup hemen toplasaydım" tuzağı anlatılmadan önce, 40. dk)

**3. ★ Çoktan seçmeli: Gözcü değer `0` olan bir toplama döngüsünde kullanıcı `5 7 3 0` giriyor. Gözcü `0` toplama eklenir mi?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme
- Evet, döngü içinde okunan her şey toplanır
- Hayır, gözcü yalnızca döngüyü bitirir, işlenmez
- Fark etmez, 0 eklense de toplam değişmez
- Duruma göre: önce okuyup sonra sorarsak toplanmaz, önce toplayıp sonra sorarsak toplanır
Not: İkinci şık **kuralın** cevabı, dördüncü şık **mekanizmanın** cevabı; ikisini de doğru say ve ayrımı sözle yap: "Doğru yazılmış döngüde gözcü işlenmez; yanlış yazılmış döngüde işlenir ve 0 için fark etmez ama -1 için eder." Üçüncü şıkkı seçenler tuzağın ta kendisi: "0 için şanslısınız; gözcü -1 olsaydı toplam bir eksik, adet bir fazla." Sonra bot ile tuzaklı istem (4 6 -1 → 9 mu 10 mu). Bu sorunun "fark etmez" yüzdesini lab sorumlu hocasına ilet; Lab 7 Görev 1'in gizli testi (gözcü ilk girdi, adet 0) tam buraya bakıyor.

## for bloğu (karar kuralı tablosu açıldıktan sonra, 33. dk)

**4. ★ Çoktan seçmeli: Kullanıcı kaç sayı gireceğini önceden söylemiyor, "bitti" diyene kadar sayı girecek. Hangi döngü?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme
- for, çünkü sayıları sayacağız
- while, çünkü tekrar sayısı baştan belli değil
- do-while, çünkü en az bir sayı girilecek
- Üçü de olur, fark yok
Not: İkinci şık doğru; "bitti" gözcü değerdir, tekrar sayısı bilinmez. Üçüncü şıkka: "Kullanıcı ilk girdide 'bitti' derse hiç sayı yok; do-while yine bir tur döner ve gözcüyü işler; o yüzden gözcü döngüsünde while." Dördüncü şıkka: "Çevrilebilir, evet; ama 'doğal olan' hangisi? Vize 'bu for'u while ile yaz' diyebilir, ama labda doğru aracı seçmek puan." Birinci şıkka: "Saymak sayaç değil; sayaç döngüyü sürdürmüyor, sadece sayıyor; Tahmin'deki deneme gibi." Bu soru Lab 7'de `Carpim` (for zorunlu) ve `Toplam` (while) ayrımının ölçüsü.

## Kapanış (son 3 dakika)

**5. ★ Açık uçlu: Bugünden aklında kalan tek cümle?**
Tür: Open-Ended (Text Wall) · Anonim
Not: 8. haftanın açılışında bu duvardan 2-3 cümle okuyarak başla. "Bir kez yaz yüz kez çalıştır", "koşulu yanlış yapan satır hangisi", "önce yap sonra sor", "gözcü işlenmez", "bot sorar ajan çalıştırır", "sayaç döngü bitince 11" cümleleri gelirse hikayeler tutmuş demektir. "Ajan her şeyi yapar" gibi yanlış bir cümle gelirse 8. haftanın açılışında adını vermeden "mekanik iş ajana, anlama size" cümlesiyle düzelt.

---

### Kurulum ipuçları

- 2., 3. ve 4. sorularda "Show results" kapalı başlasın; önce oy, sonra gösteri (Playground / terminal), sonra sonuç. 1. soru ısınma, sonuç hemen açık.
- 3. soruda iki doğru şık var (2 ve 4); Poll Everywhere'de yalnızca birini "correct" işaretle (2) ve 4'ü sözle doğru say; sonuçları okurken 2 + 4 toplamını söyle.
- 5. soruda küfür filtresini aç.
- 2., 3. ve 4. soruların sonuçlarını iki şube için ayrı ekran görüntüsü olarak al; 3. sorunun "fark etmez" ve 4. sorunun "do-while" yüzdesini lab sorumlu hocasına ilet, Lab 7'de `Toplam` ve `Carpim` görevlerinde o hataları beklesin.
