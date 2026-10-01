# Hafta 2 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 2 Ekim 2026 Cuma · A şubesi 09.15 (fiilen 09.30 başla, 10.30-10.45 arası bitir) · B şubesi 13.15 (fiilen 13.30 başla, aynı akış, 14.30-14.45 bitir).
**Tek oturum, 60-75 dakika.** Slayt yok; yansıda `/haftalar/hafta-02` açık. İkinci ekranda Java Playground ve Graphviz Online sekmeleri hazır. Poll Everywhere soruları `docs/hafta-02-polleverywhere.md`.
**Slogan:** önce çiz, sonra yaz, sonra kır.

## Hazırlık (derse girmeden)

- Yansı: site sayfası + Playground sekmesi + Graphviz Online sekmesi (boş) + ChatGPT sekmesi (ATM kodu için "Graphviz DOT olarak akış diyagramı çiz" istemi yazılı, Enter'a basılmamış).
- Yedek: ATM kodunun AI tarafından üretilmiş DOT çıktısı önceden alınmış, metin dosyası olarak masaüstünde (internet giderse okunur, tahtaya çizilir).
- Kağıt: her sıraya A4 (ATM çizimi için A5 dar gelir); tahta kalemi iki renk (siyah kutular, kırmızı Evet/Hayır okları).
- Geçen haftadan: Poll 7 duvarından seçilmiş 2-3 cümle (açılışta okunacak); tahta fotoğrafı (dört kelime).
- Poll Everywhere "Hafta 2" grubu etkin.
- Hata avı programı yansıda satır numaralı görünmeli; sayfadaki kod bloğu numarasızsa yansıya ayrıca numaralı sürümü aç (ya da tahtaya 9, 10, 12 yazmaya hazır ol).

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Öğrenci ne yapar | Tahtaya yazılacak |
|---|---|---|---|---|
| 0-10 | Açılış + ATM bulmacası | Geçen haftanın duvarından 2-3 cümle oku (1 dk). Poll 1 ("akış diyagramı çizdin mi"). Bulmacayı oku: "Kutular ve oklar, sembol bilmeniz gerekmiyor. İkili, 8 dakika." Dolaş; en az iki farklı çizimi fotoğrafla/hatırla (biri tek bitişli, biri çok bitişli). | Kağıda ATM akışını çizer; üç soruya cevap yazar | Sol üst: `Playground · Graphviz Online · dreampuf.github.io/GraphvizOnline` · Üst ortaya slogan: **ÇİZ → YAZ → KIR** |
| 10-20 | Semboller ve üç yapı | Bir çiftin çizimini tahtaya aktar. "Kaç tür kutu kullandınız?" Üç cevap gelir: iş yapan, soru soran, gösteren. Sembol tablosunu sayfadan göster; tahtadaki kutuların şeklini düzelt (dikdörtgen, elmas, paralelkenar). Sayfadaki ATM diyagramını aç; DOT kaynağını aç, "25 satır metin, çizim bedava." Nehir diyagramını göster: "Geçen hafta yalnızca sıra vardı." Üç yapıyı yaz. | Kendi çizimini sayfadaki çözümle karşılaştırır; farkı söyler | Sağda: **SIRA · SEÇİM · TEKRAR** · Altına: `düz ok · elmas · geri ok` · Küçük not: `tek BAŞLA, tek BİTİR, her elmasa Evet/Hayır` |
| 20-45 | Üç örnek, üç dil | Örnek 1: diyagram, sözde kod, Java yan yana; "elmas = EĞER = if" tahtaya. Örnek 2: önce Poll 2 ("1'den 10'a toplam kaç"), sonra kağıt üzerinde elle izleme (toplam ve i sütunları, 3 tur yeter), sonra Playground. Örnek 3: ATM kodu; "yanlış sayısı neden sabit? Çünkü girdi 3. hafta." Dört değişkenle oynat (istek=6000, bakiye=1000, yanlisSifre=3). Sözde kod neden yazılır: iki cümle. | Her kodu Playground'da çalıştırır; önce tahmin, sonra Run; Örnek 2'de kağıtta izler | `elmas = EĞER ... İSE = if` · `geri ok = TEKRARLA ... OLDUKÇA = for` · `toplam = toplam + i` (altını çiz: "matematik değil, atama") |
| 45-55 | Anatomi ve derleme | Merhaba.java'yı satır satır: class = dosya adı, main = kapı, `{ }` = kutu, `;` = cümle sonu. "Bloğu açan satırda `;` yok; o cümle değil, kapı." Playground'da neden yoktu: JShell görünmez sınıf. Derleme diyagramını aç; kaynak → javac → .class → JVM. Hata varsa javac durur, geri ok. JDK/JRE/JVM tek cümle. | Dinler; Lab 1'de yazdığı iskeleti hatırlar | `javac Merhaba.java → Merhaba.class` · `java Merhaba` · `JDK ⊃ JRE ⊃ JVM` |
| 55-65 | Hata avı, ilk tur | Üç hata tablosu (1 dk). Poll 3 ("sıfıra bölen program ne yapar") önce. Programı yansıya al: "Üç hata, üç dakika, satır ve tür. Düzeltmeyin, bulun." 3 dk sonra el kaldırt: önce sözdizimi (12), sonra çalışma zamanı (10), en son mantık (9). Mantık hatasında dur: "81.0, nokta var, doğru sanırsınız. Kimse bağırmadı." Poll 4 ("en sinsi hata"). | Kağıda üç satır numarası ve tür yazar; sonra `<details>` açılınca kontrol eder | `SÖZDİZİMİ: javac bağırır` · `ÇALIŞMA ZAMANI: JVM bağırır` · `MANTIK: kimse bağırmaz` · `81.0 ≠ 81.67` |
| 65-75 | Kantin, YZ anı, kapanış | Kantin diyagramını aç: "Bugünkü her şey burada: sıra, seçim, tekrar; yeni olan silindir." Alt akış sözde kodunu göster: "`EĞER stok < adet` = bugünkü `if`. Kutular büyür, yapılar değişmez." Portfolyo bağı: "KT4'te uygulamanız bu diyagramın bir kutusu." YZ anı (süre varsa): ChatGPT'ye DOT çizdir, Graphviz Online'a yapıştır, "hangi düğüm eksik?" Trafik ışığı: "Labda DOT sözdizimi sorulur, diyagram çizdirilmez." Poll 5 (tek cümle). Lab hatırlatması. | Diyagramda eksik düğümü bulur; anket | `Lab 2: 7 Ekim (A) · 8 Ekim (B) · Graphviz Online'ı denemiş gelin · Lab 1 son teslim BUGÜN 23.59` |

## Kilit cümleler (blok blok)

**Açılış.** "Geçen hafta kağıda liste yazdınız; bu hafta kağıda kutu çiziyoruz. Sonra aynı şeyi üç dilde yazacağız; en sonunda çalışan bir programı bilerek kıracağız." · "Sembol bilmeniz gerekmiyor; semboller sizin çiziminizden çıkacak."

**Semboller.** "Üç ihtiyaç, üç şekil: iş yapan dikdörtgen, soru soran elmas, alan ya da gösteren paralelkenar. Gerisi süs." · "Her elmasın iki oku var ve ikisinin de adı var. Adsız ok, cevapsız soru demektir." · "Bu diyagram 25 satırlık metinden çıktı. Metin kopyalanır, düzeltilir; çizim zor düzeltilir. Labda diyagramı kodla çizeceksiniz."

**Üç yapı.** "1966'da kanıtlandı: her program bu üçünden yazılır. Dönem boyunca başka bir şey öğrenmeyeceksiniz; bu üçünü iç içe koymayı öğreneceksiniz." · "Geçen haftanın nehri yalnızca sıraydı. ATM'de üçü de var."

**Üç örnek.** "Elmas, EĞER, if: aynı şeyin üç adı." · Örnek 2'de: "Çalıştırmadan önce 55 diyen el kaldırsın. Şimdi kağıtta üç tur izleyin: toplam 0, 1, 3, 6... Elmastan kaç kez Evet geçtiniz?" · "`toplam = toplam + i` matematikte saçma, burada normal: sağı hesapla, sola koy." · ATM'de: "Üç yanlışta kart yutmayı neden saymadık? Çünkü şifreyi klavyeden almak 3. haftanın işi. Bu hafta yanlış sayısı bir kutuda sabit duruyor."

**Anatomi.** "class: programın adı, dosya adıyla aynı. main: kapı; JVM buradan girer. Süslü parantez: kutu. Noktalı virgül: cümle sonu. Kapı olan satırda noktalı virgül yok." · "Playground bunları yazmıyordu çünkü sizin yerinize görünmez bir sınıfın içine koyuyordu. Gerçek program dosyadır, dosya töreni ister."

**Derleme.** "javac hata bulursa .class üretmez. Bu yüzden sözdizimi hatası olan program hiç çalışmaz; yarım çalışmaz, hiç çalışmaz." · "JVM: çalıştırır. JRE: JVM artı kütüphaneler. JDK: hepsi artı javac. Siz JDK kurdunuz."

**Hata avı.** "Üç hata, üç dakika. Düzeltmeyin, bulun." · "Sırayla: önce derleyici bağırır, sonra JVM bağırır, mantık hatasında kimse bağırmaz. 81.0 görürsünüz, nokta var, doğru sanırsınız. Öğrenci 0,67 puan kaybeder, kimse fark etmez." · "Mantık hatasının tek ilacı: çalıştırmadan önce cevabı bilmek."

**Kantin.** "Bu diyagramda bugün öğrendiğiniz her şey var; yeni olan tek şey silindir." · "`EĞER stok < adet` bugün yazdığınız `if (bakiye >= istek)` ile aynı. Yemeksepeti'nin arkasındaki mühendis de bu if'i yazıyor; onun stok'u veritabanından geliyor." · "Bu uygulamayı bu dönem yazmıyoruz; ama portfolyonuz bu diyagramın bir kutusu olabilir. KT4'te 'benim programım hangi kutu?' sorusunu soracağım."

**YZ anı.** "Yapay zeka diyagramı 'aşağı yukarı doğru' çizer. Mühendislikte aşağı yukarı yoktur. Eksik düğümü bulan kişi çizdirenden değerlidir." · "Labda DOT sözdizimini sorabilirsiniz: elmas nasıl çizilir. 'Şu kodun diyagramını çiz' diyemezsiniz; ritüelde o diyagramı siz anlatacaksınız."

**Kapanış.** "Lab 2'ye Graphviz Online'ı denemiş gelin: ATM'nin DOT kaynağını yapıştırın, bir etiketi değiştirin, PNG indirin. Lab 1'in son teslimi bu gece 23.59." · "Gelecek hafta klavyeden girdi: ATM'deki yanlış sayısı o zaman gerçekten sayılacak."

## Olası aksaklıklar ve B planı

| Sorun | B planı |
|---|---|
| **İnternet yok** | Diyagramlar sayfada **gömülü SVG**; sayfa açılmıyorsa bile tarayıcı önbelleğinde kalmış olur (derse girmeden sayfayı bir kez aç). Playground yerine üç örneği **tahtaya** yaz; sınıf kağıt üzerinde izler (Örnek 2 zaten kağıtta). YZ anı için masaüstündeki hazır DOT çıktısını oku; eksik düğümü tahtada arat. |
| Graphviz Online açılmıyor | Derste zorunlu değil; yalnızca gösterim. DOT kaynağını sayfadan oku, "bu satır bu ok" diye tahtada eşle. Labda sorun olursa lab sorumlu hocası yerel `dot` ile üretir. |
| ATM çizimi 3 dakikada bitiyor, çoğu benzer | Ek soru: "Üçüncü yanlışta kart yutuluyor; ikinci yanlıştan sonra doğru girilirse sayaç sıfırlanmalı mı? Diyagramınız ne diyor?" ve "Günlük limit tek işlem için mi, günün toplamı için mi? Diyagramınız hangisini çiziyor?" |
| Hata avında sınıf mantık hatasını bulamıyor | Beklenen durum; bulamamaları dersin tezi. "Satır 9'u elle hesaplayın: 245 / 3 kaç?" deyip 81 dedirt; sonra "double'a koyunca 81.0; bu doğru mu?" |
| Hata avında birisi hepsini 30 saniyede buluyor | Onu Lab 2'de hata avı için "ikinci göz" ilan et; ek soru: "Satır 12'yi düzeltmeden satır 10'daki çökmeyi görebilir misiniz?" (Hayır; derleyici izin vermez.) |
| Poll Everywhere çalışmıyor | El kaldırma; Poll 2 için "55 diyen el kaldırsın", Poll 4 için üç şıkkı tahtaya yaz, el say. |
| Süre taşıyor | Kesilecek sıra: YZ anı (siteye bırak; labda zaten sarı bölge kutusu var) → Sahadan örnekler (siteye bırak) → Örnek 3'ün değişken varyasyonları kısaltılır → Kantin yalnızca diyagram gösterilir, sözde kod siteye bırakılır. ATM bulmacası, üç yapı ve hata avı **kesilmez**. |
| B şubesi öğle sonrası, enerji düşük | ATM bulmacasına 2 dk fazla ver; Örnek 1'i hızlı geç (geçen haftanın kodu); hata avını 3 yerine 4 dakika yap, yarışma havası ver. |

## B şubesi (13.15)

Aynı akış, aynı dakikalar (13.30 başla, 14.30-14.45 bitir). A şubesinden not: ATM çizimlerinde en sık hangi hata çıktı (çok bitiş? etiketsiz ok?), hata avında hangi hata en geç bulundu, Poll 2'de 55 yüzdesi. B'de o noktaya iki cümle fazla ayır. Poll sonuçlarının ekran görüntüsünü iki şube için ayrı al.

## Ders sonrası (5 dk)

- ATM çizimlerinden iyi bir öğrenci örneğinin fotoğrafı (izinle) → 3. hafta sayfasına "geçen haftadan" görseli.
- Hata avında en geç bulunan hata → Lab 2 `Hatali3.java` için lab sorumlu hocasına not: öğrenciler orada takılacak.
- Poll 5'ten 2-3 cümle → 3. haftanın açılışında oku.
- Graphviz Online'da takılan nokta (Format menüsü, PNG kaydetme) → Lab 2 sayfasına ek not gerekiyorsa ekle.
