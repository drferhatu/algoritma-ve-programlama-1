# Hafta 10 · Poll Everywhere soru seti (27 Kasım; metotlar II)

Öğretim üyesi notu (siteye girmez). Ders 60 dakikalık shot akışıyla, yedi kapsülle işleniyor (`docs/hafta-10-ders-senaryosu.md`); sorular akışa göre yerleşti: açılış hikayesi → bulmaca (takas) → 1. kapsül (kapsam) → 5. kapsül (aşırı yükleme) → kapanış. Toplam 5 soru (kapanış iki parçalı); ★ işaretliler en etkilileri. Her iki şubede aynı set; sonuçları ayrı kaydet. Bütün çıktılar `content/weeks/hafta-10.mdx` içindeki kodlarla aynıdır.

---

## Açılış hikayesi (Linus'un ilk sürümünün on bin satır kadar olduğu söylendikten sonra, bugünkü boyutu söylemeden hemen önce, 3. dk)

**1. Çoktan seçmeli: 1991'de bir öğrencinin "sadece bir hobi" diye duyurduğu ve ilk sürümü on bin satır kadar olan Linux çekirdeği bugün yaklaşık kaç satır?**
Tür: Multiple Choice · Tek seçim · Sonuç hemen açık (ısınma)
- 100 bin
- 1 milyon
- 5 milyon
- 30 milyondan fazla
Not: Dördüncü şık doğru. Bu soru bilgi ölçmüyor, ölçeği hissettiriyor. Oylamayı bugünkü boyutu söylemeden **önce** aç; sonuç ekrandayken "otuz milyonu aşkın" de ve hemen ekle: "Ama otuz milyon satır, otuz milyon satır olarak yazılmadı." Küçük sayıları seçenlere dön: "Bir öğrenci projesi için bu tahmin çok makul; Linus da öyle düşünmüştü." Ardından Android'i, süper bilgisayarları ve `git push`'u say; portfolyoya bağla: KT1 tek bir `if` idi, bu gece dönen bir menü.

## Bulmaca (takas kodu yansıtılıp iki dakikalık sessiz çalışma bittikten sonra, Run'dan önce, 6. dk)

**2. ★ Çoktan seçmeli: Bu programın yazdığı ikinci satır hangisidir?**
```java
static void takas(int a, int b) {
    int gecici = a;
    a = b;
    b = gecici;
    System.out.println("takas icinde: " + a + " " + b);
}

public static void main(String[] args) {
    int x = 3;
    int y = 7;
    takas(x, y);
    System.out.println("main icinde: " + x + " " + y);
}
```
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce kağıtta izle, sonra oyla, sonra Run)
- main icinde: 3 7
- main icinde: 7 3
- main icinde: 7 7
- main icinde: 3 3
Not: Birinci şık doğru. İlk satır `takas icinde: 7 3`, ikinci satır `main icinde: 3 7`. "7 3" diyenler **metodun `x` ve `y`'yi değiştirdiğini** düşünüyor; geçen haftanın "6 7" yanılgısının aynısı ve dersin ilk yarısının hedefi tam bu grup. Bu yüzdeyi geçen haftaki Poll 3'ün "6 7" yüzdesiyle yan yana söyle; sayıyı kayıttan oku, ezberden söyleme. "7 7" ya da "3 3" diyenler takasın kendisini karıştırıyor, yani üçüncü haftanın `gecici` kutusunu hatırlamıyor; 30 saniyede tahtada üç satırı iki bardakla yeniden izlet ve geç. **Önemli:** Run'dan sonra nedenini açıklama. "Üç satır aynı üç satır; yine de iş görmüyor. Cevabı üçüncü kapsülde resmin üstünde göstereceksiniz" de ve tartışmayı bilerek açık bırak; 3. kapsülde yığın diyagramı çizildikten sonra bu sonucu yeniden yansıt.

## 1. kapsül, kapsam (rol canlandırmasından sonra, "İki ayrı toplam" kutusu yansıtılmış ama Run edilmeden önce, 11. dk)

**3. Çoktan seçmeli: Program ikinci satırda `main'deki toplam:` yazısının yanına hangi sayıyı yazar?**
```java
static double ortalama(int a, int b) {
    int toplam = a + b;
    return toplam / 2.0;
}

public static void main(String[] args) {
    int toplam = 100;
    double sonuc = ortalama(70, 85);
    System.out.println("Ortalama: " + sonuc);
    System.out.println("main'deki toplam: " + toplam);
}
```
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra Run)
- 100
- 155
- 255
- Program derlenmez; toplam iki kez tanımlanmış
Not: Birinci şık doğru: Çıktı `Ortalama: 77.5` ve `main'deki toplam: 100`. "155" diyenler iki `toplam`'ı **tek kutu** sanıyor; rol canlandırmasındaki iki kağıdı yeniden havaya kaldır: "main'in kağıdına kim yazdı?" "255" diyenler de tek kutu görüyor, üstelik atamayı üstüne ekleme sanıyor; `int toplam = a + b;` satırının **yeni bir kutu açtığını** söyle. "Derlenmez" diyenler makul bir sezgiyle geliyor: Aynı metodun içinde iki `toplam` gerçekten derlenmezdi. Bunu söyle ve tebrik et; sonra ayrımı koy: iki ayrı oda, iki ayrı Ayşe. Ardından `main`'e `System.out.println(a);` ekleyip gerçek derleme hatasını (`cannot find symbol`) göster: Derleyici ad çakışmasına değil, **odada olmayan** ada itiraz ediyor.

## 5. kapsül, aşırı yükleme ("Üç enBuyuk" kutusunun ilk üç çağrısı çalıştırılıp `9`, `9`, `4.5` görüldükten sonra, dördüncü çağrıdan önce, 39. dk)

**4. ★ Çoktan seçmeli: `System.out.println(enBuyuk(4, 2.5));` satırı ekrana ne yazar?**
```java
static int enBuyuk(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

static int enBuyuk(int a, int b, int c) {
    return enBuyuk(enBuyuk(a, b), c);
}

static double enBuyuk(double a, double b) {
    if (a > b) {
        return a;
    }
    return b;
}
```
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra Run)
- 4
- 4.0
- 2.5
- Derleme hatası
Not: İkinci şık doğru. Tam uyan bir sürüm yok; Java 4'ü 4.0'a genişletip `double` sürümünü seçer ve cevap `double` olarak, `4.0` biçiminde döner. "4" diyenler büyük olanı doğru buluyor ama **hangi sürümün çalıştığını** kaçırıyor: "Cevap doğru, tipi yanlış; ekrandaki `.0` size hangi metodun çalıştığını söylüyor." Bu grup büyükse mülakat kartını atlama. "2.5" diyenler Java'nın 2.5'i tam sayıya indirip `int` sürümünü çağıracağını ya da karşılaştırmanın ters çalışacağını düşünüyor; üçüncü haftayı hatırlat: Java kendiliğinden yalnızca **genişletir**, daraltmaz; bardaklar arası su boşaltma örneği. "Derleme hatası" diyenler "tam uyan imza yoksa çağrı geçersizdir" diye düşünüyor; iyi bir titizlik, ama geçen haftanın `bolum(10, 4)` çağrısında da `int` argümanlar `double` parametreye gitmişti. Ardından gerçek bir derleme hatası göster: `static double enBuyuk(int a, int b)` ekle ve "already defined" mesajını okut; dönüş tipi imzanın parçası değil.

## Kapanış (7. kapsül bittikten sonra, kapanış duyurularından önce, 56. dk)

**5a. Çoktan seçmeli (çoklu seçim): Bugün hangi kapsül hâlâ bulanık? En fazla iki tane seçin.**
Tür: Multiple Choice · Çoklu seçim (en fazla 2) · Sonuç hemen açık
- 1 Kapsam: her metodun kendi odası
- 2 Yığın diyagramı: her çağrıya bir kağıt
- 3 Kopya gider, asıl kalır (pass by value)
- 4 Yığın izini okumak
- 5 Aşırı yükleme
- 6 Artımlı geliştirme
- 7 Menü seçeneğini metoda taşımak
- Hiçbiri, hepsi net
Not: En çok işaretlenen iki kapsülü yüksek sesle söyle. 2. ya da 3. kapsül yüksek çıkarsa beklenen bir şey: "Lab 10'un ilk görevi tam bu; dört programı kağıtta izleyeceksiniz, kağıt kalem getirin." Sonucu lab sorumlu hocasına ilet. 7. kapsül yüksek çıkarsa sakinleştir: "Bu gece şart değil; KT3'e üç hafta var ve her hafta tek bir `case` taşıyacağız." 5. kapsül yüksek çıkarsa ve mülakat kartı zaman yüzünden eve kaldıysa, 11. haftanın açılışında dört çağrılı izlemeyi iki dakikada yap. 6. kapsül yüksek çıkarsa Lab 10'un Görev 4'ünü işaret et: üç metot, sırayla.

**5b. ★ Açık uçlu: Bu gece KT2'yi göndermenin önündeki tek engel ne? Engel yoksa "hazırım" yazın.**
Tür: Open-Ended (Text Wall) · Anonim
Not: Bu duvar akşam atacağın mesajı belirliyor; 23.59'dan önce oku ve kümelere ayır. "Derlenmiyor / hata veriyor": Kapanışta tek cümle söyle: "Yığın izini ya da derleme hatasını bugün öğrendiğiniz gibi okuyun; ilk satır ne olduğunu, satır numarası nerede olduğunu söylüyor." "Menüden çıkamıyorum / sonsuz döngü": Döngü koşulunu ve `0` gözcüsünü işaret et (yedinci haftanın menü döngüsü). "Girdi doğrulama ne demek / nerede olmalı": 7. kapsüldeki `adetOku`'nun içindeki `while` tam olarak o; metot hali şart değil, döngünün kendisi şart. "Push edemiyorum / depom yok": Ders çıkışında yanına çağır ya da lab sorumlu hocasına yönlendir; bu akşam çözülmesi gereken tek küme bu. "Hiç başlamadım": Yargılama; "bu gece çalışan en küçük menüyü gönderin: üç seçenek, `0` ile çıkış, bir doğrulama döngüsü. Linus'un ilk sürümü de pek bir işe yaramıyordu." "Hazırım" yüzdesini iki şube için ayrı kaydet; KT2 teslim sayısıyla karşılaştırmak için işe yarar.

---

### Kurulum ipuçları

- 2., 3. ve 4. sorularda "Show results" kapalı başlasın; önce oy, sonra Run, sonra sonuç. 1. ve 5a soruları sonuç açık.
- 2., 3. ve 4. sorulardaki kod bloklarını Poll Everywhere'e görsel olarak ekle (metin olarak girilirse girintiler bozulur).
- 2. soruyu bulmaca için verilen iki dakika **bittikten sonra** aç; soru açıkken kağıtta çalışmasınlar, cevaplarını işaretlesinler. Sonucu 3. kapsülde, yığın diyagramı çizildikten sonra bir kez daha yansıtmak üzere sekmede açık tut.
- 4. soruyu ilk üç çağrı çalıştırıldıktan sonra aç; dördüncü `println` satırı Run edilmeden önce yansıda görünsün ama çıktısı görünmesin (satırı geçici olarak yoruma al).
- 5a'da çoklu seçim açık ve "en fazla 2 seçim" sınırı konmuş olsun; 5b'de küfür filtresini aç.
- 2. sorunun "7 3", 3. sorunun "155" ve 4. sorunun "4" ile "derleme hatası" yüzdelerini iki şube için ayrı kaydet; hepsini lab sorumlu hocasına ilet.
- Geçen haftanın Poll 3 sonucunu ("6 7" yüzdesi) derse girmeden önce her iki şube için ayrı ayrı bir kağıda yaz; 2. soruyla karşılaştırırken kullanılacak.
- İnternet yoksa: Şıkları tahtaya yaz, el kaldırt, sayıları senaryo belgesinin kenarına not et; 5b'yi küçük kağıtlara yazdırıp çıkışta topla.
