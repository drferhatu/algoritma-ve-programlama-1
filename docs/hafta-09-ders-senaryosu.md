# Hafta 9 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 20 Kasım 2026 Cuma · A şubesi 09.15 · B şubesi 13.15.
**Tek oturum, 60 dakikalık "shot" akışı.** Slayt yok; yansıda `/haftalar/hafta-09` açık (Yansı modu: Alt+Y). İkinci ekranda Java Playground sekmeleri ve LeetCode. Poll Everywhere soruları `docs/hafta-09-polleverywhere.md`.
**Slogan:** bugün yeni döngü yok; geçen haftanın döngülerine ad veriyoruz.

## Üslup notu

Bu hafta ton **hikaye anlatıcısı**. Cümleler tam, acele yok, tahtaya az şey yazılıyor. Sınıf sınavdan dört gün önce geliyor ve gergin; ders bilerek hafif ve moral verici. Metotlar sınavda yok, ama metotların içine koyduğumuz döngüler sınavın tam ortasında; bunu ders boyunca iki üç kez, sakin bir sesle söyle: "Bugün yaptığımız şey sınav tekrarının kendisi."

Açılışta ve kapanışta aynı cümle: **"Bugün yeni döngü yok, geçen haftanın döngülerine ad veriyoruz."**

Her kapsül bir "shot": tek fikir, tek kod, bir canlı etkinlik. Ritim:

1. Fikir satırını yüksek sesle oku.
2. **Sınıfta** etkinliğini yap; etkinlik koddan önce gelir.
3. Kodu göster, **tahmin ettir, sonra Run.**
4. Hikayesi olan kapsülde hikayeyi anlat. Bu hafta iki büyük hikaye var (left-pad ve Mars); ikisine de zaman tanı, kısaltma.
5. **Sor** ve **Doğrula** şeritleri bu hafta eve kalıyor; canlı Gemini yok.

**Mülakat kartları:** dört karttan **ikisi derste** işlenir: 4. kapsülün izleme sorusu (2 dakika sessiz, kağıt kalem) ve 6. kapsülün `enBuyuk3` sorusu (sınıf birlikte yazar). Basamak toplamı (3. kapsül) ve LeetCode takip soruları eve. Kart kullanımı geçen haftaki gibi: yansıt, sessiz düşünme, bir gönüllü anlatır, cevabı aç, "mülakatçının duymak istediği cümle"yi oku.

**Uzun kapsüller:** 3, 4 ve 5. Bunlar kısaltılmaz. 1 ve 6 gerekirse kısalır (B planı).

Sabit cümleler: **"Hesap yapan metot sonucunu döndürür, ekrana yazmaz."** ve **"İmza bir sözleşmedir."**

## Hazırlık (derse girmeden)

- Playground'da ayrı sekmelerde hazır (hepsi `Main` sınıfı; **Playground tam sınıfı kendiliğinden çalıştırmaz**, bu yüzden kutunun sağ üstündeki "Playground için kopyala ve aç" düğmesiyle kopyala: düğme sona `Main.main(null);` ekler. Derste bunu bir kez yüksek sesle söyle): "Math: hazır metotlar" (1), "Parametreli çizgi" (2), "asalMi" (3), "Göstermek ve vermek" (4), "Sıra önemlidir" (5), "ekok, ebob'un omuzlarında" (6). Bulmacanın kodu ayrı bir sekmede dursun; Run edildiğinde `97 asal mi: false` yazdığını önceden gör.
- **LeetCode hesabı açık**, [9 · Palindrome Number](https://leetcode.com/problems/palindrome-number/) sekmesi hazır, dil **Java** seçili. Çözümü bir gün önce bir kez gönder ve Accepted yazısını gör. Giriş ekranı sınıfta görünmesin. **Çözüm yedeği panoda** (sayfadaki `isPalindrome` gövdesi); canlı yazarken takılırsan yapıştır.
- İzleme sorusunun kodu (4. kapsül mülakat kartı) yansıda büyük görünsün; cevabı (`icerde 6` / `3 7`) açık kalmasın, kart kapalı başlasın.
- **Kronometre** yansıda gösterilebilir olsun: 2 dk bulmaca, 2 dk izleme.
- Tahtada önceden, sağ üst köşede sabit kutu: `Vize: 24 Kasım Salı 17.00 · kapsam 1-8. hafta · metotlar YOK`. Ders boyunca silinmez.
- Yedek ekran görüntüleri: Math çıktısı (12.0, 1024.0, 12, 5, 2.0000000000000004), fiş çıktısı, `100'e kadar asal sayisi: 25`, `25 / 26 / 81`, `2.5 / 0.4`, `EBOB: 21 / EKOK: 36 / En buyuk: 9`, LeetCode Accepted ekranı.
- İnternet yoksa: `Belgeler/algo1` klasöründe aynı kutuların `Main.java` halleri ayrı alt klasörlerde derlenmiş dursun; terminalden çalıştır.
- 8. haftanın Poll 6b duvarından ("bugün sınıfta olmasaydım neyi kaçırırdım?") en iyi iki cümle açılış için elde olsun.
- İki gönüllü gerektiren rol canlandırması için tahtanın önünde yer aç.
- Salon teyidi geldiyse tahtaya yaz; gelmediyse "duyurudaki tablo geçerli" de.

## Açılış duyuruları (ilk 60 saniye, hikayeden önce)

- "Bugün yeni döngü yok, geçen haftanın döngülerine ad veriyoruz. Metotlar sınavda sorulmayacak; ama bugün içine baktığımız her döngü sınavda."
- **Ara sınav 24 Kasım Salı 17.00-18.00.** A: A304-306; B: A306, A404-406. Kapsam 1-8. hafta.
- **Lab 8 için depo teslimi alınmıyor;** lab saatinde yaptığınız çalışma yeterli. Ayrıntı duyurularda.
- "Kağıt kalem dışarıda olsun; iki kez ikişer dakika sessiz çalışacağız."

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Öğrenci ne yapar | Tahtaya yazılacak | Hikaye (süre) |
|---|---|---|---|---|---|
| 0-5 | Hikaye: on bir satır | Duyurular (60 sn). Sonra otur, sesini alçalt ve anlat: 22 Mart 2016 sabahı, derlenmeyen projeler, hata mesajındaki tanınmayan ad. Azer Koçulu: Türkiye'de doğup büyümüş bir yazılımcı; paket adı yüzünden bir şirketle anlaşmazlık; 273 paketini bir gecede geri çekmesi. `left-pad` ne yapıyordu: metnin soluna boşluk ekler. "Tamamı on bir satırdı." Zincir: kimse doğrudan kullanmıyordu, ama kullandıkları araç başka aracı, o da onu çağırıyordu. **Poll 1.** Bitiriş sorusu: "O on bir satırı siz yazabilir miydiniz?" Cevap verme; "dersin sonunda birlikte bakacağız." | Dinler; Poll 1; soruyu aklında tutar | `22 Mart 2016` · `left-pad: 11 satır` · `METOT = adı olan küçük iş` | left-pad (4 dk; kısaltma) |
| 5-8 | Bulmaca: üç kere aynı sekiz satır | Kodu yansıt: "arkadaşınız asal testini üç sayı için kopyalayıp yapıştırmış." **Kronometre 2 dk, sessiz:** "üç satır yazıyor, biri yanlış; hangisi, neden?" Sonra Run: `97 asal mi: false`. Bir öğrenciye satırı göstert: `n2 % i`. "Derleyici neden görmedi?" "Yüz sayı olsaydı kaç yerde saklanabilirdi?" Çözüm: daha dikkatli kopyalamak değil, **hiç kopyalamamak.** | Hatayı arar; satırı gösterir | `kopyala-yapıştır hatası` · `1 kez YAZ, 3 kez ÇAĞIR` | Yok |
| 8-13 | Kapsül 1 · Zaten kullanıyordunuz (kısalabilir) | "144'ün karekökünü bulan döngüyü şu an yazabilir misiniz?" 30 saniye sustur. Sonra tek satır: `Math.sqrt(144)`. "Bu satırın arkasındaki kodu kim, ne zaman yazdı?" `println`, `nextInt`, `Math.random`: dokuz haftadır çağırıyorsunuz. Kutu: her satırı tahmin ettir, Run. Son satır `2.0000000000000004`: "3. haftadan hatırlayan?" "Yerine geçme" fikrini söyle: dönen değer çağrının yerine geçer. | Tahmin eder; 3. haftayı hatırlar | `ad ( ne veriyorum ) → ne alıyorum` · `Math.sqrt(144) → 12.0` | Karekökü kim yazdı: Sun, 1990'ların başı; "bir kez doğru yazılır, herkes unutabilir" (40 sn) |
| 13-20 | Kapsül 2 · İlk metodunuz: çizgi | Tahtaya dört satırlık `cizgi()` tanımını yaz; parça parça oku: ad, boş parantez, gövde, `void`, `static` ("şimdilik kalıp"). "Bu dört satır tarif defterinde bekler." **Poll 2** (tanım var, çağrı yok). **Rol canlandırması:** bir gönüllü `main`, bir gönüllü `cizgi`. Main programı yüksek sesle okur ("Basla yaz"), `cizgi()` satırında susar ve arkadaşına döner; arkadaşı "yirmi tire" der; main kaldığı yerden devam eder ("Bitti yaz"). Diyagramdaki numaraları göster. Sonra main "cizgi, beş" der: "ne değişti?" → parametre. "Parametreli çizgi" kutusu: Run; `cizgi(30)` ekle; tireyi yıldıza çevir: "tek yerde değişiklik, üç yerde sonuç." Parametre/argüman tanımını tek cümleyle söyle. | İki gönüllü rol yapar; Poll 2; çıktıyı tahmin eder | `TANIM ≠ ÇAĞRI` · `main → git → geri dön` · `parametre = boş kutu · argüman = kutuya konan` | Yok |
| 20-28 | Kapsül 3 ★ UZUN · return ve asalMi | "cizgi bir iş yapıyordu; şimdi bir soruyu cevaplayan metot." Bulmacanın üç kopyasını yansıt, sonra `asalMi` kutusuna geç: "yirmi dört satır tek çağrıya indi." `void` yerine `boolean`. Üç `return`'ü parmakla göster: n = 1, n = 91, n = 97 için hangisi çalışır? "return çalışınca döngünün kalanına ne olur?" → "break'e de bayrağa da gerek kalmadı." **Tahmin toplama:** "1 ile 100 arasında kaç asal var?" En düşük ve en yüksek tahmini tahtaya yaz. Run: **25.** `if (asalMi(i))` satırını yüksek sesle okut: "eğer i asalsa." Sınav bağlantısı: "bu gövde sınav kapsamında; 91 için iz tablosunu bu akşam çıkarın." Basamak toplamı kartı evde. | Hangi return'ün çalıştığını söyler; tahmin verir | `boolean asalMi(int n)` · `return = bitir + geri ver` · `1-100: 25 asal` | Yok |
| 28-36 | Kapsül 4 ★★ UZUN · return ile println | Otomat benzetmesi: camın arkasında gösteren ve hazneye düşüren. "Göstermek ve vermek" kutusu: tahmin, Run: `25`, `26`, `81`. `kareAl(kareAl(3))`'ü içten dışa oku. Sonra **mülakat kartı (izleme sorusu)**: kodu yansıt, **kronometre 2 dk, sessiz, kağıt kalem, telefon kapalı.** Yan sıra karşılaştırma 30 sn. **Poll 3.** Cevabı aç: `icerde 6` ve `3 7`. İki soru: "metot neyi yazdırdı, neyi döndürdü?" ve "a neden hâlâ 3?" → kopya. "Adı pass by value; ayrıntısı haftaya." Kuralı tahtaya yaz. | Kağıtta izler; karşılaştırır; Poll 3 | `println = GÖSTER · return = VER` · `icerde 6` / `3 7` · `HESAP YAPAN METOT DÖNDÜRÜR, YAZMAZ` | Yok |
| 36-44 | Kapsül 5 ★★ UZUN · İmza bir sözleşmedir | Tahtaya tek satır yaz: `static double itki(double sure)`. "Bu metot sonucu hangi birimde veriyor?" Bekle; kimse bilemez. "Çünkü yazmıyor." "Sıra önemlidir" kutusu: `bolum(10, 4)` ve `bolum(4, 10)`; **Poll 4**; Run: `2.5` ve `0.4`. `bolum(10)` yaz, derleme hatasını okut: "derleyici sözleşmenin hangi maddesini denetliyor, hangisini denetleyemiyor?" Sonra hikaye. Kapanış sorusu: "Bu satırı nasıl yazsaydınız kaza olmazdı?" → `itkiNewton`, ya da bir yorum satırı. | Birim sorusunda susar; Poll 4; ad önerir | `static double itki(double sure)` → `? birim` · `İMZA = SÖZLEŞME` · `1 pound ≈ 4,45 newton` · `itkiNewton` | Mars Climate Orbiter: 125 milyon dolarlık uydu; yüklenici pound döndürdü, NASA newton okudu; her düzeltme 4,45 kat küçük; dokuz buçuk ay birikti; 23 Eylül 1999'da atmosferde parçalandı. "İki program da doğru çalışıyordu." (3 dk; kısaltma) |
| 44-50 | Kapsül 6 · Metot metodu çağırır (kısalabilir) | "left-pad'deki zinciri hatırlayın." "ekok'un gövdesi kaç satır olur?" tahmin al; kutuda göster: **tek satır**, içinde döngü yok. `ebob`'u bilerek boz (`return b`), Run: ekok da bozuldu; düzelt. Sonra **mülakat kartı:** "üç sayının en büyüğü; tek kural: **yeni if yazmak yasak.**" 60 saniye; sınıf `enBuyuk(enBuyuk(a, b), c)`'yi bulur. "Dört sayı?" "Gerçek projede?" → `Math.max`. | ekok satırını söyler; enBuyuk3'ü kurar | `ekok = a / ebob(a, b) * b` · `enBuyuk(enBuyuk(a, b), c)` · `KÜÇÜK PARÇA → BÜYÜK İŞ` | Yok |
| 50-55 | Kapsül 7 · Kilit açıldı: LeetCode canlı | "Geçen hafta 'LeetCode sizden metot ister' demiştik; o gün engeldi." LeetCode 9 sekmesi: iskeleti yansıt, **imzayı sınıfa okut** (ad, parametre, dönüş tipi). Gövdeyi sınıfla birlikte yaz: negatifse `return false`; basamak döngüsü; `return x == ters`. **Submit.** Accepted yazısını birlikte görün; kısa bir alkış iyi gelir. "Bu akşam üç soru: 2235, 9, 258." | İmzayı okur; gövdeyi dikte eder | `isPalindrome(int x) → boolean` · `Accepted` · `2235 · 9 · 258` | Yok |
| 55-60 | Kapanış: on bir satır ve sınav | `solaDoldur` kodunu yansıt. "Dersin başındaki soru: yazabilir miydiniz?" Satır satır okut: imza, `while`, `return`. "**Bunu okuyabiliyorsunuz.** 2016'nın o sabahında dünyayı durduran kod bu." `length()`: "bir başka metot çağrısı; 14. hafta." **Poll 5.** Sonra kapanış duyuruları. Son cümle: "Bugün yeni döngü yazmadınız; geçen haftanın döngülerine ad verdiniz. Salı günü o döngüleri kağıtta izleyeceksiniz. Hazırsınız." | Kodu okur; Poll 5 | `solaDoldur("42", 6) → "    42"` · `imza + while + return` | left-pad kapanışı (60 sn) |

## Kapanış duyuruları (son 90 saniye)

- **Ara sınav 24 Kasım Salı 17.00-18.00.** A: A304-306; B: A306, A404-406. Kağıt üzerinde, telefon kapalı; kimlik ve kalem yeter. Kapsam 1-8. hafta, **metotlar yok.**
- **Vize planının son dört günü** (`/vize-plani`): Cumartesi kendi deneme kağıdını asistana yazdır ve 60 dakikada çöz; Pazar yanlışlara dön ve KT1'deki seçim yapını kağıda bakmadan yaz; Pazartesi yalnızca cep kartı ve erken uyku.
- "Bu akşam dört iz tablosu, yarım saat: asal testi 91 ile, Euclid 252 ve 105 ile, basamak toplamı 4725 ile, palindrom 1200 ile."
- **Lab 8 için depo teslimi alınmıyor.**
- **Lab 9:** A 25 Kasım Çarşamba 13.15, B 26 Kasım Perşembe 15.15. Hafif lab; **hiçbir yere dosya yüklenmiyor.** Sayfadaki iskelet kendi kendini sınıyor, lab sorumlu hocanız sonucu ekranda görüp bir metodu anlattırıyor.
- **KT2 27 Kasım Cuma 23.59**; şartlar aynı (menü döngüsü ve girdi doğrulama), metot şart değil. Göndermeden önce kendi bilgisayarınızda `javac Uygulama.java` ve `0` ile deneyin.

## B planı

- **Zaman biterse:** önce 1. kapsül kısalır (yalnızca `Math.sqrt(144)` ve "kim yazdı?" sorusu, 2 dakika); sonra 6. kapsülde yalnızca `ekok` gösterilir, `enBuyuk3` kartı eve kalır. Hâlâ sıkışıksa LeetCode'da gövdeyi sınıfla yazmak yerine panodaki çözümü yapıştır ve doğrudan Submit'e bas. **3, 4 ve 5 kısaltılmaz;** left-pad ve Mars hikayeleri de.
- **Zaman artarsa (B şubesinde olabilir):** 3. kapsülde ikiz asalları `main`'e iki satırla ekle (çıktı: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43, 59-61, 71-73); basamak toplamı kartını 60 saniyelik sessizlikle yap.
- **İnternet yoksa:** Playground yerine yerel terminal; Poll yerine el kaldırma (şıkları tahtaya yaz); LeetCode yerine Accepted ekran görüntüsü, gövdeyi tahtada sınıfla yaz.
- **Gönüllü çıkmazsa:** rol canlandırmasında `main` sen ol, `cizgi`'yi ön sıradan bir öğrenci oturduğu yerden oynasın.
- **Sınıf çok gerginse:** 3. kapsülün sonunda bir dakika dur ve sınav sorularını al; cevabı kısa tut, ayrıntıyı kapanışa bırak.

## Ders sonrası

- Poll sonuçlarını iki şube için ayrı kaydet: Poll 2'de "bir çizgi" yüzdesi, Poll 3'te "6 7" yüzdesi, Poll 4'te "2.5" yüzdesi, Poll 5a'nın en bulanık iki kapsülü ve 5b duvarından sınav ihtiyaçları.
- **Poll 5b'yi aynı gün oku:** "Salı günkü sınav için en çok neye ihtiyacın var?" cevaplarından en sık geçen iki ihtiyaca göre hafta sonu WhatsApp kanalından kısa bir vize planı mesajı yaz (hangi güne, hangi bloğa baksınlar).
- **Ömer'e Lab 9 notu:**
  - İskelet lab sayfasında (`/laboratuvar/lab-09`); öğrenci Playground için kutunun sağ üstündeki düğmeyle kopyalar (sona `Main.main(null);` eklenir) ya da `Main.java` olarak kaydedip `javac Main.java` ve `java Main` ile çalıştırır. Playground kodu saklamaz; öğrenciye ara sıra bir not dosyasına kopyalamasını söyle. Depo, hesap, yükleme yok.
  - İskelet hiç değiştirilmeden `Sonuc: 4/20` yazar; bu beklenen bir şey ve sayfada açıklaması var.
  - Kontrol eşiği **18/20** (bonus hariç tam). Görev 1-3'ü bitirip bir metodu anlatan öğrenci labı tamamlamış sayılır.
  - Dört kontrol sorusundan birini sor, cevap 30 saniyeyi geçmesin: imzayı oku; bu `return` çalışınca döngüye ne olur; metot ekrana yazıyor mu, yazsaydı kontrol bölümü neden çalışmazdı; `ekok`'un içinde neden döngü yok.
  - Yoklama listesine **sonuç (kaç/20) ve anlatım (oldu/olmadı)** işlenecek; labın tek kaydı bu. LabYoklama PDF'leri `Algo-I/YOKLAMA` klasöründe.
  - Beklenen hatalar: `fizzBuzz`'da sayıyı metne çevirmemek (`"" + i`), metodun içine `println` koymak, `ekok`'u `ebob` bitmeden denemek (ekranda "BEKLIYOR" yazar), `palindromMu`'da parametreyi tüketip asıl sayıyı kaybetmek.
  - Lab sınavın ertesi günü; sınıf yorgun olacak, tempo düşük tutulsun.
- 4. kapsülün sessiz izlemesinde dolaşırken gördüğün en yaygın yanlış cevabı yaz (`6 7` bekleniyor); 10. haftanın pass by value açılışında kullan.
- Salon teyidi geldiyse duyuruyu ve `/vize-plani` sayfasını güncelle.
