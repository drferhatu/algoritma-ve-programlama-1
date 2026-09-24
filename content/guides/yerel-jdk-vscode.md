---
title: "Kendi Bilgisayarında Java: JDK ve VS Code"
description: "Windows ve macOS için JDK 21 LTS kurulumu, PATH ayarı, VS Code ve Extension Pack for Java, javac/java komutları ve en sık karşılaşılan hatalar."
order: 2
icon: "☕"
---

## Neden yerel kurulum?

Playground derste yeter, Codespaces lab'da yeter. Ama kendi bilgisayarınızda Java'nın çalışması sizi internetten ve kotalardan bağımsız kılar; portfolyo üzerinde evde rahat çalışırsınız. Kurulum bir kez yapılır, 15-20 dakika sürer.

> [!not] Takılırsanız
> Hata mesajının ekran görüntüsünü alıp bir yapay zeka asistanına "bu adımda ne yapmalıyım?" diye sormak çoğu zaman yeterlidir. Olmazsa laboratuvarda asistana ya da ofis saatinde bana getirin. Kurulum bitene kadar Codespaces ile devam edin; kimse geride kalmaz.

## Adım 1 · JDK 21'i kur

**JDK** (Java Development Kit): derleyici (`javac`), çalıştırıcı (`java`) ve kütüphaneler. Sürüm olarak **21 LTS** kullanıyoruz (uzun süreli destek). Daha yenisi de olur; 17'den eski olmasın.

İndirme: [adoptium.net](https://adoptium.net/) (Eclipse Temurin, ücretsiz, hesap istemez). Alternatif: [Oracle JDK](https://www.oracle.com/java/technologies/downloads/).

### Windows

1. Adoptium'dan **Windows x64 .msi** dosyasını indirip çalıştırın.
2. Kurulum ekranında **"Add to PATH"** ve **"Set JAVA_HOME variable"** seçeneklerini **etkin** yapın (varsayılan olarak kapalı gelebilir; tıklayıp "Will be installed on local hard drive" seçin).
3. Kurulum bitince açık olan bütün terminal pencerelerini kapatıp yeniden açın.

### macOS

1. Çipinize göre indirin: Apple Silicon (M1/M2/M3/M4) için **aarch64**, Intel için **x64**. Emin değilseniz sol üst  → Bu Mac Hakkında → "Çip".
2. `.pkg` dosyasını çalıştırın, varsayılanlarla ilerleyin. PATH kendiliğinden ayarlanır.
3. Terminal'i kapatıp yeniden açın.

### Kontrol

```bash
java -version
javac -version
```

İkisi de `21.x` gibi bir sürüm yazmalı. `javac` yazmıyorsa yalnızca JRE kurulmuş demektir; JDK'yi kurun.

## Adım 2 · PATH nedir, neden bozulur?

Terminale `javac` yazdığınızda işletim sistemi bu programı **PATH** adlı klasör listesinde arar. JDK'nin `bin` klasörü listede yoksa "komut tanınmıyor" hatası alırsınız.

**Windows'ta elle eklemek:** Başlat → "ortam değişkenleri" yazın → *Sistem ortam değişkenlerini düzenle* → **Ortam Değişkenleri** → *Path* → **Düzenle** → **Yeni** → JDK'nin bin yolunu yapıştırın, örneğin `C:\Program Files\Eclipse Adoptium\jdk-21.0.4.7-hotspot\bin` → Tamam. Terminali kapatıp açın.

**macOS'ta elle eklemek** (nadiren gerekir): Terminal'de

```bash
echo 'export PATH="$(/usr/libexec/java_home -v 21)/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## Adım 3 · VS Code ve Java eklentisi

1. [code.visualstudio.com](https://code.visualstudio.com/) adresinden VS Code'u kurun.
2. Sol çubukta **Extensions** (kare simge) → arama kutusuna `Extension Pack for Java` yazın → Microsoft'un paketini **Install**.
3. VS Code'u yeniden başlatın. Bir `.java` dosyası açtığınızda `main` metodunun üstünde **Run** yazısı belirir.

Ders için bir klasör açın: **File → Open Folder** → portfolyo deponuzun klasörü. Terminal için **Terminal → New Terminal** (VS Code'un içinde açılır).

## Adım 4 · İlk dosya: derle, çalıştır

`Merhaba.java` adında dosya oluşturun (dosya adı = sınıf adı, büyük harf dahil):

```java
public class Merhaba {
    public static void main(String[] args) {
        System.out.println("Merhaba, Java!");
    }
}
```

VS Code terminalinde:

```bash
javac Merhaba.java     # Merhaba.class üretir
java Merhaba           # çalıştırır; .class YAZMAYIN
```

Java 11 ve sonrasında tek dosyalık programlar için kısayol da var: `java Merhaba.java` (derleme ve çalıştırma tek adımda). Öğrenme aşamasında iki adımı ayrı görmenizi istiyoruz; ama acelesi olan için orada.

## Sık karşılaşılan hatalar

| Mesaj | Sebep | Çözüm |
|---|---|---|
| `'javac' is not recognized` / `command not found` | PATH ayarı yok ya da terminal eski | Adım 2; terminali kapatıp açın |
| `error: file not found: Merhaba.java` | Yanlış klasördesiniz | `cd` ile dosyanın klasörüne gidin; `ls` / `dir` ile kontrol edin |
| `class Merhaba is public, should be declared in a file named Merhaba.java` | Dosya adı ile sınıf adı farklı | Dosyayı sınıf adıyla, aynı büyük-küçük harfle kaydedin |
| `Could not find or load main class Merhaba.class` | `java Merhaba.class` yazdınız | `java Merhaba` |
| `';' expected` | Noktalı virgül eksik | Satır numarasına bakın; eksik olan genelde bir üst satırdır |
| `cannot find symbol` | Yazım hatası ya da tanımsız değişken | Adı ve büyük-küçük harfi kontrol edin: `system` değil `System` |
| `reached end of file while parsing` | Kapanmamış `{` | Parantezleri eşleştirin; VS Code eşleşeni vurgular |
| Türkçe karakterler bozuk çıkıyor | Terminal kodlaması | Windows'ta `chcp 65001`; ya da çıktıda Türkçe karakterden kaçının |

## Yararlı komutlar

```bash
java -version          # kurulu sürüm
javac Dosya.java       # derle
java Dosya             # çalıştır
java Dosya.java        # tek adımda derle+çalıştır (tek dosya)
jshell                 # etkileşimli kabuk; çıkış: /exit
cd klasor              # klasöre gir
ls   (macOS) / dir (Windows)   # klasör içeriği
```
