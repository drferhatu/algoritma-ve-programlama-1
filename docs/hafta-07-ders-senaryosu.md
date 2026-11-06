# Hafta 7 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 6 Kasım 2026 Cuma · A şubesi 09.15 (fiilen 09.30-10.40) · B şubesi 13.15 (fiilen 13.30-14.40).
**Tek oturum, 70 dakika fiilî.** Slayt yok; yansıda `/haftalar/hafta-07` açık (Yansı modu: Alt+Y). İkinci ekranda Java Playground sekmesi ve **Gemini masaüstü uygulaması** (sohbet + görev modu, `Belgeler/algo1` yetkili). Poll Everywhere soruları `docs/hafta-07-polleverywhere.md`.
**Slogan:** bir kez yaz, yüz kez çalıştır; koşulu yanlış yapan satır hangisi?

## Üslup notu

Sayfa 12 kapsülden oluşuyor ve ders de öyle işlenecek. **Kapsül = tek fikir + tek kod + bir deneme + bir soru.** Her kapsülde aynı ritim:

1. Kapsülün "fikir" satırını yüksek sesle oku (tek cümle, tahtaya kısaltılmışı).
2. Kodu göster, **tahmin ettir, sonra Run** (Playground'da ya da terminalde).
3. **Sor** şeridindeki istemi canlı bir kez Gemini'ye gönder; cevap gelirken sınıfa "neyi kontrol edeceğiz?" diye sor.
4. **Doğrula** şeridiyle cevabı sınıfla sına: bot haklı mı, kod haklı mı? Haklı olan her zaman koddur.

Hiçbir kapsül 3 dakikayı geçmesin; ayrıntı sayfada, evde okurlar. Canlı Gemini gösterisi her kapsülde değil, yıldızlı olanlarda (2, 5, 6, 7, 8, 11); diğerlerinde "Sor şeridi evde" de ve geç. Sabit cümle, her seferinde aynı: **bot sorar ve cevaplar; ajan klasörde dosya açar, çalıştırır, sonucu getirir.** Sonsuz döngü kodlarını (3. ve 10. kapsül) **asla** Playground'da çalıştırma; tahtada izlet. Motivasyon tonu: "bugünden sonra yazabileceğiniz program sayısı birkaç yüz kat artıyor"; oyun, menü, sayaç, hepsi bugünkü üç yapıdan.

## Hazırlık (derse girmeden)

- Playground'da ayrı sekmelerde hazır: "1'den 10'a toplam" (2), "Hiç mi, en az bir mi?" (4), "Çarpım tablosu ve geri sayım" (6), "Kaç kapı?" (9), "On kere 0.1" (10), "Sayaç nerede yaşar?" (11).
- `Belgeler/algo1` klasöründe derlenmiş halde: `NotAl.java` (5), `Kasa.java` (7), `Tahmin.java` (8, hedef 42). Terminal açık; `9 0 4`, `5 7 3 0`, `50 40 42` girdileri elle verilecek.
- Gemini görev modu bir gün önce provalı: klasör yetkilendirme diyaloğu nerede, `javac`/`java` çalıştırma ve stdin girdi verme bu sürümde nasıl. 8. kapsülün ajan istemi sayfadan kopyalanıp gönderilecek; çıktının ekran görüntüsü alınmış olsun (B planı).
- Yedek ekran görüntüleri: 2. kapsül tur tablosu (son satır i = 11), 7. kapsül tuzak cevabı (9 mu 10 mu), 8. kapsül ajan tablosu (3, 1, 5), 11. kapsül doğrulama anı cevabı, KT1 kontrol raporu.
- Portfolyo örnek deposu klonu `Belgeler/algo1-portfolyo-ornek` adıyla, bilerek bir eksikle (AI-BEYANI'nda KT1 bölümü boş); kapanıştaki KT1 kontrol istemi için.
- Mektup ödevi 5 Kasım'da bitti. Açılışta tek cümle: **"Gelen mektupları aldım, hiçbirini açmadım, 25 Aralık'ta size geri geliyor."** Göndermeyenlere süre uzatması yok, ama "hâlâ yazmak isteyen gönderebilir, yine açılmadan bekler" de.
- **KT1 bu gece 23.59.** Açılışta ve kapanışta söyle. Lab 7 11-12 Kasım, son teslim 13 Kasım. Vize 9. hafta (16-20 Kasım), kapsam 1-8. hafta; `/vize-plani` bugün 8. gün.
- El kaldırt: "portfolyo deposunu açan?" Düşükse kapanışta kabul bağlantısını yansıt.

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Tahtaya yazılacak |
|---|---|---|---|
| 0-5 | Bulmaca: yüz kere | Mektup cümlesi, "KT1 bu gece 23.59." Gönüllü tahtaya: "yüz kez Merhaba." Sınıf yüz kez söylemeye başlasın, onuncuda kes: "en fazla dört cümle." Tarif bulununca dört cümleyi numarala. Zor soru: "kaç kez olduğunu bilmiyorsak?" → "dur diyene kadar"; "sayaç gerekli mi?" Hayır. "Bugün bu iki fikri öğreniyoruz." | `1 sayaç = 0` · `2 sayaç < 100 ise yaz` · `3 sayaç + 1` · `4 → 2` · `"dur" = GÖZCÜ` |
| 5-9 | Kapsül 1 · Dört parça | Fikir satırı: "bilgisayar sizden iyi hesap yapmaz, yorulmaz." Diyagramı göster, dört cümleyle eşleştir; "Lab 2'deki geri sayım oku buydu." Sor şeridi evde. "Bugünden sonra oyun, menü, sayaç: hepsi bu dört parça." | `BAŞLANGIÇ · KOŞUL · GÖVDE · ADIM` · `bir kez yaz, yüz kez çalıştır` |
| 9-14 | Kapsül 2 ★ · while | Dört satırlık Merhaba'yı tahtada satır satır izle (0, 1, …, 99, 100 → hayır). **Poll 1** burada. Canlı: "1'den 10'a toplam" tahmin → Run; "i = 11!" **Sor:** tur tablosu istemini gönder; gelince son satıra bak. **Doğrula:** 11 mi? Playground'daki ikinci println kanıt. | `while (koşul) { … adım; }` · `i döngü bitince = 11` · `bot: sorar-cevaplar` |
| 14-17 | Kapsül 3 · Sonsuz döngü | `i++` satırını sil, Run'a BASMA; kağıtta izlet. Üç sebep: adım yok, ters yön, koşul bozulamaz. Kilit soru tahtaya. Uyarı kutusu: kasıtlı sonsuz (sensör) sahada. Sor şeridi evde. | `KOŞULU YANLIŞ YAPAN SATIR HANGİSİ?` · `adım yok / ters yön / koşul bozulamaz` |
| 17-22 | Kapsül 4 · do-while | Otomat: önce para, sonra soru. Sözdizimi; noktalı virgül daire içinde. Diyagram. **Poll 2** (para = 50, kaç kez). Canlı: "Hiç mi, en az bir mi?" tahmin → Run; while 0 satır, do-while 1 satır. Sor şeridi evde ("en az bir kez" cümlesi Oracle sayfasında). | `do { … } while (koşul);` ← `;` · `ÖNCE YAP, SONRA SOR` · `en az 1 kez` |
| 22-27 | Kapsül 5 ★ · Girdi doğrulama | `NotAl.java` satır satır; terminalde `9 0 4`. Kilit: "bu on satır portfolyo sözleşmesi, KT2'de sizin konunuzda." Tanım kutusu. **Sor:** test girdisi istemini gönder ("çıktıyı söyleme"). **Doğrula:** beş diziden sınır olanı sınıf hesaplar; bot "5 geçersiz" derse kod haklı. | `KT2: girdi doğrulama döngüsü` · `tam 1 ve tam 5 geçerli` |
| 27-32 | Kapsül 6 ★ · for | "Üç parça üç satırda dağınık; adım unutuluyor." `for (başlangıç; koşul; adım)` tahtada, while'ın üstüne oklarla. Canlı: "Çarpım tablosu ve geri sayım" tahmin → Run; "i-- yerine i++?" kağıtta. Karar tablosu; **Poll 4** burada. **Sor:** üç sürüme çevirme istemi. **Doğrula:** N = 0 tuzağı: do-while 1 ekler; bot "aynı" dediyse yanıldı. | `for (int i = 1; i <= 10; i++)` · `belli → for · bilinmiyor → while · en az 1 → do-while` |
| 32-37 | Kapsül 7 ★ · Gözcü değer | Kasiyer: "kaç ürün?" diye sormaz, "toplam" tuşu. Gözcü seçme kuralı. `Kasa.java` satır satır: ilk okuma önce, sonraki gövdenin sonunda; terminalde `5 7 3 0`. **Poll 3** (0 toplanır mı). **Sor:** tuzaklı do-while istemi (`4 6 -1`). **Doğrula:** doğru cevap 9, çünkü gözcü toplanıyor; bot 10 derse görmedi. "KT2: menü gözcüsü 0." | `GÖZCÜ = "toplam" tuşu` · `önce oku → sor → işle + sonrakini oku` · `GÖZCÜ İŞLENMEZ` · `4 6 -1 → 9` |
| 37-45 | Kapsül 8 ★ · Tahmin oyunu + AJAN (8 dk) | `Tahmin.java`: dört parçayı sınıf bulsun (başlangıç -1, koşul != HEDEF, adım = yeni tahmin okumak; deneme sayar ama sürdürmez). Terminalde `50 40 42`. "Üç girdiyle çalıştırıp tabloya yazsın istiyorum. Bot yapabilir mi?" Hayır. Görev modu: klasör yetkili, istemi sayfadan kopyala, gönder. İzin diyaloglarını **yüksek sesle oku** ve onayla. Tablo gelince: 3, 1, 5 mi? "Hangi komutları çalıştırdın" satırını oku. Ajan "iyileştireyim mi?" derse HAYIR. Neden kutusu: mekanik iş ajana, anlama size. | `BOT: sorar-cevaplar · AJAN: klasörde açar, çalıştırır, getirir` · `mekanik iş → ajan · anlama → siz` · `izin = okuyarak` |
| 45-49 | Kapsül 9 · Kapı hikayesi | On kapı, `<` dokuz, `<=` on. Canlı: "Kaç kapı?" Run, saydır; i = 0'dan başlat, bir daha say. Kural: "0'dan < ile, 1'den <= ile." Sor şeridi (sorgu istemi) evde. | `0'dan < · 1'den <=` · `sayacı döngüden sonra yazdır` |
| 49-53 | Kapsül 10 · İki tuzak | `while (i < 3);` tahtada, Run YOK: gövde noktalı virgül, sonsuz. Canlı: "On kere 0.1" tahmin → Run, false. "Sayaç her zaman int." Sor şeridi evde. | `while (…);` ← SONSUZ · `double sayaç YOK` |
| 53-57 | Kapsül 11 ★ · Doğrulama anı | Canlı: "Sayaç nerede yaşar?" Run, derleme hatasını oku. **Sor:** iki iddialı istemi gönder. **Doğrula:** 1 doğru, 2 yanlış; ikisine "doğru" diyen araç o gün iyi gününde değil. "Derleyici onaylamadığını araç onaylayabilir; AI-BEYANI 4. satır." | `for'un i'si döngü bitince ölür` · `doğru + yanlış iddia aynı soruda` |
| 57-60 | Kapsül 12 · Menü döngüsü | 5. haftanın switch'i do-while içinde, gözcü 0. Kodu hızlı oku: do → switch → while (secim != 0). "KT2'nin iskeleti bu; KT1'de şart değil." Sor/Doğrula şeridi evde (1, 7, 5, 0 sırası; case 0 break silinirse). Sahada kutusu tek cümle. | `do { menü; switch } while (secim != 0);` · `KT2: menü döngüsü + doğrulama` |
| 60-64 | Hata avı (4 dk) | Puzzle'ı aç, 3 dk süre: üç hata, satır ve tür. Cevabı details'tan aç: noktalı virgül (derleyici), i++ yok (sonsuz), gözcü toplanıyor (9 yerine 10). "Üç hata, bugünün üç kuralı." | `; · i++ · gözcü` |
| 64-68 | KT1 kapanış (4 dk) | Kontrol listesi kutusunu oku. Ajan istemini örnek portfolyo klonunda canlı çalıştır: rapor "AI-BEYANI KT1 boş" demeli. "Kontrol ajanın, içerik sizin; README'deki kural cümlesini vizede kağıda siz yazacaksınız." Trafik ışığı: Lab 7 sarı, Sor şeritleri serbest, görev yaptırmak yasak. **Poll 5** (bulanık kapsül) ve **Poll 6** (tek cümle). | `KT1 BU GECE 23.59` · `Lab 7: 11-12 Kasım, teslim 13 Kasım` · `vize 9. hafta` |
| 68-70 | Kapanış | Poll 5'te en çok işaretlenen iki kapsülü söyle: "o kapsülün Dene şeridi bu akşam ilk işiniz." Özet üç cümle: bir kez yaz yüz kez çalıştır; koşulu yanlış yapan satır; gözcü işlenmez. "Haftaya döngüler II: iç içe döngü ve break." | `bir kez yaz, yüz kez çalıştır` |

## Ders sonrası

- Poll 3'ün "fark etmez" yüzdesini, Poll 4'ün "do-while" yüzdesini ve Poll 5'in en bulanık iki kapsülünü lab sorumlu hocasına ilet; Lab 7'de `Toplam`, `Carpim` ve ilgili görevlerde o hataları beklesin.
- Poll 6 duvarından 2-3 cümleyi 8. haftanın açılışı için kaydet.
- KT1 gece 23.59'da Classroom 50'de otomatik toplanır; Cumartesi sabahı "Collect now" ile anlık görüntü al ve teslim etmeyenlerin sayısını not et.
- Gemini görev modunda bir şey ters gittiyse (izin diyaloğu, stdin) ne olduğunu yaz; 10. haftadaki ajan gösterisi için düzelt.
