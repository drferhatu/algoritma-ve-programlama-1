# Hafta 6 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 30 Ekim 2026 Cuma · A şubesi 09.15 (fiilen 09.30 başla, 10.40 bitir) · B şubesi 13.15 (fiilen 13.30 başla, 14.40 bitir).
**Tek oturum, 70 dakika fiilî.** Slayt yok; yansıda `/haftalar/hafta-06` açık. İkinci ekranda Java Playground sekmesi ve **Gemini masaüstü uygulaması** (sohbet + görev modu, `Belgeler/algo1` yetkili). Poll Everywhere soruları `docs/hafta-06-polleverywhere.md`.
**Slogan:** bir kez yaz, yüz kez çalıştır; koşulu yanlış yapan satır hangisi?
**Üslup notu:** Geçen hafta ders canlı gösteri ağırlıklıydı; bu hafta normal ders üslubuna dönülüyor: önce kavram ve kod (tahmin → Run), **sonra** "şimdi bunu asistanla şöyle çalışın". Asistan her bölümün sonunda bir dakikalık bir ek, bölümün kendisi değil. İstisna 44-52. dakika: ajan gösterisi orada dersin kendisi. "Bot" ve "ajan" kelimelerini bilerek kullan ve farkı her seferinde aynı cümleyle söyle: **bot sorar ve cevaplar; ajan klasörde dosya açar, çalıştırır, sonucu getirir.** Her bölümün sonundaki "Çalışma rehberi" kutusunu göstermek için 10 saniye yeter: "evde 15 dakika, üç adım: Playground, istem, doğrulama."

## Hazırlık (derse girmeden)

- Playground'da sekmede hazır: "1'den 10'a toplam", "Hiç mi, en az bir mi?", "Çarpım tablosu ve geri sayım", "Kaç kapı?", "On kere 0.1", "Sayaç nerede yaşar?". Sonsuz döngü kutularını **asla** Playground'da çalıştırma; tahtada.
- `Belgeler/algo1` klasöründe `Tahmin.java` derlenmiş halde dursun (dersteki 42 sürümü); `Kasa.java` ve `NotAl.java` da orada; terminal açık, bunları elle çalıştırmak için.
- Portfolyo örnek deposu (`algo1-ornek-kirtasiye`) klonu `Belgeler/algo1-portfolyo-ornek` adıyla ayrı klasörde, bilerek bir eksikle (ör. AI-BEYANI'nda KT1 bölümü boş); KT1 kontrol istemi için.
- Gemini görev modu önceden denenmiş: `javac`/`java` çalıştırma ve stdin girdi verme akışı bu sürümde nasıl, izin diyalogları nerede; bir gün önce prova et ve çıktının ekran görüntüsünü al (B planı).
- Yedek ekran görüntüleri: "kaç kez döner" tablosu, gözcü tuzağı cevabı (9 mu 10 mu), ajan tablosu, KT1 kontrol raporu, doğrulama anı cevabı.
- Geçen haftadan: Poll 5 duvarından 2-3 cümle (açılışta oku); Poll 2'de "break olmadan durur" diyenlerin yüzdesi (Menu2 uyarısında söyle).
- Lab 4 ve Lab 5 son teslim **bu gece 23.59** (Lab 4 kabul sorunu nedeniyle uzatıldı): açılışta ve kapanışta söyle. Lab 6 4-5 Kasım; KT1 6 Kasım; vize 9. hafta (16-20 Kasım), çalışma planı `/vize-plani` (30 Ekim-15 Kasım, bugün 1. gün).
- El kaldırt: "portfolyo deposunu açan?" Düşükse kapanışta kabul bağlantısını yansıt.

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Öğrenci ne yapar | Tahtaya yazılacak |
|---|---|---|---|---|
| 0-6 | Bulmaca: yüz kere | Geçen haftanın duvarından 2 cümle. "Lab 4 ve Lab 5 bu gece 23.59." Gönüllü tahtaya: "yüz kez Merhaba." Sınıf 100 kez söylemeye başlasın, 10'da kes: "dört cümleyle." Sınıf tarifi bulana kadar bekle; bulunca dört cümleyi tahtaya numarala. Zor soru: "kaç kez olduğunu bilmiyorsak?" → "dur diyene kadar"; "sayaç gerekli mi?" Hayır. "İki döngü türü buradan doğdu." | Tarifi bulur; zor soruyu tartışır | `1 sayaç = 0` · `2 sayaç < 100 ise yaz, değilse dur` · `3 sayaç + 1` · `4 → 2` · `"dur" diyene kadar = GÖZCÜ` |
| 6-10 | Neden tekrar | "Bilgisayar sizden iyi hesap yapmaz; tek üstünlüğü yorulmamak." Kasiyer 500. fiş. "Bir kez yaz, yüz kez çalıştır." Diyagram h06-dongu: başlangıç, koşul, gövde, adım; dört cümleyle eşleştir. "Lab 2 geri sayım diyagramındaki ok buydu." Çalışma rehberi kutusunu göster (10 sn). | Diyagramla dört cümleyi eşler | `BAŞLANGIÇ · KOŞUL · GÖVDE · ADIM` · `bir kez yaz, yüz kez çalıştır` |
| 10-20 | while | Sözdizimi: "olduğu sürece"; if'e benzer, farkı başa dönmesi. Dört satırlık Merhaba'yı tahtada satır satır izle (0,1,...,99,100 → hayır). **Canlı:** "1'den 10'a toplam": önce tahmin (toplam ve bitişte i), Run; "i = 11!" Sonra `i++`'ı sil, Run'a BASMA: "ne olur?" → sonsuz; Ctrl+C / sekme kapat. Üç sebep: adım yok, ters yön, koşul bozulamaz. **Kilit soru:** "koşulu yanlış yapan satır hangisi?" Uyarı kutusu: kasıtlı sonsuz (sensör) sonra. **Bot ile (1 dk):** "kaç kez döner" istemini sohbette gönder, tablo gelince son satıra bak: 11 mi? Poll 1 burada (kaç satır). | Tahmin, Run, i = 11'i görür; sonsuz döngüyü kağıtta izler | `while (koşul) { … adım; }` · `i döngü bitince = 11` · `KOŞULU YANLIŞ YAPAN SATIR HANGİSİ?` · `bot: sorar-cevaplar` |
| 20-28 | do-while ve doğrulama | Otomat: önce para, sonra soru. Sözdizimi; **noktalı virgül** tahtada daire içinde. Diyagram h06-while-dowhile. **Canlı:** "Hiç mi, en az bir mi?" para = 50: tahmin, Run; while 0 satır, do-while 1 satır. Poll 2 (en az kaç kez). `NotAl.java` tam dosya: satır satır; `9 0 4` terminalde çalıştır. **Kilit:** "Bu on satır portfolyo sözleşmesindeki girdi doğrulama döngüsü; KT2'de sizin konunuzda." Tanım kutusu. **Bot ile (1 dk):** test girdisi istemi, "çıktıyı söyleme"; beş diziden sınır olanı sınıf hesaplar. | Tahmin, Run; NotAl çıktısını izler; sınır girdiyi hesaplar | `do { … } while (koşul);` ← `;` · `ÖNCE YAP, SONRA SOR` · `en az 1 kez` · `KT2: girdi doğrulama döngüsü` |
| 28-36 | for | "Üç parça üç ayrı satırda; adım unutuluyor." `for (başlangıç; koşul; adım)` tahtada, while'ın üstüne oklarla. **Canlı:** "Çarpım tablosu ve geri sayım": tahmin, Run; "i-- → i++ yaparsam?" kağıtta. "1'den N'e toplam, for ile": N = 10, 100, 0. Karar kuralı tablosu: belli sayı for, bilinmiyor while, en az bir kez do-while. Poll 4 (for mu while mi) burada. **Bot ile (1 dk):** "üç sürüme çevir" istemi; N = 0 tuzağını sınıf cevaplar: do-while 1 ekler. | Tahmin, Run; karar kuralını üç örneğe uygular | `for (int i = 1; i <= 10; i++)` · `belli → for · bilinmiyor → while · en az 1 → do-while` |
| 36-44 | Gözcü değer | Kasiyer: "kaç ürün?" diye sormaz, "toplam" tuşu = gözcü. Gözcü seçme kuralı: gerçek girdiyle karışmasın (fiyat 0, yaş -1). Kalıp dört adım: önce oku, sor, işle + sonrakini oku, dön. `Kasa.java` tam dosya satır satır; terminalde `5 7 3 0`. **Tuzak:** "gövdenin başında okuyup hemen toplasaydım?" → gözcü toplanır; -1 ile fark. Poll 3 (0 toplanır mı). `(double) toplam / adet` ve `adet > 0`: 3. hafta hatırlatması. **Kilit:** "KT2: ana akış gözcüyle biten menü döngüsü; gözcü 0." **Bot ile (1 dk):** tuzaklı do-while istemi: `4 6 -1` → doğru 9; bot 10 derse "gözcünün toplandığını görmedi." | Kasa çıktısını izler; tuzağı kağıtta hesaplar | `GÖZCÜ = "toplam" tuşu` · `önce oku → sor → işle + sonrakini oku` · `GÖZCÜ İŞLENMEZ` · `4 6 -1 → 9 (yanlış) / 10 (doğru)` |
| 44-52 | Tahmin oyunu + AJAN gösterisi | `Tahmin.java` tam dosya: dört parçayı sınıf bulsun (başlangıç -1, koşul != HEDEF, adım = yeni tahmin okumak, deneme sayar ama sürdürmez). Terminalde `50 40 42`. Sonra: "Şimdi bunu üç girdiyle çalıştırıp tabloya yazsın istiyorum. Bot yapabilir mi?" Hayır, dosyayı görmez, çalıştıramaz. Gemini görev modu: klasör yetkili, istemi sayfadan kopyala, gönder. İzin diyaloglarını **yüksek sesle oku** ve onayla. Tablo gelince: ikinci satır Deneme 1, üçüncü Deneme 3 mü? "Hangi komutları çalıştırdın" satırını oku. Ajan "iyileştireyim mi?" derse HAYIR. **Kilit cümle tahtaya.** Neden kutusu: mekanik iş ajana, anlama size; artırma otomasyon değil. | Dört parçayı söyler; ajan tablosunu elle doğrular | `BOT: sorar-cevaplar · AJAN: klasörde açar, çalıştırır, getirir` · `mekanik iş → ajan · anlama → siz` · `izin = okuyarak` |
| 52-60 | Yaygın hatalar + hata avı | Dört tuzak hızlı: (1) `while (i < 3);` tahtada, Run yok: sonsuz. (2) adım unutma: "while'da ilk iş adım satırı." (3) Kapı hikayesi: 10 kapı, `<` dokuz, `<=` on. **Canlı:** "Kaç kapı?" Run, say. (4) **Canlı:** "On kere 0.1": tahmin, Run, false. Ortak nokta: iki soru. Hata avı puzzle'ı aç, 3 dk, sınıf bulur; cevap details. Bot ile sorgu istemi: tek cümle, "evde." | Kağıtta tahmin, Run; hata avında üç hatayı bulur | `while (…);` ← SONSUZ · `0'dan < · 1'den <=` · `double sayaç YOK` · `; · i++ · gözcü` |
| 60-65 | Büyük Resim: kırtasiye döngülü menü | Örnek depodaki `Uygulama.java`'yı aç; geçen haftanın switch'ine iki satır eklendi: `do {` ve `} while (secim != 0);`. Terminalde `1 2 5 7 0`. "0 ilk girdiyse Cikis ve biter; otomatik kontrol bunu dener." **Kilit:** "Bu KT2'nin şartı, KT1'in değil; KT1 tek geçişlik olabilir." Sahada kutusu tek cümle: kasa yazılımı aynı iskelet. | Çıktıyı tahmin eder | `KT2: do { menü; switch } while (secim != 0);` · `KT1: menü döngüsü ŞART DEĞİL` |
| 65-70 | KT1 listesi + vize planı + kapanış | KT1 kutusunu oku: README kural cümlesi, Uygulama.java Scanner + if/else + kural en basit hali, 0 ile hatasız çıkış, AI-BEYANI KT1 bölümü, derleniyor. **Ajan ile (2 dk):** örnek portfolyo klasöründe kontrol istemi, "KOD YAZMA"; rapor gelince bilerek bıraktığın eksiği buldu mu? "README'yi yazayım mı?" derse hayır. Doğrulama anı (1 dk): iki iddialı istem; ikincisine "doğru" derse "Sayaç nerede yaşar?" Run → cannot find symbol. Vize kutusu: 9. hafta (16-20 Kasım), gün bölümce; `/vize-plani` 30 Ekim-15 Kasım, "bugün 1. gün." Kapanış: Lab 4 + Lab 5 **bu gece**; Lab 6 4-5 Kasım, altı görev; KT1 6 Kasım, ayrı depo, ritüel labda; Poll 5. Haftaya: iç içe döngü, break/continue, bankamatiğin üç denemesi. | Listeyi kendi deposuyla karşılaştırır; anket | `KT1 6 Kasım: README · Uygulama.java · 0 → çıkış · AI-BEYANI KT1` · `ajan: kontrol et, KOD YAZMA` · `VİZE 9. HAFTA · /vize-plani · bugün 1. gün` · `Lab 4+5 BU GECE` |

## Kilit cümleler (blok blok)

**Bulmaca.** "Yüz cümle değil, dört cümle; dördüncüsü 'ikinciye dön'." · "Kaç kez olduğunu bilmiyorsak sayaç saymaz, 'dur' kelimesini bekleriz."

**Neden tekrar.** "Bilgisayarın tek üstünlüğü yorulmamak." · "Bir kez yaz, yüz kez çalıştır." · "Başlangıç, koşul, adım; biri eksikse ya hiç dönmez ya hiç durmaz."

**while.** "while: olduğu sürece. if bir kez bakar, while başa döner." · "Döngü bitince i 11'dir; koşulu bozan ilk değerde kalır." · "Koşulu yanlış yapan satır hangisi? Gösteremiyorsanız döngünüz sonsuz." · "Bot tur sayar, Playground kanıtlar."

**do-while.** "Otomat önce parayı alır, sonra sorar." · "Noktalı virgül burada zorunlu; geçen haftanın tersi." · "Kullanıcıya soru en az bir kez sorulur; o cümle do-while'dır." · "Bu on satır sözleşmedeki girdi doğrulama döngüsü; KT2'de sizin konunuzda."

**for.** "Üç parça tek satırda; adım gözünüzün önünde." · "Belli sayıda tur for, bilinmeyen while, en az bir kez do-while." · "N = 0 için do-while bir kez döner; bot 'aynı çıktı' derse yanılır."

**Gözcü.** "Kasiyer kaç ürün diye sormaz; 'toplam' tuşu gözcüdür." · "Gözcü gerçek girdiyle karışmasın: fiyat için 0, yaş için -1." · "Önce oku, sonra sor; gözcü işlenmez, yalnızca döngüyü bitirir." · "4 6 -1 için 9 diyen bot gözcünün toplandığını görmemiştir."

**Tahmin + ajan.** "Bu döngüde adım sayaç değil, yeni tahmin okumak." · "Bot sorar ve cevaplar; ajan klasörde dosya açar, çalıştırır, sonucu getirir." · "Mekanik iş ajana, anlama işi size; artırma, otomasyon değil." · "İzni okuyarak verin; 'iyileştireyim mi' derse hayır."

**Yaygın hatalar.** "while (…); sonsuz döngüdür; noktalı virgül gövdedir." · "while yazarken ilk iş adım satırı." · "On kapı: küçükken dokuz, küçük ya da eşitken on." · "Döngü sayacı int olur; double sayaç 1.0'a hiç varmaz."

**Büyük Resim.** "Geçen haftanın switch'ine iki satır: do ve while." · "Döngülü menü KT2'nin şartı, KT1'in değil."

**KT1 + doğrulama.** "Kontrol listesi ajanın işi, içerik sizin; README'deki kuralı vizede siz yazacaksınız." · "Aynı soruya bir doğru bir yanlış iddia; ikisine de evet diyen araç o gün iyi gününde değil." · "for sayacı döngü bitince yaşamaz; derleyici cannot find symbol der."

**Kapanış.** "Lab 4 ve Lab 5 bu gece 23.59." · "Lab 6 altı görev, hepsi döngü; KT1 aynı Cuma, ayrı depo, anlatım labda." · "Vize 9. hafta; plan /vize-plani, bugün 1. gün."

## Olası aksaklıklar ve B planı

| Sorun | B planı |
|---|---|
| **İnternet yok / Gemini açılmıyor** | Dersin omurgası (üç döngü, gözcü, doğrulama, dört tuzak) Playground'suz da tahtada anlatılır; her CodeTry'ın çıktısını sen söyle, sınıf tahmin etsin. Ajan gösterisi için bir gün önce alınmış tablo ekran görüntüsü; "bot ile ajan farkı" cümlesini yine söyle, resimle göster. KT1 kontrol raporu ekran görüntüsü. |
| **Görev modu programı çalıştıramıyor / stdin veremiyor** | Ajana "derle ve çalıştır" yerine "bu klasördeki Tahmin.java'yı oku, 50 40 42 girdisi için satır satır izleyip çıktıyı tabloya yaz" de; sonra sen terminalde çalıştır ve karşılaştır. "Ajan bugün yalnızca okudu; siz çalıştırdınız; fark yine aynı: bot dosyayı göremezdi bile." Lab 6 sayfasında ajan zaten yok, sorun büyümez. |
| **Ajan Tahmin.java'yı değiştirmeye kalkıyor** | Beklenen; "hayır" de ve izin diyaloğunu göster: "işte bu yüzden okuyarak onaylıyoruz." AI-BEYANI dördüncü satırına örnek. |
| **Ajan KT1 raporunda bilerek bırakılan eksiği bulamıyor** | En iyi senaryo: "ajan 'var' dedi, dosyada yok; raporu çöpe atıp listeyi elle geçin" cümlesi sayfada zaten yazıyor; göster. |
| Bulmacada sınıf tarifi bulamıyor | "Aklında bir sayı tut" diye başlat; sonra "o sayı 100'den küçükse ne yaparsın?"; "yazdıktan sonra sayıya ne yaparsın?"; "sonra hangi adıma dönersin?" Dört soru, dört cümle. |
| Playground'da biri sonsuz döngü çalıştırdı, sekme dondu | Sevin: "işte sonsuz döngü; sekmeyi kapat, yeniden aç." Terminalde Ctrl+C'yi göster. |
| Bot "kaç kez döner" tablosunda doğru (i = 11) | Güzel; "bugün iyi gününde." Yine Playground: "aracın sözü değil, çıktı." İkinci tuzak: gözcü istemi; ikisini de doğru yaparsa doğrulama anındaki iki iddialı istemde ikincisine "doğru" deme ihtimali yüksek. |
| Doğrulama anında araç iki iddiayı da doğru ayırt ediyor | "İyi; ama derleyici de ayırt ediyor, bakalım": Sayaç nerede yaşar? Run, hata oku. "Aracın doğru günü sizi doğrulamadan muaf tutmaz." |
| Poll Everywhere çalışmıyor | El kaldırma: "0 toplanır diyen / toplanmaz diyen"; "for diyen / while diyen". |
| **Süre taşıyor** | Kesilecek sıra: "1'den N'e toplam, for ile" CodeTry (evde) → bot ile "üç sürüme çevir" (evde) → "On kere 0.1" (evde, 3. haftadan biliyorlar) → hata avı puzzle'ı (evde, cevap details'te) → Sahada kutuları. **Kesilmeyecekler:** bulmaca, while canlı + sonsuz döngü, do-while canlı + NotAl, gözcü tuzağı, Tahmin + ajan gösterisi, kırtasiye iki satır, KT1 listesi + ajan kontrol, vize planı + kapanış duyuruları. |
| B şubesi öğle sonrası, enerji düşük | Bulmacayı yarış yap: dört cümleyi ilk bulan sıra. Kaç kapı: "kaç satır?" diye bahis. Tahmin oyununu bir öğrenciye oynat (42'yi bilmeden, ikili arama ipucu vermeden); "kaç denemede?" → 11. hafta ikili arama tohumu. |

## B şubesi (13.15)

Aynı akış (13.30 başla, 14.40 bitir). A şubesinden not: bulmacada tarifi bulma süresi; Poll 3'te "0 toplanır" diyenlerin oranı; ajan gösterisinde izin akışında takılan nokta ve ajanın tabloyu doğru getirip getirmediği; KT1 kontrol raporunda eksiği bulup bulmadığı; doğrulama anında ikinci iddiaya ne dediği. B'de o noktalara iki cümle fazla ayır. Poll sonuçlarının ekran görüntüsünü iki şube için ayrı al.

## Ders sonrası (5 dk)

- Poll 3 (gözcü toplanır mı) ve Poll 4 (for mu while mi) sonuçlarını lab sorumlu hocasına ilet: Lab 6'da `Toplam` ve `Carpim` görevlerinde beklenen hatalar.
- Ajan gösterisinde görev modunun çalıştırma/stdin akışında ne değiştiyse not et; hafta-06 sayfasındaki "ajan ile" istemini yalnızca gerçekten yanıltıcıysa güncelle.
- "Portfolyo deposunu açan" el sayısı düşükse Pazartesi hatırlatma duyurusu: "KT1 Cuma 23.59; kabul bağlantısı /proje; ajanla kontrol istemi hafta-06 sayfasında."
- Poll 5'ten 2-3 cümle → 7. haftanın açılışında oku.
- 7. hafta: iç içe döngü, break/continue, EBOB, bankamatiğin üç denemesi (iki koşullu döngü); açılışta Tahmin.java'ya "en fazla 7 deneme" ekleyerek başla.
