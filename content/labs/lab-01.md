---
week: 1
title: "Lab 1 · Araç Çantası: GitHub, JDK ve İlk Java Dosyası"
description: "GitHub hesabı ve ders organizasyonu, JDK ve VS Code kurulum kontrolü (ya da Codespaces), Merhaba.java'yı komut satırında derleyip çalıştırma ve beş küçük görev."
status: hazir
objectives:
  - "GitHub hesabıyla ders organizasyonuna katılır ve portfolyo deposunu oluşturur."
  - "Kendi bilgisayarında JDK ve VS Code'un çalıştığını doğrular ya da Codespaces ortamını açar."
  - "Merhaba.java dosyasını javac ile derleyip java ile çalıştırır; derleyici hatasını okuyup düzeltir."
  - "println, değişken ve basit aritmetikle beş küçük program yazar ve lab01/ klasörüne push eder."
tools:
  - "GitHub"
  - "JDK 21"
  - "VS Code"
  - "GitHub Codespaces"
  - "Git"
deliverable: "Portfolyo deposunda lab01/ klasörü: Merhaba.java ve beş görev dosyası, lab bitmeden push edilmiş."
---

## Ne zaman, nerede, kiminle

| Şube | Tarih | Saat | Yürütücü |
|---|---|---|---|
| A | 30 Eylül 2026 Çarşamba | 13.15 | Arş. Gör. Ömer Miraç Kökçam |
| B | 1 Ekim 2026 Perşembe | 15.15 | Arş. Gör. Ömer Miraç Kökçam |

Laboratuvar teoriden bir hafta sonra yapılır: bugün 1. haftanın (25 Eylül) konularını uyguluyoruz. Kendi bilgisayarınızı getirebilirsiniz; getirmeyenler lab bilgisayarı ya da tarayıcıda Codespaces kullanır.

> [!uyari] Yapay zeka: Sarı bölge
> Laboratuvarda yapay zekaya **soru sorabilirsiniz** ("javac komutu tanınmıyor ne demek?"), ama **kod kopyalayamazsınız**. Lab sorumlu hocanız istediğinde ekranınızı görebilir. Sebep basit: takıldığınız yeri kendiniz çözmezseniz sınavda aynı yerde takılırsınız.

## Adım 0 · GitHub hesabı ve ders organizasyonu (10 dk)

1. [github.com](https://github.com) hesabınız yoksa şimdi açın; üniversite e-postanızı kullanın (öğrenci paketi için gerekecek).
2. Ders organizasyonuna katılım bağlantısı lab sırasında verilecek (bağlantı sonra eklenecek). Bağlantıya tıklayıp daveti kabul edin.
3. Portfolyo deponuzu oluşturun: **New repository**, ad `algo1-portfolyo`, **Public**, "Add a README" işaretli. Bu depo dönem boyunca tek deponuz olacak; KT1'den KT4'e her şey buraya girer.
4. Kullanıcı adınızı lab sorumlu hocanıza listeye yazdırın.

Ayrıntılı anlatım: [GitHub ve Codespaces rehberi](/rehber/github-ve-codespaces).

## Adım 1 · Ortam kontrolü (10 dk)

İki yoldan **birini** seçin.

**Yol A: Kendi bilgisayarım.** Terminal (macOS) ya da Komut İstemi / PowerShell (Windows) açın:

```bash
java -version
javac -version
```

İkisi de `21` ya da üzeri bir sürüm yazıyorsa hazırsınız. Yazmıyorsa [JDK ve VS Code rehberindeki](/rehber/yerel-jdk-vscode) adımları izleyin; 10 dakikada olmuyorsa Yol B'ye geçin, kurulumu evde bitirin.

**Yol B: Codespaces.** GitHub'da `algo1-portfolyo` deposunu açın → **Code** → **Codespaces** → **Create codespace on main**. Tarayıcıda VS Code açılır; terminalde `java -version` yazın. Java hazır gelir. Ayda 60 saat ücretsiz; lab için fazlasıyla yeter.

## Adım 2 · Merhaba.java: derle ve çalıştır (15 dk)

Deponuzun içinde `lab01` klasörü açın; içine `Merhaba.java` adında dosya oluşturun. Dikkat: dosya adı ile sınıf adı **birebir aynı** olmalı, büyük harf dahil.

```java
public class Merhaba {
    public static void main(String[] args) {
        String isim = "Adınız";
        System.out.println("Merhaba, " + isim + "!");
        System.out.println("Bu benim ilk Java dosyam.");
    }
}
```

Terminalde `lab01` klasörüne girin ve:

```bash
javac Merhaba.java
java Merhaba
```

İlk komut `Merhaba.class` dosyasını üretir (bytecode), ikincisi onu çalıştırır. `java Merhaba.class` **yazmayın**; uzantısız.

Derste Playground'da yazmadığımız `public class` ve `main` satırları burada zorunlu. Şimdilik şöyle düşünün: `class` programın adı, `main` programın kapısı. Java bir programı çalıştırırken hep `main`'den başlar. Ayrıntısı 2. haftada.

> [!ornek] Bilerek hata yapın
> Bir noktalı virgülü silin, `javac` çalıştırın. Mesajı okuyun: hangi satır, ne bekliyor? Geri koyun. Sonra sınıf adını `merhaba` yapın (küçük harf) ve tekrar deneyin. Bu iki hata, dönem boyunca en çok göreceğiniz iki hata.

## Adım 3 · Beş küçük görev (40 dk)

Her görev ayrı bir `.java` dosyası; her dosyada bir `public class` ve bir `main`. Kodu Playground'da deneyip dosyaya taşıyabilirsiniz. **Önce çıktıyı tahmin edin, sonra çalıştırın.**

### Görev 1 · Hoş geldin mesajları (`UcMesaj.java`)

Üç ayrı `println` ile: adınız ve bölümünüz, bu dersi neden aldığınız (bir cümle), bugünün tarihi. Sonra aynı üç satırı `print` ile yazdırıp farkı görün (`\n` kullanmadan neden tek satıra yığılıyor?).

### Görev 2 · Matematiksel işlemler (`IkiIslem.java`)

İki `int` değişken tanımlayın (ör. `a = 17`, `b = 5`). Toplamı, farkı, çarpımı, bölümü ve kalanı **etiketleriyle** yazdırın:

```
17 + 5 = 22
17 / 5 = 3
17 % 5 = 2
```

Sonra `b`'yi `double` yapın ve bölümün nasıl değiştiğini not olarak yorum satırına (`//`) yazın.

### Görev 3 · Geometrik hesap (`DaireHesap.java`)

Yarıçapı `double yaricap = 3.5;` olan dairenin çevresini ve alanını hesaplayıp yazdırın. `Math.PI` kullanın. Bonus: `Math.pow(yaricap, 2)` ile `yaricap * yaricap` aynı sonucu veriyor mu?

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

1. haftanın `for` döngüsünü kullanarak 5'in çarpım tablosunu yazdırın:

```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

Zorlaması: tabloyu `1`'den `10`'a değil, `10`'dan `1`'e yazdırın (döngüde neyi değiştirdiniz?).

### Bonus · Saat dönüştürme (`SaatDonusturme.java`)

`int toplamSaniye = 7384;` değerini saat, dakika ve saniyeye çevirin: `2 saat 3 dakika 4 saniye`. Yalnızca `/` ve `%` ile.

## Adım 4 · Teslim (10 dk)

Terminalde (kendi bilgisayarınızda ya da Codespaces'te):

```bash
git add lab01
git commit -m "Lab 1: ilk Java dosyaları"
git push
```

Tarayıcıda deponuzu yenileyin; `lab01/` klasörü ve dosyalar görünmeli. Git komutlarını ilk kez görüyorsanız [rehberdeki](/rehber/github-ve-codespaces) üç satırlık özete bakın; Codespaces'te sol menüdeki kaynak kontrol simgesi aynı işi düğmeyle yapar.

> [!not] Teslim ritüeli: lab sorumlu hocanıza 30 saniye anlatın
> Push ettikten sonra lab sorumlu hocanızı çağırın ve görevlerden **birini** 30 saniyede anlatın: ne yapıyor, en çok nerede takıldınız, hata mesajı ne dedi. Anlatamadığınız kod sizin değildir; bu ritüel her lab'da tekrar edecek.

## Bitiremediyseniz

Sorun değil. Adım 2'yi (Merhaba.java derle-çalıştır) lab'da tamamlamış olmanız yeterli; kalan görevleri gelecek lab'a kadar evde bitirip push edin. Kurulum takıldıysa ofis saatine gelin ya da Codespaces ile devam edin.
