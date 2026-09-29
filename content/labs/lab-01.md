---
week: 1
title: "Lab 1 · Araç Çantası: GitHub, JDK ve İlk Java Dosyası"
description: "GitHub hesabı ve ders organizasyonu, Classroom 50 ile lab deposunu alma, JDK ve VS Code kurulum kontrolü (ya da Codespaces), Merhaba.java'yı komut satırında derleyip çalıştırma ve beş küçük görev."
status: hazir
objectives:
  - "GitHub hesabıyla ders organizasyonuna katılır ve Classroom 50 kabul bağlantısıyla Lab 1 deposunu alır."
  - "Kendi bilgisayarında JDK ve VS Code'un çalıştığını doğrular ya da Codespaces ortamını açar."
  - "Merhaba.java dosyasını javac ile derleyip java ile çalıştırır; derleyici hatasını okuyup düzeltir."
  - "println, değişken ve basit aritmetikle beş küçük program yazar, lab deposuna push eder ve otomatik kontrol sonucunu okur."
tools:
  - "GitHub"
  - "Classroom 50"
  - "JDK 21"
  - "VS Code"
  - "GitHub Codespaces"
  - "Git"
deliverable: "Lab 1 deposu (algo1-lab01-KULLANICIADI) kök dizininde Merhaba.java ve beş görev dosyası (bonus isteğe bağlı); son teslim 2 Ekim 2026 Cuma 23.59."
---

## Ne zaman, nerede, kiminle

| Şube | Tarih | Saat | Yürütücü |
|---|---|---|---|
| A | 30 Eylül 2026 Çarşamba | 13.15 | Arş. Gör. Ömer Miraç Kökçam |
| B | 1 Ekim 2026 Perşembe | 15.15 | Arş. Gör. Ömer Miraç Kökçam |

Laboratuvar teoriden bir hafta sonra yapılır: bugün 1. haftanın (25 Eylül) konularını uyguluyoruz. Kendi bilgisayarınızı getirebilirsiniz; getirmeyenler lab bilgisayarı ya da tarayıcıda Codespaces kullanır.

> [!not] Lab 1 kabul bağlantısı
> Ödevler **Classroom 50** üzerinden dağıtılır. Organizasyon davetini kabul ettikten sonra şu bağlantıya tıklayıp **Accept assignment** deyin:
> **[classroom50.org/FiratUniversity-FerhatUcarsLAB/algo1/assignments/lab01/accept](https://classroom50.org/FiratUniversity-FerhatUcarsLAB/algo1/assignments/lab01/accept)**
> Deponuz `algo1-lab01-KULLANICIADI` adıyla oluşur. Bağlantı, organizasyona davet edilmemiş hesaplarda çalışmaz; sırayı Adım 0'da izleyin. Ayrıntı: [Classroom 50 rehberi](/rehber/classroom-50).

> [!uyari] Yapay zeka: Sarı bölge
> Laboratuvarda yapay zekaya **soru sorabilirsiniz** ("javac komutu tanınmıyor ne demek?"), ama **kod kopyalayamazsınız**. Lab sorumlu hocanız istediğinde ekranınızı görebilir. Sebep basit: takıldığınız yeri kendiniz çözmezseniz sınavda aynı yerde takılırsınız.

## Adım 0 · GitHub hesabı, organizasyon daveti ve lab deposu (10 dk)

1. **GitHub hesabı.** [github.com](https://github.com) hesabınız yoksa şimdi açın; üniversite e-postanızı kullanın (öğrenci paketi için gerekecek). E-posta doğrulamasını yapın.
2. **Kullanıcı adınızı bildirin.** GitHub kullanıcı adınızı (ya da üniversite e-postanızı) lab sorumlu hocanıza yazdırın. Dönem başında verilen listeyle davet aldıysanız bu adımı atlayın.
3. **Daveti kabul edin.** Birkaç dakika içinde e-postanıza ve GitHub bildirimlerinize "FiratUniversity-FerhatUcarsLAB organizasyonuna davet" gelir; **Accept** deyin. Bildirim gelmediyse [github.com/FiratUniversity-FerhatUcarsLAB](https://github.com/FiratUniversity-FerhatUcarsLAB) adresini açın; üstte **View invitation** düğmesi görünür.
4. **Ödevi kabul edin.** Yukarıdaki kutudaki kabul bağlantısına tıklayın, **Accept assignment** deyin. Sayfa "Not a member yet" diyorsa davet henüz kabul edilmemiştir; 3. adımı yapıp **Check again** deyin.
5. Birkaç saniye içinde `algo1-lab01-KULLANICIADI` adlı **özel (private)** deponuz organizasyon içinde oluşur; sayfadaki bağlantıyla açın. Depoyu **yeniden adlandırmayın** ve **Actions**'ı kapatmayın; otomatik kontrol bunlara bağlı.

Portfolyo (dönem projesi) deposu için şimdi bir şey yapmanız gerekmiyor; o depo da ilerleyen haftalarda aynı yöntemle, ayrı bir bağlantıyla verilecek. Ayrıntılı anlatım: [GitHub ve Codespaces rehberi](/rehber/github-ve-codespaces), [Classroom 50 rehberi](/rehber/classroom-50).

## Adım 1 · Ortam kontrolü (10 dk)

İki yoldan **birini** seçin.

**Yol A: Kendi bilgisayarım.** Terminal (macOS) ya da Komut İstemi / PowerShell (Windows) açın:

```bash
java -version
javac -version
```

İkisi de `21` ya da üzeri bir sürüm yazıyorsa hazırsınız. Yazmıyorsa [JDK ve VS Code rehberindeki](/rehber/yerel-jdk-vscode) adımları izleyin; 10 dakikada olmuyorsa Yol B'ye geçin, kurulumu evde bitirin. Sonra depoyu bilgisayarınıza indirin:

```bash
git clone https://github.com/FiratUniversity-FerhatUcarsLAB/algo1-lab01-KULLANICIADI.git
cd algo1-lab01-KULLANICIADI
```

**Yol B: Codespaces.** GitHub'da `algo1-lab01-KULLANICIADI` deposunu açın → **Code** → **Codespaces** → **Create codespace on main**. Tarayıcıda VS Code açılır; terminalde `java -version` yazın. Java hazır gelir. Ayda 60 saat ücretsiz; lab için fazlasıyla yeter.

## Adım 2 · Merhaba.java: derle ve çalıştır (15 dk)

Dosyaları deponun **kök dizinine** koyun (README ve .gitignore'un yanına); alt klasör açmayın, otomatik kontrol dosyaları kökte arar. `Merhaba.java` adında dosya oluşturun. Dikkat: dosya adı ile sınıf adı **birebir aynı** olmalı, büyük harf dahil.

```java
public class Merhaba {
    public static void main(String[] args) {
        String isim = "Adınız";
        System.out.println("Merhaba, " + isim + "!");
        System.out.println("Bu benim ilk Java dosyam.");
    }
}
```

Terminalde deponun kök dizinindeyken:

```bash
javac Merhaba.java
java Merhaba
```

İlk komut `Merhaba.class` dosyasını üretir (bytecode), ikincisi onu çalıştırır. `java Merhaba.class` **yazmayın**; uzantısız. `.class` dosyaları `.gitignore` sayesinde depoya girmez; yalnızca `.java` dosyalarınız push edilir.

Derste Playground'da yazmadığımız `public class` ve `main` satırları burada zorunlu. Şimdilik şöyle düşünün: `class` programın adı, `main` programın kapısı. Java bir programı çalıştırırken hep `main`'den başlar. Ayrıntısı 2. haftada.

> [!ornek] Bilerek hata yapın
> Bir noktalı virgülü silin, `javac` çalıştırın. Mesajı okuyun: hangi satır, ne bekliyor? Geri koyun. Sonra sınıf adını `merhaba` yapın (küçük harf) ve tekrar deneyin. Bu iki hata, dönem boyunca en çok göreceğiniz iki hata.

## Adım 3 · Beş küçük görev (40 dk)

Her görev ayrı bir `.java` dosyası; her dosyada bir `public class` ve bir `main`. Dosya adları aşağıdaki gibi **birebir** olmalı; otomatik kontrol bu adlara ve gösterilen çıktı satırlarına bakar. Kodu Playground'da deneyip dosyaya taşıyabilirsiniz. **Önce çıktıyı tahmin edin, sonra çalıştırın.**

### Görev 1 · Hoş geldin mesajları (`UcMesaj.java`)

Üç ayrı `println` ile: adınız ve bölümünüz, bu dersi neden aldığınız (bir cümle), bugünün tarihi. Sonra aynı üç satırı `print` ile yazdırıp farkı görün (`\n` kullanmadan neden tek satıra yığılıyor?).

### Görev 2 · Matematiksel işlemler (`IkiIslem.java`)

İki `int` değişken tanımlayın: `a = 17`, `b = 5`. Bu değerleri değiştirmeyin; otomatik kontrol çıktıda `17 % 5 = 2` satırını arar. Toplamı, farkı, çarpımı, bölümü ve kalanı **etiketleriyle** yazdırın:

```
17 + 5 = 22
17 / 5 = 3
17 % 5 = 2
```

Sonra `b`'yi `double` yapan bir deneme yapın ve bölümün nasıl değiştiğini yorum satırına (`//`) not edin; teslim ettiğiniz dosyada `a` ve `b` yine `int` ve 17, 5 olsun.

### Görev 3 · Geometrik hesap (`DaireHesap.java`)

Yarıçapı `double yaricap = 3.5;` olan dairenin çevresini ve alanını hesaplayıp yazdırın. `Math.PI` kullanın. Otomatik kontrol çıktıda alan için `38.48` arar: `System.out.printf("Alan: %.2f%n", alan)` ile iki basamak yazdırabilirsiniz ya da `println` ile olduğu gibi (38.48451000647496) bırakabilirsiniz; ikisi de geçer, yeter ki `38.48` görünsün. Bonus: `Math.pow(yaricap, 2)` ile `yaricap * yaricap` aynı sonucu veriyor mu?

### Görev 4 · İsim kartı (`IsimKarti.java`)

Yalnızca `println` ve `+` ile bir çerçeve çizin:

```
+--------------------+
|  Ayşe Yılmaz       |
|  Yazılım Müh. 1    |
+--------------------+
```

İpucu: `"-".repeat(20)` yazarsanız 20 tire üretir. Adınız çerçeveye sığmazsa ne olur?

### Görev 5 · Tablo deseni (`CarpimTablosu.java`)

1. haftanın `for` döngüsünü kullanarak 5'in çarpım tablosunu yazdırın. Satır biçimi birebir `5 x 10 = 50` gibi olmalı (küçük `x`, boşluklar dahil); otomatik kontrol bu satırı arar:

```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

Zorlaması: tabloyu `1`'den `10`'a değil, `10`'dan `1`'e yazdırın (döngüde neyi değiştirdiniz? `5 x 10 = 50` satırı yine çıktıda olmalı).

### Bonus · Saat dönüştürme (`SaatDonusturme.java`)

`int toplamSaniye = 7384;` değerini saat, dakika ve saniyeye çevirin ve tam olarak `2 saat 3 dakika 4 saniye` yazdırın. Yalnızca `/` ve `%` ile. Bonus 10 puan; yapmazsanız eksik sayılmaz.

## Adım 4 · Teslim (10 dk)

Terminalde (kendi bilgisayarınızda ya da Codespaces'te), deponun kök dizininde:

```bash
git add .
git commit -m "Lab 1: ilk Java dosyaları"
git push
```

Codespaces'te sol çubuktaki **Source Control** düğmesi aynı üç adımı tıklamayla yapar: mesajı yazın, **Commit**, sonra **Sync Changes**. Git komutlarını ilk kez görüyorsanız [rehberdeki](/rehber/github-ve-codespaces) üç satırlık özete bakın.

Push'tan sonra:

1. Tarayıcıda deponuzu yenileyin; `.java` dosyaları kökte görünmeli.
2. 1-2 dakika bekleyip deponun **Releases** sayfasına bakın: otomatik kontrol her push'ta çalışır ve hangi testin geçtiğini, puanınızı orada listeler. Aynı sonuç depoda açılan **Feedback** pull request'inde de görünür; lab sorumlu hocanız yorumlarını oraya yazabilir.
3. Geçmeyen test varsa dosyayı düzeltin, tekrar commit ve push edin. Son teslim saatine kadar istediğiniz kadar push edebilirsiniz; en son push geçerlidir.

**Son teslim: 2 Ekim 2026 Cuma 23.59.** Lab saatinde bitiremeyenler o saate kadar evden push edebilir.

> [!not] İki puan, iki bakış
> Otomatik kontrol (100 puan) yalnızca dosyaların derlenip derlenmediğine ve birkaç çıktı satırına bakar: `Merhaba` derleniyor mu (20), çıktısında "Merhaba" geçiyor mu (10), `UcMesaj` derleniyor mu (10), `17 % 5 = 2` (10), `38.48` (10), `IsimKarti` derleniyor mu (10), `5 x 10 = 50` (20), bonus `2 saat 3 dakika 4 saniye` (10). Kodun okunabilirliği, isimlendirme ve aşağıdaki "30 saniye anlat" ritüeli lab sorumlu hocanızın değerlendirmesidir; ikisi birlikte lab notunuzu oluşturur.

> [!not] Teslim ritüeli: lab sorumlu hocanıza 30 saniye anlatın
> Push ettikten sonra lab sorumlu hocanızı çağırın ve görevlerden **birini** 30 saniyede anlatın: ne yapıyor, en çok nerede takıldınız, hata mesajı ne dedi. Anlatamadığınız kod sizin değildir; bu ritüel her lab'da tekrar edecek.

## Bitiremediyseniz

Sorun değil. Lab'da Adım 0'ı (depo açıldı) ve Adım 2'yi (Merhaba.java derle-çalıştır, ilk push) tamamlamış olmanız yeterli; kalan görevleri **2 Ekim Cuma 23.59**'a kadar evde bitirip push edin, Releases sayfasından sonucu görün. Cuma'dan sonra gelen push'lar puanlanmaz. Kurulum takıldıysa Codespaces ile devam edin ya da ofis saatine gelin.
