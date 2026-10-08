# Hafta 3 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 9 Ekim 2026 Cuma · A şubesi 09.15 (fiilen 09.30 başla, 10.30-10.45 arası bitir) · B şubesi 13.15 (fiilen 13.30 başla, aynı akış, 14.30-14.45 bitir).
**Tek oturum, 60-75 dakika.** Slayt yok; yansıda `/haftalar/hafta-03` açık. İkinci ekranda Java Playground sekmesi ve **Codespaces ya da yerel terminal** (Scanner örnekleri için; Playground'da çalışmaz, derste bunu açıkça söyle). Poll Everywhere soruları `docs/hafta-03-polleverywhere.md`.
**Slogan:** program ilk kez bize soru soruyor.
**Üslup notu:** bu hafta anlatım hikayeli: her kavram önce 3-5 cümlelik bir sahne, sonra kod. Sahneler sayfada yazılı; derste aynı sahneleri anlat, kodu sonra aç.

## Hazırlık (derse girmeden)

- Yansı: site sayfası + Playground sekmesi + terminal (Codespaces ya da yerel) içinde `YasBoy.java`, `Tuzak.java`, `VkiHesap.java` önceden kaydedilmiş ve bir kez derlenmiş; `javac` çıktıları temiz. ChatGPT sekmesinde "Java'da 7/2 kaç eder?" yazılı, Enter'a basılmamış.
- Yedek: üç Scanner programının terminal çıktısının ekran görüntüsü masaüstünde (terminal açılmazsa yansıya koyulur).
- Kağıt: her sıraya A5 yeter (iki bardak bulmacası küçük). Tahta kalemi iki renk: siyah kutular, kırmızı kutuların içindeki değerler (değer değişince kırmızıyı sil, yeniden yaz; "üstüne yazma" fiziksel olarak görülsün).
- Fiziksel sahne için (isteğe bağlı ama çok etkili): iki şeffaf bardak, biri su, biri çay (ya da renkli su) ve boş üçüncü bardak masada, bulmacayı çözdükten sonra gerçekten takas et.
- Geçen haftadan: Poll 5 duvarından 2-3 cümle (açılışta okunacak); Lab 2'de en çok takılan nokta (lab sorumlu hocasından al; hata avı tahminlerinde kullan).
- Poll Everywhere "Hafta 3" grubu etkin.
- Hata avı programı yansıda satır numaralı görünmeli; numaralı sürümü ayrıca aç ya da tahtaya 9, 10, 11 yazmaya hazır ol.

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Öğrenci ne yapar | Tahtaya yazılacak |
|---|---|---|---|---|
| 0-8 | Açılış + iki bardak | Geçen haftanın duvarından 2-3 cümle (1 dk). "Lab 2 son teslim bu akşam 23.59, dersten sonra kapatın." Bulmacayı oku; 3 dk ver. Çoğunluk "üçüncü bardak" deyince fiziksel bardaklarla takası yap. Sonra tahtaya `int a = 5; int b = 7;` ve hatalı `a = b; b = a;`; her satırdan sonra kutuların içini kırmızıyla sil-yaz, iki 7 görülsün. `gecici` kutusunu ekle, üç adımı yaz. Diyagramı aç (h03-takas). Playground'da takas kodunu çalıştır. | Kağıda adımları yazar; `a`, `b` kutularını çizip her satırdan sonra içini yazar | Sol üst: **= EŞİTLİK DEĞİL, KOPYALAMA** · Üç kutu: `a`, `b`, `gecici` (içleri kırmızı) |
| 8-18 | Değişken ve bellek | Kantinde sipariş alan kişi sahnesi (3 cümle: kağıt yoksa unutur, kağıtta satır, üstünü karalar). Üç parça: tip, isim, değer. Bellek diyagramını aç (h03-bellek). camelCase ve "Türkçe karakter yok, çünkü terminal/otomatik kontrol" (bir cümle). Poll 1'i burada değil, tipler bloğunda sor. CodeTry "İlk kutular": önce tahmin, sonra Run; `yas` satırını sildirip `cannot find symbol` okut. | Playground'da ilk kutuları çalıştırır; hata mesajını okur | `TİP · İSİM · DEĞER` · `int yas = 19;` üstüne üç ok · `ogrenciSayisi ✓ öğrenciSayısı ✗` |
| 18-30 | Tipler ve taşma | Kumbara / banka hesabı sahnesi (4 cümle). Beş tipin tablosu hızlı; `String` için tek cümle: "sınıf, büyük harf, 2. dönem." Poll 1 ("int mi double mı: para"); sonucu gösterme, "Büyük Resim'de döneceğiz" de. Taşma: kilometre saati sahnesi; Poll 2 ("2147483647 + 1 kaç?") önce oyla, sonra Playground'da çalıştır, eksi sayıyı gör. "Hata vermedi. Kimse bağırmadı. Ariane 5'i sayfada okuyun." | Önce oy, sonra Run; tabloyu telefondan izler | `int = KUMBARA (tam, sınırlı)` · `double = BANKA HESABI (ondalıklı, yaklaşık)` · `2.147.483.647 + 1 = -2.147.483.648` (altını çiz: "sessiz") |
| 30-42 | Operatörler ve pizza | Pizza sahnesi: yedi dilim, iki kişi, bıçak yok. Poll 3 ("7/2 Java'da kaç?") önce oyla; sonra Playground'da `7 / 2` ve `7 % 2`. "Bıçağı masaya koymak = taraflardan biri double": `7 / 2.0`. İnce nokta: `double sonuc = 7 / 2;` yine 3.0; geçen haftanın 81.0'ı. Kalan: 7384 saniye → saat/dakika/saniye tahtada elle (Lab 1 bonusu hatırlat, Lab 3 Görev 2 bu). Öncelik: `1 + 2 * 3`; "şüphede parantez". `++` ve `+=` tek cümle, geçen haftanın `for`'una bağla. | CodeTry "Pizza": her satır önce tahmin; `7 / 2 * 2.0` denemesi | `7 / 2 = 3` (bıçaksız) · `7 % 2 = 1` (ortada kalan) · `7 / 2.0 = 3.5` (bıçak) · `7384 / 3600 = 2, 7384 % 3600 = 184` · `( ) → * / % → + -` |
| 42-50 | Tür dönüşümü | Bardak sahnesi: çay bardağından su bardağına (hiçbir şey kaybolmaz, otomatik), su bardağından çay bardağına (taşar, izin ister = casting). `(int) 3.9` için el kaldırt: 4 diyenler çok çıkar; çalıştır, 3; "keser, yuvarlamaz; yuvarlamak istiyorsan `Math.round`". `0.1 + 0.2` tek satır, tek cümle: "ikilikte 0,1 sonsuz kesir; para için Büyük Resim." | CodeTry "Bardaklar": önce tahmin; `0.1 + 0.2 == 0.3` denemesi | `int → double: OTOMATİK` · `double → int: (int) CASTING, KESER` · `(int) 3.9 = 3` · `Math.round(3.9) = 4` · `0.1 + 0.2 ≠ 0.3` |
| 50-55 | Sabitler | "0.20 on dört yerde" hikayesi (4 cümle: KDV değişti, on beşinci yer kaçtı, biri KDV değil indirimdi, kimse bağırmadı). `final double KDV_ORANI = 0.20;`; büyük harf. CodeTry "Sabit": `KDV_ORANI = 0.18;` ekletip `cannot assign a value to final variable` okut: "bu hata dostunuz." | Sabit kodunu çalıştırır, derleyici hatasını görür | `final double KDV_ORANI = 0.20;` · `MAGIC NUMBER ✗` |
| 55-67 | Scanner, tam dosya (terminalde canlı) | "Konuşan ama dinlemeyen program" sahnesi; "ATM bakiyenizi kodda taşımaz, sorar." Üç adım tahtaya. **Playground'da çalışmadığını açıkça söyle**, terminale geç. `YasBoy.java`: derle, çalıştır, 19 ve 1.75 gir; `print` ile `println` farkı; `%.2f`, `%d`, `%n`. Scanner diyagramını aç (h03-scanner): "Enter da bir karakter, akışta kalıyor." Poll 4 ("Enter bir karakter midir?"). `Tuzak.java`'yı önce **çözüm satırı yorumlanmış** halde çalıştır: `Merhaba , 19 yaşındasın.` boş ad görülsün; sonra yorumu kaldır, tekrar çalıştır. "Lab 3 Görev 5 bu; çözümü biliyorsunuz, kodu siz yazacaksınız." `InputMismatchException`: yaş yerine "on dokuz" yaz, çöküşü göster, "labda `gozlem.md`'ye bunu yazacaksınız." | Terminali izler; kağıda üç adımı yazar; tuzağı görünce sebebini yanındakine söyler | `1 import java.util.Scanner;` · `2 new Scanner(System.in)` · `3 nextInt() / nextDouble() / nextLine()` · `ENTER DA BİR KARAKTERDİR` · `nextInt(); nextLine(); ← yut` |
| 67-72 | VKİ + hata avı | `VkiHesap.java`'yı terminalde 80 ve 1.75 ile çalıştır: `VKI: 26.12`. "Neden double, neden parantez, neden %.2f" üç soru, üç cevap sınıftan. "Lab 3 Görev 1 bu programın altına Zayif/Normal/... ekliyor." Hata avı: "Üç hata, üç dakika, bulun, düzeltmeyin." Sıra: önce derleme (10), sonra 87 (11), en son boş ad (9). "İkisi bugünkü iki tuzağın ta kendisi." | Terminali izler; hata avında kağıda üç satır numarası ve tür | `VKI: 26.12` · `SATIR 10: javac bağırır` · `SATIR 11: 87, 87.5 değil` · `SATIR 9: boş ad, Enter` |
| 72-75 | Kantin tipleri, YZ anı, kapanış | Kantin tablosunu aç: "Her kutu bir tip. Fiyat neden int (kuruş)? Bankalar double tutmaz: 0.30000000000000004 günde yüz bin kez birikir." Sipariş tutarı sözde kodunu göster: "`/` lira, `%` kuruş; pizza ile para aynı iki işaret." YZ anı (süre varsa): ChatGPT'ye "7/2 kaç?" sonra "neden?"; cevabı sınıf doğrular. "Doğrulayan kişi, soran kişiden değerlidir." Trafik ışığı: "Labda kavram sorulur, program yazdırılmaz." Poll 5 (tek cümle). Lab 3 hatırlatması: Codespaces'i deneyip gelin. | Sözde kodda `/` ve `%`'yi bulur; anket | `PARA = int (KURUŞ)` · `13650 / 100 = 136, 13650 % 100 = 50` · `Lab 3: 14 Ekim (A) · 15 Ekim (B) · Codespaces'i deneyin · Lab 2 son teslim BU AKŞAM 23.59` |

## Kilit cümleler (blok blok)

**Açılış.** "Şimdiye kadar yazdığınız her program konuşan ama dinlemeyen biriydi. Bugün ilk kez durup size soru soracak." · "Üçüncü bardak olmadan takas olmaz. Java'da da olmaz; `gecici` o bardaktır." · "`=` eşitlik değil, kopyalama. Sağı hesapla, sola koy, eskisi silinir. Bugünkü her şey bu cümlenin üstüne kurulu."

**Değişken.** "Kantinde sipariş alan kişinin elindeki kağıt: kağıt yoksa mutfağa varana kadar unutur. Değişken o kağıttaki bir satırdır." · "Her satırın üç parçası var: ne tür bir şey (tip), nasıl bulacağım (isim), şu an ne yazıyor (değer)." · "Türkçe karakter kullanmıyoruz, çünkü terminal bozar, otomatik kontrol ASCII bekler ve klavye değişince eziyet olur."

**Tipler ve taşma.** "`int` kumbaradır: tam, eksiksiz, ama dolunca almaz. `double` banka hesabıdır: kuruşlu, milyonluk, ama yaklaşık." · "Kumbara dolunca Java 'doldu' demez. Kilometre saati gibi başa döner ve eksiye düşer. Kimse bağırmaz." · "Tam olması gereken her şey `int`, zaten ölçülmüş ve yaklaşık olan her şey `double`. Para ikisinin arasında garip bir yerde, az sonra."

**Operatörler.** "Yedi dilim, iki kişi, bıçak yok: herkes üç alır, bir dilim ortada kalır. `/` üçü, `%` ortada kalanı verir." · "Bıçağı masaya koymanın yolu: taraflardan birinin ondalıklı olması. `7 / 2.0`." · "`double sonuc = 7 / 2;` yine 3.0 verir, çünkü önce sağ taraf hesaplanır. Geçen haftanın 81.0'ı buydu." · "Fazladan parantez hiçbir zaman hata değildir; eksik parantez her zaman mantık hatasıdır."

**Dönüşüm.** "Çay bardağından su bardağına: hiçbir şey taşmaz, Java sormadan yapar. Su bardağından çay bardağına: taşar, Java izin ister, o izin `(int)`." · "`(int) 3.9` dört değil üçtür. Casting yuvarlamaz, keser. Yuvarlamak istiyorsan `Math.round`." · "0,1 ikilik tabanda tıpkı onluk tabandaki üçte bir gibi sonsuzdur; bir yerden kesilir, küçücük bir hata kalır."

**Sabitler.** "0.20 kodda on dört yerde geçiyordu, KDV değişti, on beşinci yer kaçtı ve bir tanesi KDV değil indirimdi. Program çalıştı, kasa aylarca yanlış kesti." · "Sayıya bir kez isim ver, her yerde ismi kullan; `final` sayesinde yanlışlıkla değiştirmeni derleyici engeller. Bu hata dostunuz."

**Scanner.** "ATM bakiyenizi kodun içinde taşımaz, size sorar. Bugün programınız da soracak." · "Üç adım: `import`, `new Scanner(System.in)`, `nextInt()`. Bu Playground'da çalışmaz; labda terminalde çalışır." · "Enter tuşu da bir karakterdir. `nextInt()` sayıyı alır, Enter'ı akışta bırakır; `nextLine()` ilk gördüğü şeyi, yani o Enter'ı alır ve boş döner." · "Çözüm tek satır: sayıdan sonra bir `nextLine()` yazıp sonucunu hiçbir yere koymayın. Lab 3 Görev 5 bu."

**VKİ ve hata avı.** "Neden `double`? 72,5 kilo olabilirsiniz. Neden parantez? `kilo / boy * boy` soldan sağa kilonun kendisini verir. Neden `%.2f`? Kimse 26.122448979591837 okumak istemez." · "Üç hata, üç dakika, bulun, düzeltmeyin. Birini derleyici yakalar, ikisini yalnızca cevabı bilen yakalar."

**Kantin.** "Bankalar parayı `double` tutmaz. Bir kuruşluk hata bir siparişte görünmez, günde yüz bin işlemde birikir ve muhasebe kabul etmez. Para kuruş cinsinden `int`." · "13650 kuruşu 136.50 diye yazmak için `/` ve `%` yetiyor. Pizza bölüşmekle para yazmak aynı iki işaret."

**YZ anı.** "Yapay zekanın cevabını ancak cevabı zaten biliyorsanız doğrulayabilirsiniz. Bugün 7/2'yi bilen kişi oldunuz." · "'Neden?' diye sorun; 'iki int bölününce int, ondalık atılır' cümlesi gelmiyorsa model ezberlemiş."

**Kapanış.** "Lab 3'e Codespaces'i açıp `java -version` görmüş gelin; lab günü ilk kez açarsanız on dakikanız beklemekle geçer." · "Lab 2'nin son teslimi bu akşam 23.59." · "Gelecek hafta program karar verecek: `if`, `else`, karşılaştırma. VKİ'nin altına 'Normal' yazan satır o zaman ders kitabına giriyor."

## Olası aksaklıklar ve B planı

| Sorun | B planı |
|---|---|
| **Terminal / Codespaces açılmıyor** | Masaüstündeki ekran görüntülerini yansıya koy; `YasBoy` ve `Tuzak` çıktılarını görüntüden oku. Playground'da `nextInt()` satırlarını `int yas = 19;` ile değiştirip gerisini çalıştır; "girdi sabit ama hesap aynı" de. Enter tuzağını tahtada akış kutusuyla anlat: `[1][9][⏎]`, nextInt ilk ikiyi alır, üçüncüsü kalır. |
| **İnternet yok** | Diyagramlar sayfada gömülü SVG; sayfayı derse girmeden bir kez aç. Playground kodlarını tahtaya yaz, sınıf kağıtta tahmin eder; taşma için `-2147483648` sonucunu sen söyle. YZ anını atla. |
| İki bardak bulmacası 30 saniyede bitiyor | Beklenen; asıl iş tahtadaki `a = b; b = a;`. Ek soru: "`gecici` olmadan, yalnızca toplama-çıkarma ile takas olur mu? `a = a + b; b = a - b; a = a - b;` neden çalışıyor ve neden 'hileli'?" (taşma riski; az önce öğrendiler). |
| `(int) 3.9` için sınıfın çoğu 3 diyor | Güzel; ek soru: "`(int) -3.9` kaç?" (-3; sıfıra doğru keser) ve "`Math.round(-3.9)`?" (-4). |
| Hata avında boş ad hatasını (satır 9) kimse bulamıyor | Beklenen durum; "Satır 7'de ne yazdınız, Enter'a bastınız mı, Enter nereye gitti?" diye sor; terminalde `Tuzak`'ı çözüm satırı yorumlu halde bir kez daha çalıştır. |
| Poll Everywhere çalışmıyor | El kaldırma: "7/2 için 3 diyen", "3.5 diyen"; taşma için "eksi diyen, hata diyen". |
| Süre taşıyor | Kesilecek sıra: YZ anı (siteye bırak; labda sarı bölge kutusu var) → Sahadan örnekler (siteye bırak) → Sabitler bloğu CodeTry'sız, yalnızca hikaye → `++`/`+=` cümlesi → Kantin yalnızca tablo, sözde kod siteye. İki bardak, pizza, bardaklar (casting) ve **Scanner tam dosya terminalde** kesilmez. |
| B şubesi öğle sonrası, enerji düşük | Fiziksel bardak sahnesini mutlaka yap (ayağa kaldırır). Pizza için sınıftan iki gönüllü ve yedi kağıt dilim. Hata avını 4 dakika yap, yarışma havası ver. |

## B şubesi (13.15)

Aynı akış, aynı dakikalar (13.30 başla, 14.30-14.45 bitir). A şubesinden not: Poll 3'te 3.5 yüzdesi, `(int) 3.9` için 4 diyenlerin oranı, hata avında en geç bulunan hata, terminal gösteriminde takılan nokta (Codespaces açılış süresi?). B'de o noktaya iki cümle fazla ayır. Poll sonuçlarının ekran görüntüsünü iki şube için ayrı al.

## Ders sonrası (5 dk)

- Hata avında en geç bulunan hata → Lab 3 Görev 5 için lab sorumlu hocasına not: öğrenciler orada takılacak, Enter tuzağını labın başında bir kez daha anlatsın.
- Poll 1'de ("para: int mi double mı") double diyenlerin yüzdesi → 4. haftanın açılışında "geçen hafta yüzde X'iniz double dedi" diye hatırlat.
- Poll 5'ten 2-3 cümle → 4. haftanın açılışında oku.
- Codespaces ilk açılışında takılan öğrenci sayısı → Lab 3 sayfasının Adım 0'ına ek not gerekiyorsa ekle; duyuruda "Codespaces'i deneyin" cümlesini bir kez daha yinele.
