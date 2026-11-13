# Hafta 8 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 13 Kasım 2026 Cuma · A şubesi 09.15 (fiilen 09.30-10.40) · B şubesi 13.15 (fiilen 13.30-14.40).
**Tek oturum, 70 dakika fiilî.** Slayt yok; yansıda `/haftalar/hafta-08` açık (Yansı modu: Alt+Y). İkinci ekranda Java Playground sekmeleri, HackerRank ve Gemini masaüstü uygulaması. Poll Everywhere soruları `docs/hafta-08-polleverywhere.md`.
**Slogan:** aynı cevap, 85 adım ve 3 adım; bu döngü kaç kez dönüyor?

## Üslup notu

Bu hafta dersin ana fikri **sınıfta olmanın bir anlamı olması**. Sayfa evde okunur; sınıfta yapılan şey sayfada yoktur. Bu yüzden her kapsülün asıl malzemesi **Sınıfta** şerididir: koro, sessiz iz tablosu, sırayla bölme, kağıtta Euclid, ayakta FizzBuzz. Kodu okutma, yaşat.

Her kapsülde ritim:

1. Fikir satırını yüksek sesle oku (tek cümle; tahtaya kısaltılmışı).
2. **Sınıfta** etkinliğini yap (varsa). Etkinlik koddan önce gelir.
3. Kodu göster, **tahmin ettir, sonra Run.**
4. Hikayesi olan kapsülde hikayeyi anlat; süre sınırı tabloda yazıyor. Hikaye bir kapsülde 90 saniyeyi geçmesin.
5. **Sor** ve **Doğrula** şeritleri bu hafta büyük ölçüde eve kalıyor; canlı Gemini yalnızca 4. kapsülde (bot tabloyu yazmaz, öğrencinin satırını onaylar) ve zaman kalırsa 12. kapsülde.

**Mülakat sorusu kartları nasıl kullanılır:** soruyu yansıt ve yüksek sesle oku → **60-90 saniye sessiz düşünme, kağıt kalem** (kronometre yansıda) → bir gönüllü tahtada çözümünü **anlatır** (yazmasa da olur, sesli düşünsün) → sınıfa "eksik köşe durumu var mı?" → cevabı aç, "mülakatçının duymak istediği cümle"yi oku. Yedi kartın hepsi yetişmez: **4. kapsül (kaç kez x), 6. kapsül (asal) ve 11. kapsül (FizzBuzz) kartları derste**; piramit, break/continue, palindrom ve EBOB/EKOK kartları "bu akşam kağıtta" diye eve.

**Öncelik sırası (70 dakikaya sığması için):**

- **Mutlaka:** 1, 3, 4, 5, 6, 9, 11. Bunlar kısaltılmaz.
- **Kısa geç ya da eve bırak:** 2, 7, 8, 10, 12. Her biri için tabloda "kısa sürüm" yazıyor.

Sabit cümleler: **"Bu döngü kaç kez dönüyor?"** (her iç içe döngüde sor) ve **"Asistan çalışan kodu verir, tur sayısını siz sorarsınız."** Hata avındaki sonsuz döngüyü (`i++` yerine `j++` olması gereken satır) **Playground'da çalıştırma**; kağıtta.

## Hazırlık (derse girmeden)

- Playground'da ayrı sekmelerde hazır: "Saat" (1), "9 x 9 çarpım tablosu" (2), "Yıldız üçgeni" (3), "İz tablosu alıştırması" (4), "El sıkışma sayacı" (5), "Asal mı?" (6), "İki algoritma, bir sayaç" (9), "Pi tahmini" (10). 7 ve 8'in kutuları tek sekmede dursun, zaman kalırsa.
- **HackerRank hesabı açık**, Java alanında **"Java Loops I"** sorusu ayrı sekmede hazır; çözümü bir gün önce bir kez gönderip yeşil işareti gör (dil seçimi Java 15/8 fark etmez; `Scanner` ile `N` oku, `N x i = sonuc` yaz). Giriş ekranı sınıfta görünmesin.
- Gemini masaüstü açık, "Java Hocam" becerisi seçili; 4. kapsülün "tabloyu SEN yazma" istemi panoda hazır.
- **Kronometre** yansıda gösterilebilir olsun (telefon ya da tarayıcı): 3 dk iz tablosu, 60-90 sn mülakat sessizliği, 3 dk kağıtta FizzBuzz.
- Tahtada önceden: sağ üst köşeye küçük, sabit bir kutu: `Vize: 24 Kasım Salı 17.00 · kapsam 1-8. hafta`. Ders boyunca silinmez.
- Yedek ekran görüntüleri (internet ya da Playground sorununa karşı): saat çıktısı (6 satır), 9 x 9 tablo, iz tablosu çıktısı (son satır `Toplam: 14`), el sıkışma 5 / 70 / 250 / 1000 / 10000 sonuçları, "İki algoritma" çıktısı (85 ve 3; büyük çiftte 123.456.781 ve 2), pi üç çalıştırma, HackerRank yeşil işareti.
- İnternet yoksa B planı: `Belgeler/algo1` klasöründe aynı kutuların tam dosya halleri (`Saat.java`, `Iz.java`, `ElSikisma.java`, `Asal.java`, `Ebob.java`, `Pi.java`) derlenmiş dursun; terminalden çalıştır.
- 7. haftanın Poll 6 duvarından 2-3 cümle ve Poll 5'in en bulanık kapsülü açılış için elde olsun.
- Boş A4 getirmelerini bir gün önce WhatsApp kanalından hatırlat: "yarın kağıt kalem şart."
- **Salonları bölümle teyit et:** programda A306 hem A hem B şubesinde görünüyor. Teyit gelmeden salon numarasını tahtaya yazma; "duyurudaki tablo geçerli, değişirse kanaldan yazarım" de.

## Açılış duyuruları (ilk 60 saniye, bulmacadan önce)

- **Ara sınav 24 Kasım Salı 17.00-18.00.** A: A304-306; B: A306, A404-406. Kağıt üzerinde, telefon kapalı.
- **Kapsam 1-8. hafta;** bugünkü dersin tamamı dahil, 20 Kasım'daki metotlar hariç. O hafta dersler ve lablar normal.
- **Lab 7 son teslim bu gece 23.59.**
- "Bugün kağıt kalem dışarıda olsun; üç kez sessiz çalışacağız."

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Öğrenci ne yapar | Tahtaya yazılacak | Hikaye (süre) |
|---|---|---|---|---|---|
| 0-6 | Bulmaca: el sıkışma | Duyurular (60 sn). Geçen haftanın duvarından 2 cümle. Beş gönüllü tahtaya: "herkes herkesle bir kez." Sınıf yüksek sesle saysın. "Neden 25 değil, neden 20 değil?" Sonra "70 kişi?" tahmin topla, yöntem iste: 4 + 3 + 2 + 1. "Bir sayımın içinde başka bir sayım yaptınız." 70 → 2415 (bir saat yirmi dakika), 250 → 31.125. | Beş gönüllü el sıkışır; sınıf sayar, 70 için tahmin yazar | `5 kişi → 4+3+2+1 = 10` · `70 → 2415` · `250 → 31.125` · `kişi ×3,5 → iş ×13` | Yok; "bu orantısızlık bir oyunu yedi yıl bekletti, 5. kapsülde" diye merak bırak (10 sn) |
| 6-11 | Kapsül 1 ★ MUTLAKA · Saat | Fikir satırı. **Koro:** sol yarı akrep, sağ yarı yelkovan. Akrep "sıfır" der ve susar; yelkovan "sıfır, bir, iki"; akrep "bir"; yelkovan yine baştan. "Kim kimi bekliyor? Yelkovan neden baştan başladı?" **Poll 1.** Sonra "Saat" kutusu: Run, 6 satır. 24 ve 60 yap: 1440. Diyagramda `j = 1` kutusunu parmakla göster. | Koro; Poll 1; çıktıyı tahmin eder | `DIŞ bir adım → İÇ tam tur` · `2 × 3 = 6` · `iç sayaç her dış turda BAŞTAN` | Ekran pikselleri: 1920 × 1080, saniyede 124 milyon tur (30 sn) |
| 11-13 | Kapsül 2 · Çarpım tablosu (KISA) | Kutuyu Run et, tabloyu göster. Tek soru: "`println()` neden iç döngünün dışında?" Satırı sil, Run: tek satır. Geri koy. `%4d`'yi bir cümleyle söyle. Gerisi evde. | Tek soruya cevap verir | `dış = SATIR · iç = SÜTUN` · `print / println` | Yok |
| 13-19 | Kapsül 3 ★ MUTLAKA · Desen | Tahtaya 5 satırlık dik üçgeni çiz. Her satır için sor: "kaç yıldız, satır numarasıyla ilişkisi ne?" Yanına tablo: satır 1 → 1, satır 2 → 2, satır i → i. "İç koşul?" → `j <= i`. Run. "Baş aşağı çevirmek için hangi tek ifade?" → `n - i + 1`. Yöntemi adlandır: **her satır için 'kaç tane' sor.** Piramit kartını yansıt, yalnızca ipucunu oku: "iki ayrı 'kaç tane'; bu akşam kağıtta." | Satır başına yıldız sayısını söyler; ters üçgen ifadesini bulur | `satır i → i yıldız → j <= i` · `ters: n - i + 1` · `HER SATIR İÇİN: KAÇ TANE?` | Yok |
| 19-28 | Kapsül 4 ★★ MUTLAKA · İz tablosu | "Sınavda en çok puan getiren beceri bu." Kodu yansıt, `j = i` başlangıcını göster ama açıklama. **Poll 2** (önce tahmin). **Kronometre 3 dk: sessiz, tek başına, telefon kapalı; iz tablosu.** Sonra 1 dk yan sıra karşılaştırma: "tablonuz farklıysa fark hangi satırda başlıyor?" Run; çıktıyı tabloyla satır satır eşle. Details'teki tabloyu aç. Canlı Gemini (40 sn): "tabloyu SEN yazma" istemi; bir öğrencinin 4. satırını yaz, bot "doğru/yanlış" desin. Sonra **mülakat kartı (kaç kez x):** 60 sn sessiz, gönüllü tahtada anlatır, cevabı aç: 45, `n(n-1)/2`, "çarpmıyorum, topluyorum." Uyarı kutusunu oku. | 3 dk iz tablosu; yan sırayla karşılaştırır; mülakat sorusunu kağıtta çözer | Tablo başlığı: `tur · i · j · toplam` · `3 + 2 + 1 = 6 tur` · `Toplam: 14` · `0+1+…+9 = 45 = n(n-1)/2` | Yok; "mülakatta da bilgisayar sizsiniz" (10 sn) |
| 28-34 | Kapsül 5 ★ MUTLAKA · Maliyet | Bulmacanın rakamlarına dön. "40.000 öğrenci için tahmin?" En düşük ve en yüksek tahmini tahtaya yaz. "El sıkışma sayacı": n = 1000 → 499.500; n = 10000 → 49.995.000. "Girdi 10 kat, iş kaç kat?" **Poll 3.** 40.000 için kağıtta: yaklaşık 800 milyon (n = 40000'i Playground'da çalıştırma, 800 milyon tur zaman aşımına düşebilir; sonucu söyle: 799.980.000). Sonra GTA hikayesi. Alışkanlık kutusunu oku. | Tahmin yazar; Poll 3; "kaç kat" sorusuna cevap verir | `n ×10 → iş ×100` · `KARESEL BÜYÜME` · `BU DÖNGÜ KAÇ KEZ DÖNÜYOR?` · `63.000 kalem → 6 dakika` | **GTA Online** (90 sn): altı dakika açılış, t0st, 63.000 kalem, fark edilmemiş iç içe döngü, yüzde 70, 10.000 dolar; son cümle "yedi yıl kimse sormadı" |
| 34-41 | Kapsül 6 ★ MUTLAKA · break ve asal | "Anahtarı çantada bulunca cepleri aramazsınız." **Sıra bölmesi:** "91 asal mı?" Sıradaki öğrenci 2'yi dener, sonraki 3'ü, 5'i, 7'yi; yedide "buldum, dur!" Tahtaya `break`. "97 için nereye kadar denemek yeter? 96? 48? Daha az?" Oy topla. 36'nın bölen çiftlerini yaz: 2-18, 3-12, 4-9, 6-6; "küçük olan karekökü geçemez." Kutu: 91, 97, sonra 1000003 → 999 deneme; "`i <= n` olsaydı bir milyon." **Mülakat kartı (asal):** 60 sn sessiz; "mülakatçı 'daha iyisi?' der" → üç iyileştirmeyi sınıftan topla; köşe durumları: 0, 1, 2, negatif. | Sırayla böler; kareköke kadar fikrini tartışır; iyileştirmeleri söyler | `BULUNCA DUR = break` · `36: 2·18 3·12 4·9 6·6` · `i * i <= n` · `1.000.000 → 999` · `köşe: 0, 1, 2, negatif` | Yok; "aynı cevap, bin kat az iş" (10 sn) |
| 41-44 | Kapsül 7 · continue ve bayrak (KISA) | Kasiyer benzetmesi tek cümle: "break kasayı kapatır, continue bu müşteriyi geçer." "Üçün katlarını atla" Run. Sonra tek soru: "İç içe döngüde break hangisini kırar?" **Poll 4.** "Çarpımı 42" kutusunda `&& !bulundu`'yu göster: bayrak. while + continue tuzağı ve mülakat kartı evde. | Poll 4; bayrağın ne işe yaradığını söyler | `break → en İÇTEKİ döngü` · `BAYRAK: boolean bulundu` | Yok |
| 44-47 | Kapsül 8 · Basamak döngüsü (KISA) | Tahtada 4725'i elle sök: `% 10` → 5, `/ 10` → 472; dört tur. "Sınavda izleme sorusu olarak gelir." Kutuyu bir kez Run (12321). Palindrom kartı ve 1200 sorusu evde. Zaman dardaysa yalnızca tahtadaki söküm ve Luhn cümlesi. | 4725'in turlarını söyler | `% 10 → son basamak` · `/ 10 → at` · `4725 → 5, 52, 527, 5274` | Luhn: kart numarasının son hanesi, 1954 IBM (30 sn) |
| 47-56 | Kapsül 9 ★★ MUTLAKA · EBOB | "İki yöntem, aynı cevap." Önce kaba kuvvet tek cümle: "105'ten geriye her sayıyı dene." **Kağıtta Euclid, 2 dk:** 252 ÷ 105 kalan 42; 105 ÷ 42 kalan 21; 42 ÷ 21 kalan 0. "Kaç bölme yaptınız?" Üç. Diyagramı göster. Kutu: Run → **85 ve 3**; sloganı tahtaya. Sonra 987654321 ve 123456789: 123.456.781 adım ve 2 adım; sınıfın tepkisini bekle. "Ekranınız 1920 × 1080; EBOB size neyi söyler?" → 120, 16:9. RSA hikayesi. Mülakat kartı (EBOB/EKOK) evde; yalnızca "önce böl, sonra çarp: taşma" cümlesini söyle. | 252/105'i kağıtta Euclid'le çözer; adım sayılarını karşılaştırır | `252 = 2·105 + 42` · `105 = 2·42 + 21` · `42 = 2·21 + 0` · `EBOB = 21` · `85 ADIM / 3 ADIM` · `1920 : 1080 = 16 : 9` | **Euclid** MÖ 300 (15 sn) + **RSA anahtarları** 2012: anahtarları ikişer ikişer EBOB'la, ortak asal çıkarsa ikisi de kırılır (75 sn) |
| 56-59 | Kapsül 10 · Monte Carlo (KISA; zaman yoksa EVE) | Tahtaya kare ve çeyrek daire. Beş gönüllü birer nokta söylesin (20 değil, 5 yeter); içeride mi dışarıda mı. "Pi tahmini" kutusu: N = 100 iki kez (farklı sonuç), N = 1000000 bir kez. Hikaye. Sor/Doğrula evde. | Nokta söyler; iki çalıştırmanın farkını yorumlar | `içeride / toplam ≈ pi / 4` · `x*x + y*y <= 1` · `çok deneme → iyi tahmin` | **Ulam** 1946: iskambil falı, von Neumann, ENIAC, amcanın kumarhanesi; AlphaGo (60 sn) |
| 59-67 | Kapsül 11 ★★ MUTLAKA · FizzBuzz | **Ayağa kalk:** sınıf sırayla sayar, yanılan oturur; 30'a kadar ya da 90 saniye. Hikaye. Sonra **kronometre 3 dk: kağıtta Java ile FizzBuzz; yapay zeka yok, Playground yok.** Dolaş, 15 için ilk koşula ne yazdıklarına bak. **Poll 5.** Bir gönüllünün çözümünü Playground'a yaz, Run; 15'te ne yazdı? Kartı aç: "en özel koşul en üstte." Takip soruları tek cümle: "7'de Bazz?", "nasıl test edersiniz? 1, 3, 5, 15, 30, 100." Neden kutusunu oku: "mülakat kodu değil sizi ölçer." | Ayakta oyun; 3 dk kağıtta FizzBuzz; Poll 5 | `15 → ÖNCE i % 15` · `EN ÖZEL KOŞUL EN ÜSTTE` · `test: 1, 3, 5, 15, 30, 100` | **FizzBuzz** 2007: Imran Ghory, Jeff Atwood, "mezunların çoğu çözemiyor" (45 sn) + Google yüz yüze mülakat cümlesi (15 sn) |
| 67-70 | Kapsül 12 + kapanış | Zaman varsa (2 dk): HackerRank "Java Loops I" canlı; "bu soru geçen haftanın çarpım tablosu"; Gönder, yeşil işaret. Zaman yoksa yalnızca tabloyu yansıt: "bu akşam HackerRank'te dört soru." **Poll 6** (çoklu seçim + duvar). Kapanış duyuruları. Hata avı puzzle'ı eve: "üç hata, dört dakika; üçüncüsü bugünün en değerli dersi." | Poll 6; site adresini not alır | `GÜNDE BİR SORU` · `HackerRank → Java Loops I` · `Lab 7 bu gece · Lab 8 18-19 Kasım · Vize 24 Kasım 17.00` | Yok |

## Kapanış duyuruları (son 60 saniye)

- **Lab 7 bu gece 23.59.**
- **Lab 8:** A 18 Kasım Çarşamba 13.15, B 19 Kasım Perşembe 15.15; son teslim **20 Kasım Cuma 23.59**. "Sınavdan önceki son uygulamalı prova; teslim ritüeli iz tablosu."
- **Ara sınav 24 Kasım Salı 17.00**, kapsam 1-8. hafta. Vize planı **23 Kasım'a uzadı**: `/vize-plani`.
- **KT2 27 Kasım Cuma 23.59** (sınavdan üç gün sonra); menü döngüsünü bu hafta sonu bitiren 25-27 Kasım'ı rahat geçirir.
- "Sınav için en iyi hazırlık: sayfadaki yedi mülakat sorusu, kağıtta, yardımsız."

## B planı

- **Zaman biterse:** önce 12 (yalnızca tablo yansıtılır), sonra 10 (tamamı eve; "Monte Carlo'yu Lab 8 bonusunda yazacaksınız" de). Hâlâ sıkışıksa 8 yalnızca tahtadaki 4725 sökümüne, 7 yalnızca Poll 4'e iner. 4, 9 ve 11'in sessiz çalışma süreleri **kısaltılmaz**.
- **Zaman artarsa (B şubesinde olabilir):** 7. kapsülün while + continue tuzağını tahtada izlet; palindrom kartını 60 saniyelik sessizlikle yap.
- **İnternet yoksa:** Playground yerine yerel terminal (`Belgeler/algo1`); Poll yerine el kaldırma (şıkları tahtaya yaz, say); HackerRank yerine ekran görüntüsü; Gemini adımını atla.
- **Gönüllü çıkmazsa:** el sıkışmayı ön sıradaki beş kişiyle yerlerinde yaptır; FizzBuzz oyununu ayakta değil oturarak sıra sıra.
- **FizzBuzz oyunu çok gürültülü olursa:** 15'te kes; amaç ısınma, asıl iş kağıttaki üç dakika.

## Ders sonrası

- Poll sonuçlarını iki şube için ayrı kaydet (ekran görüntüsü): Poll 2'de "6" ve "12" yüzdeleri, Poll 3'te "10 kat" yüzdesi, Poll 4'te "ikisini birden" yüzdesi, Poll 5'te "FizzBuzz" yüzdesi, Poll 6'nın en bulanık iki kapsülü ve duvardan 3 cümle.
- **Ömer'e Lab 8 notu:** teslim ritüeli iz tablosu (bir iç içe döngü seç, 30 saniyede kağıtta izlet); Poll 6'da en bulanık çıkan iki kapsül ve ilgili görevler; FizzBuzz görevinde koşul sırası hatasını beklesin (Poll 5 yüzdesi); Euclid görevinde `Adim` sayısının `while` turu olarak sayıldığını hatırlat; Lab 8 sınavdan önceki son prova, kağıt kalem istesin.
- Sessiz iz tablosunda (4. kapsül) dolaşırken gördüğün en yaygın hatayı yaz (`j`'yi 1'den başlatmak, `toplam`'ı her dış turda sıfırlamak); 9. haftanın açılışında iki dakikalık tekrar olsun.
- Salon teyidi geldiyse duyuruyu ve `/vize-plani` sayfasını güncelle; gelmediyse Pazartesi bölüme yeniden sor.
- Duvardaki "bugün sınıfta olmasaydım neyi kaçırırdım?" cevaplarından en iyi üçünü sakla; MÜDEK kanıtı ve 9. hafta açılışı için.
