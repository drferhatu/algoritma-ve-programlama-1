# Hafta 1 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 25 Eylül 2026 Cuma · A şubesi 09.15 (fiilen 09.30 başla, 10.30-10.45 arası bitir) · B şubesi 13.15 (fiilen 13.30 başla, aynı akış, 14.30-14.45 bitir).
**Tek oturum, yaklaşık 75 dakika.** Slayt yok; yansıda `/haftalar/hafta-01` açık. İkinci ekranda Java Playground sekmesi hazır. Poll Everywhere soruları `docs/hafta-01-polleverywhere.md`.

## Hazırlık (derse girmeden)

- Yansı: site sayfası + Playground sekmesi + ChatGPT sekmesi (nehir bulmacası istemi hazır yazılı, Enter'a basılmamış).
- Yedek: nehir bulmacasının AI çözümü önceden alınmış, PDF olarak masaüstünde (internet giderse).
- Kağıt: her sıraya A5 kağıt (bulmaca için); tahta kalemi iki renk.
- Gönüllü "insan bilgisayar" için tahtada yer.
- Poll Everywhere "Hafta 1" grubu etkin.

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Öğrenci ne yapar | Tahtaya yazılacak |
|---|---|---|---|---|
| 0-8 | Açılış ve anket | Kendini ve asistanı tanıt (1 dk). Poll 1 kelime bulutu "algoritma", Poll 2 programlama deneyimi. Bulut büyürken yorumla. | PollEv'e telefondan girer | Sol üst köşe: `Ders sitesi: <adres>` · `Playground: dev.java/playground` |
| 8-25 | Nehir bulmacası | Bulmacayı oku (site yansıda). "İkili çalışın, 8 dakika, numaralı liste yazın." 8 dk sonra bir çift çözümü okur; tahtaya adımları yaz. Sonra dört soru: neyi bilmemiz gerek, ne yapabiliriz, ne yasak, ne zaman durduk. | Kağıtta çözer; dört soruyu yazar | Tahta ortası: 7 adım listesi. Sağda dört kelime: **DURUM · HAMLE · KISIT · HEDEF** (bunlar dönem boyunca kalacak; fotoğrafını çek) |
| 25-38 | İnsan bilgisayar | Gönüllü tahtaya. "O artık bilgisayar; yalnızca yazılanı yapar." Sınıf "en uzunu bul" der; gönüllü "anlamadım" der (önceden anlaşın). Sınıfı adım adım tarife zorla. | Komut önerir; 4 adımlık tarif çıkar | `aklında tut` = değişken · `büyükse değiştir` = if · `kişi kalmadıysa dur` = döngü |
| 38-60 | Playground: dört program | "Telefonu çıkarın, Playground'u açın." Her programda: **önce tahmin** (el kaldırt), sonra Run. Program 2'de `7 / 2` için Poll 4. Program 1'de bilerek noktalı virgülü sil, hata mesajını yansıda oku. | Her kodu kendi telefonunda çalıştırır; ismi değiştirir; noktalı virgülü siler | `int` tam sayı · `double` ondalık · `7 / 2 = 3` (büyük yaz) · `; unutma` |
| 60-70 | Yapay zeka anı | ChatGPT'ye istemi gönder. Kodu yansıya al; "yazmıyoruz, okuyoruz." `if`, `while`/`for`, dizi satırlarını göster; kağıttaki adımları kodda buldur. Trafik ışığını üç cümleyle söyle. | Kodda kısıt satırlarını bulur | `KIRMIZI sınav · SARI lab · YEŞİL portfolyo` |
| 70-75 | Kapanış | Poll 6 ("YZ programcılığı bitirecek mi?") ve Poll 7 ("aklında kalan tek cümle"). Lab hatırlatması: 30 Eylül / 1 Ekim, GitHub hesabıyla gelin. "Kağıdı saklayın; 13. haftada bu bulmacayı kodlayacaksınız." | Anket; kağıdı saklar | `Lab: 30 Eyl (A) · 1 Ekim (B) · GitHub hesabı` |

## Kilit cümleler (blok blok)

**Açılış.** "Bu derste slayt yok. Bu sayfa yansıda, aynı sayfa sizin telefonunuzda. Her hafta aynı düzen: bulmaca, notlar, kod, yapay zeka anı." · "Kodu ilk gün yazacağız; ama sığ taraftan giriyoruz."

**Nehir.** "Çözümü bilmek ile çözümü yazabilmek ayrı şeyler. Bilgisayar yalnızca ikinciyi anlar." · "Kağıda yazdığınız şeyin adı algoritma. Bugün elle çözdük; 13. haftada Java'da yazacaksınız. Kağıdı saklayın." · Dört kelimeyi yazarken: "Dönem boyunca yazacağınız her programın iskeleti bu dört kelime."

**İnsan bilgisayar.** "Bilgisayar 'en uzun' ne demek bilmez. 'Büyükse değiştir' bilir. Komutlar bu kadar küçük olmalı." · "'Aklında tut' dediğiniz şeye şimdi bir kutu diyeceğiz: değişken."

**Playground.** "Çalıştırmadan önce çıktıyı söyleyin. Yanlış tahmin, doğru tahminden değerli; öğrenme o anda oluyor." · Noktalı virgülü silince: "Korkutucu görünüyor ama iki şey söylüyor: hangi satır, ne bekliyor. Bu kadar." · `7 / 2` için: "Bu bir hata değil, bir kural. Bu kuralı bilmeyen birinin yazdığı not programında ne olur?" · Program 4: "Babil'in 'ikinci adıma dön' cümlesi işte bu satır."

**Yapay zeka anı.** "Bu programı okuyoruz, yazmıyoruz. Anlamadığınız her satır, önümüzdeki 13 haftada öğreneceğiniz bir konu." · "Trafik ışığı: sınavda yok çünkü ölçtüğüm şey sizin zihniniz; lab'da sor ama kopyalama çünkü ustalaşma takılıp çözmekle olur; portfolyoda serbest ama beyan yaz çünkü anlatamadığın kod senin değil." · "Ben de şeffafım: bu sayfayı hazırlarken yapay zeka kullandım; notunuzu verirken kullanmayacağım."

**Kapanış.** "Vizede 10, finalde 15 puan doğrudan sizin uygulamanızdan gelecek. Teslim etmeyen o soruyu yapamaz." · "Gelecek hafta: akış diyagramı, `class` ve `main` töreni, üç hata türü."

## Olası aksaklıklar ve B planı

| Sorun | B planı |
|---|---|
| **İnternet yok / Playground açılmıyor** | Dört programı tahtaya yaz; sınıf **kağıt üzerinde izler** (her satır için "ekrana ne çıkar?" sorusu, el kaldırt). `7 / 2` tartışması tahtada daha da iyi işler. AI anı için masaüstündeki PDF çözümü yansıt. |
| Telefonların bir kısmında `{` `;` klavyede bulunamıyor | "Kodu sayfadan kopyalayın, yalnızca sayıları ve ismi değiştirin." Yan yana oturanlar tek telefon paylaşsın. |
| Nehir bulmacasını çoğu biliyor, 3 dakikada bitiyor | Dört soruya geç; ek soru: "En az kaç geçiş gerekir, kanıtlayabilir misiniz?" ve "Bir de kurt eklense?" |
| Gönüllü çıkmıyor | Asistanı bilgisayar yap; ya da hoca bilgisayar olur, sınıf komut verir (daha eğlenceli). |
| Poll Everywhere çalışmıyor | El kaldırma ile aynı sorular; kelime bulutu yerine 5 kişiden tek kelime al, tahtaya yaz. |
| Süre taşıyor | Kesilecek sıra: Sahadan örnekler (siteye bırak) → Program 4'ün varyasyonları → İnsan bilgisayar kısaltılır (tarif tahtada hazır verilir, yalnızca izlenir). Nehir bulmacası ve Playground **kesilmez**. |
| B şubesi öğle sonrası, enerji düşük | Nehir bulmacasına 2 dk fazla ver, insan bilgisayarı kısa tut, Playground'a erken geç. |

## B şubesi (13.15)

Aynı akış, aynı dakikalar (13.30 başla, 14.30-14.45 bitir). A şubesinden not: hangi programda tahmin en çok şaştı, hangi sorunun cevabı sürpriz oldu; B'de o noktaya iki cümle fazla ayır. Poll sonuçlarının ekran görüntüsünü her iki şube için ayrı al (14. haftada tekrar sorulacak).

## Ders sonrası (5 dk)

- Tahtanın fotoğrafı (dört kelime) → 2. hafta sayfasına "geçen haftadan" görseli.
- Poll 7'den 2-3 cümle → 2. haftanın açılışında oku.
- Playground'da en çok takılan yer → `content/guides/java-playground.md` sınırlar bölümüne ekle.
