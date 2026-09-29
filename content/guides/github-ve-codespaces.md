---
title: "GitHub ve Codespaces"
description: "Hesap açma, öğrenci paketi, Classroom 50 ile ödev deposu alma, commit ve push'un en kısa hali, Codespaces'te kurulumsuz Java çalıştırma."
order: 3
icon: "🐙"
---

## GitHub nedir, neden zorunlu?

GitHub, kod için Google Drive artı sosyal medya: dosyalarınızı saklar, her değişikliğin tarihçesini tutar, başkalarıyla paylaşmanızı sağlar. Bu derste laboratuvar görevleri ve **portfolyo deponuz** GitHub'da yaşar; her lab görevi ve dört kilometre taşı (KT1-KT4) oraya push edilir. Depolar size [Classroom 50](/rehber/classroom-50) bağlantılarıyla hazır verilir; elle depo açmanız gerekmez. Mezun olduğunuzda işverenin ilk bakacağı yer de burasıdır.

## Adım 1 · Hesap

1. [github.com/signup](https://github.com/signup): **üniversite e-postanızla** kaydolun (öğrenci paketi için gerekli). Kullanıcı adını düşünerek seçin; yıllarca kullanacaksınız ve CV'nize yazacaksınız.
2. E-posta doğrulamasını yapın.
3. Kullanıcı adınızı lab sorumlu hocanıza bildirin; **FiratUniversity-FerhatUcarsLAB** organizasyonundan gelen daveti e-postanızdan ya da GitHub bildirimlerinden kabul edin (Adım 3).

## Adım 2 · Öğrenci paketi (GitHub Education)

[education.github.com/pack](https://education.github.com/pack): GitHub Pro, Copilot, JetBrains IDE'leri, bulut kredileri ve daha fazlası ücretsiz. Başvuruda öğrenci belgesi ya da üniversite e-postası ister; onay birkaç gün sürebilir. Ders için şart değil ama Codespaces saatinizi artırır.

## Adım 3 · Classroom 50 ile ödev deposu almak

Ödevler **Classroom 50** (CS50 ekibinin ücretsiz, açık kaynak aracı) üzerinden dağıtılır. Her lab için size hazır bir depo verilir; siz yalnızca bir bağlantıya tıklarsınız.

1. **Davet.** Kullanıcı adınızı (ya da üniversite e-postanızı) lab sorumlu hocanıza bildirdikten sonra e-postanıza ve GitHub bildirimlerinize "FiratUniversity-FerhatUcarsLAB organizasyonuna davet" gelir; **Accept** deyin. Bildirim göremezseniz [github.com/FiratUniversity-FerhatUcarsLAB](https://github.com/FiratUniversity-FerhatUcarsLAB) adresinde **View invitation** düğmesi çıkar. Bu adım olmadan kabul bağlantısı çalışmaz.
2. **Kabul bağlantısı.** Her lab'ın kabul bağlantısı lab sayfasında ve lab günü verilir (Lab 1: [Lab 1 sayfası](/laboratuvar/lab-01)). Bağlantıya tıklayın, GitHub ile giriş yapın, **Accept assignment** deyin.
3. **Depo.** Birkaç saniye içinde organizasyon altında `algo1-labXX-KULLANICIADI` adlı **özel (private)** deponuz oluşur; içinde bir README ve `.gitignore` vardır. Dosyalarınızı deponun **kök dizinine** koyarsınız. Depoyu yeniden adlandırmayın, **Actions** sekmesini kapatmayın.
4. **Sonuç.** Her push'ta otomatik kontrol çalışır. Puanınızı deponun **Releases** sayfasında ve depoda otomatik açılan **Feedback** pull request'inde görürsünüz; lab sorumlu hocanız yorumlarını da oraya yazar. Son teslim saatine kadar düzeltip yeniden push edebilirsiniz.

Portfolyo (dönem projesi) deposu da ilerleyen haftalarda aynı yöntemle, ayrı bir kabul bağlantısıyla verilecek; kendi elinizle depo açmanız istenmiyor. Ayrıntılar ve sık sorunlar: [Classroom 50 rehberi](/rehber/classroom-50).

İsteğe bağlı komut satırı yolu: [GitHub CLI](https://cli.github.com) kuruluysa `gh extension install foundation50/gh-student` sonrası `gh student accept FiratUniversity-FerhatUcarsLAB algo1 lab01` aynı işi yapar.

## Adım 4 · Git'in en kısa hali

Git, değişiklikleri kaydeden araçtır; GitHub o kayıtların internetteki kopyasıdır. Bilmeniz gereken döngü üç komut:

```bash
git add .                          # değişen dosyaları sepete koy
git commit -m "Lab 3: Scanner"     # sepeti bir mesajla kaydet
git push                           # kaydı GitHub'a gönder
```

Kendi bilgisayarınızda ilk kez çalışacaksanız depoyu bir kez indirin:

```bash
git clone https://github.com/FiratUniversity-FerhatUcarsLAB/algo1-lab01-KULLANICIADI.git
cd algo1-lab01-KULLANICIADI
```

Git kurulu değilse [git-scm.com](https://git-scm.com/downloads). İlk push'ta GitHub kullanıcı adı ve **şifre yerine token** ister; tarayıcı üzerinden giriş öneren pencereyi kabul edin, en kolayı odur. VS Code'da sol çubuktaki **Source Control** simgesi aynı üç adımı düğmeyle yapar.

> [!uyari] Commit mesajı
> "asdf" ya da "düzeltme" yazmayın. Ne yaptığınızı bir cümleyle yazın: "Lab 6: gözcü değerli toplama eklendi". Sınavdan önce kendi tarihçenizi okuyacaksınız.

## Adım 5 · Codespaces: kurulumsuz VS Code

Kendi bilgisayarına Java kuramayanlar ya da lab bilgisayarında çalışanlar için:

1. Lab deponuzu (`algo1-labXX-KULLANICIADI`) GitHub'da açın → yeşil **Code** düğmesi → **Codespaces** sekmesi → **Create codespace on main**.
2. Bir dakika içinde tarayıcıda tam bir VS Code açılır; sağ altta terminal.
3. Terminalde `java -version` yazın; Java hazır gelir (gelmezse, Extensions'tan **Extension Pack for Java** kurun; kurulumu önerir).
4. Dosya oluşturun, `javac` / `java` ile çalıştırın, sol çubuktaki Source Control ile commit ve push yapın; ya da terminalde üç komut.

Ücretsiz hesapta ayda **60 saat** (öğrenci paketiyle 180). Codespace'i işiniz bitince **Stop** edin (Codespaces sayfasından); açık kalırsa saat yer. Kapatınca dosyalar kaybolmaz ama push etmediğiniz değişiklik yalnızca o Codespace'te kalır; **her lab sonunda push** alışkanlığı bu yüzden.

## Sık sorunlar

| Belirti | Çözüm |
|---|---|
| `git push` şifre kabul etmiyor | GitHub şifre yerine token ister; tarayıcıyla giriş seçeneğini kullanın ya da GitHub Desktop kurun |
| `fatal: not a git repository` | Depo klasörünün içinde değilsiniz; `cd algo1-lab01-KULLANICIADI` |
| Push reddedildi (rejected) | Önce `git pull`, sonra tekrar `git push` |
| Codespace açılmıyor | Kota bitmiş olabilir; Codespaces sayfasında eski olanları silin |
| Dosyalar GitHub'da görünmüyor | Commit ettiniz ama push etmediniz; `git push` |
| Kabul sayfası "Not a member yet" diyor | Organizasyon davetini henüz kabul etmediniz; e-postanıza ya da [github.com/FiratUniversity-FerhatUcarsLAB](https://github.com/FiratUniversity-FerhatUcarsLAB) adresine bakın, daveti kabul edin, sonra **Check again** |
| Releases sayfasında sonuç yok | Push'tan sonra 1-2 dakika bekleyin; deponun **Actions** sekmesinde çalışmayı görebilirsiniz |
| Puan düşük ama kod çalışıyor | Dosya adı, sınıf adı ve beklenen çıktı satırı birebir eşleşmeli (büyük-küçük harf, boşluklar dahil); dosyalar deponun kök dizininde olmalı |
