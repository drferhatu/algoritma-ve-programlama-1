---
title: "GitHub ve Codespaces"
description: "Hesap açma, öğrenci paketi, portfolyo deposunu oluşturma, commit ve push'un en kısa hali, Codespaces'te kurulumsuz Java çalıştırma."
order: 3
icon: "🐙"
---

## GitHub nedir, neden zorunlu?

GitHub, kod için Google Drive artı sosyal medya: dosyalarınızı saklar, her değişikliğin tarihçesini tutar, başkalarıyla paylaşmanızı sağlar. Bu derste **portfolyo deponuz** GitHub'da yaşar; laboratuvar görevleri ve dört kilometre taşı (KT1-KT4) oraya push edilir. Mezun olduğunuzda işverenin ilk bakacağı yer de burasıdır.

## Adım 1 · Hesap

1. [github.com/signup](https://github.com/signup): **üniversite e-postanızla** kaydolun (öğrenci paketi için gerekli). Kullanıcı adını düşünerek seçin; yıllarca kullanacaksınız ve CV'nize yazacaksınız.
2. E-posta doğrulamasını yapın.
3. Ders organizasyonu daveti lab'da verilecek; gelen daveti kabul edin.

## Adım 2 · Öğrenci paketi (GitHub Education)

[education.github.com/pack](https://education.github.com/pack): GitHub Pro, Copilot, JetBrains IDE'leri, bulut kredileri ve daha fazlası ücretsiz. Başvuruda öğrenci belgesi ya da üniversite e-postası ister; onay birkaç gün sürebilir. Ders için şart değil ama Codespaces saatinizi artırır.

## Adım 3 · Portfolyo deposu

1. Sağ üst **+** → **New repository**.
2. Ad: `algo1-portfolyo`. Görünürlük: **Public** (sınavda sizden bu depodan soru soracağız; halka açık olması bir sorun değil, tersine bir portfolyo).
3. **Add a README file** işaretli. **Create repository**.

Bu depo dönem boyunca **tek** deponuz. Her lab için `labXX/` klasörü, kilometre taşları için sürüm etiketi ya da klasör.

## Adım 4 · Git'in en kısa hali

Git, değişiklikleri kaydeden araçtır; GitHub o kayıtların internetteki kopyasıdır. Bilmeniz gereken döngü üç komut:

```bash
git add .                          # değişen dosyaları sepete koy
git commit -m "Lab 3: Scanner"     # sepeti bir mesajla kaydet
git push                           # kaydı GitHub'a gönder
```

Kendi bilgisayarınızda ilk kez çalışacaksanız depoyu bir kez indirin:

```bash
git clone https://github.com/KULLANICI/algo1-portfolyo.git
cd algo1-portfolyo
```

Git kurulu değilse [git-scm.com](https://git-scm.com/downloads). İlk push'ta GitHub kullanıcı adı ve **şifre yerine token** ister; tarayıcı üzerinden giriş öneren pencereyi kabul edin, en kolayı odur. VS Code'da sol çubuktaki **Source Control** simgesi aynı üç adımı düğmeyle yapar.

> [!uyari] Commit mesajı
> "asdf" ya da "düzeltme" yazmayın. Ne yaptığınızı bir cümleyle yazın: "Lab 6: gözcü değerli toplama eklendi". Sınavdan önce kendi tarihçenizi okuyacaksınız.

## Adım 5 · Codespaces: kurulumsuz VS Code

Kendi bilgisayarına Java kuramayanlar ya da lab bilgisayarında çalışanlar için:

1. Deponuzu GitHub'da açın → yeşil **Code** düğmesi → **Codespaces** sekmesi → **Create codespace on main**.
2. Bir dakika içinde tarayıcıda tam bir VS Code açılır; sağ altta terminal.
3. Terminalde `java -version` yazın; Java hazır gelir (gelmezse, Extensions'tan **Extension Pack for Java** kurun; kurulumu önerir).
4. Dosya oluşturun, `javac` / `java` ile çalıştırın, sol çubuktaki Source Control ile commit ve push yapın; ya da terminalde üç komut.

Ücretsiz hesapta ayda **60 saat** (öğrenci paketiyle 180). Codespace'i işiniz bitince **Stop** edin (Codespaces sayfasından); açık kalırsa saat yer. Kapatınca dosyalar kaybolmaz ama push etmediğiniz değişiklik yalnızca o Codespace'te kalır; **her lab sonunda push** alışkanlığı bu yüzden.

## Sık sorunlar

| Belirti | Çözüm |
|---|---|
| `git push` şifre kabul etmiyor | GitHub şifre yerine token ister; tarayıcıyla giriş seçeneğini kullanın ya da GitHub Desktop kurun |
| `fatal: not a git repository` | Depo klasörünün içinde değilsiniz; `cd algo1-portfolyo` |
| Push reddedildi (rejected) | Önce `git pull`, sonra tekrar `git push` |
| Codespace açılmıyor | Kota bitmiş olabilir; Codespaces sayfasında eski olanları silin |
| Dosyalar GitHub'da görünmüyor | Commit ettiniz ama push etmediniz; `git push` |
