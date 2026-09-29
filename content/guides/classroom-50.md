---
title: "Classroom 50: Ödev Deposu ve Otomatik Kontrol"
description: "Lab ve portfolyo depolarının nasıl dağıtıldığı: organizasyon daveti, kabul bağlantısı, deponun adı, push ile teslim, Releases sayfasındaki otomatik kontrol, son teslim kuralı ve sık sorunlar."
order: 4
icon: "🎓"
---

## Classroom 50 nedir?

[Classroom 50](https://classroom50.org), Harvard'ın CS50 ekibinin geliştirdiği ücretsiz ve açık kaynak bir ödev dağıtım aracıdır. Hoca bir ödev tanımlar, siz bir bağlantıya tıklarsınız, GitHub'da size ait bir depo kendiliğinden oluşur. Her push'ta otomatik kontrol çalışır ve puanınızı görürsünüz. Bu derste bütün lab görevleri ve portfolyo bu yolla verilir; elle depo açmanız gerekmez.

Ders organizasyonu: **FiratUniversity-FerhatUcarsLAB**. Classroom kısa adı: **algo1**.

## 1 · Davet: bağlantı yalnızca üyelerde çalışır

Kabul bağlantısı yalnızca organizasyona davet edilmiş GitHub hesaplarında çalışır. Sıra şöyle:

1. GitHub hesabınızı açın (üniversite e-postanızla) ve e-posta doğrulamasını yapın.
2. GitHub kullanıcı adınızı ya da üniversite e-postanızı lab sorumlu hocanıza bildirin. Dönem başındaki listeyle davet aldıysanız bu adım gerekmez.
3. E-postanıza ve GitHub bildirimlerinize "FiratUniversity-FerhatUcarsLAB organizasyonuna davet" gelir; **Accept** deyin. Bildirim gelmediyse [github.com/FiratUniversity-FerhatUcarsLAB](https://github.com/FiratUniversity-FerhatUcarsLAB) adresini açın; üstte **View invitation** düğmesi görünür.

> [!uyari] "Not a member yet"
> Kabul sayfasında bu yazıyı görüyorsanız daveti henüz kabul etmemişsiniz demektir. Daveti kabul edin, sonra sayfadaki **Check again** düğmesine basın.

## 2 · Kabul bağlantısı ve depo

Her ödevin kendi kabul bağlantısı vardır; biçimi şöyledir:

```
https://classroom50.org/FiratUniversity-FerhatUcarsLAB/algo1/assignments/labXX/accept
```

Bağlantı lab sayfasında ve lab günü verilir (Lab 1: [Lab 1 sayfası](/laboratuvar/lab-01)). Tıklayın, GitHub ile giriş yapın, **Accept assignment** deyin. Birkaç saniye içinde deponuz oluşur:

- Ad: `algo1-labXX-KULLANICIADI` (organizasyonun altında).
- Görünürlük: **özel (private)**; siz ve ders ekibi görür.
- İçerik: README ve `.gitignore`. Dosyalarınızı deponun **kök dizinine** koyarsınız, alt klasör açmazsınız.

> [!not] Dokunmayın
> Depoyu **yeniden adlandırmayın**, **Actions**'ı kapatmayın, görünürlüğü değiştirmeyin. Otomatik kontrol deponun adına ve Actions'a bağlıdır; herkese açık (public) yapılan depoda kontrol çalışmaz.

İsteğe bağlı komut satırı yolu: GitHub CLI kuruluysa `gh extension install foundation50/gh-student` sonrası `gh student accept FiratUniversity-FerhatUcarsLAB algo1 lab01`.

## 3 · Çalışma ve teslim

Depoyu iki yoldan açabilirsiniz:

- **Codespaces:** depo sayfasında **Code** → **Codespaces** → **Create codespace on main**. Tarayıcıda VS Code açılır, Java hazır gelir.
- **Kendi bilgisayarınız:** `git clone https://github.com/FiratUniversity-FerhatUcarsLAB/algo1-labXX-KULLANICIADI.git`

Dosyaları yazın, derleyip çalıştırın, sonra push edin:

```bash
git add .
git commit -m "Lab 1: ilk Java dosyaları"
git push
```

Codespaces'te sol çubuktaki **Source Control** düğmesi aynı işi tıklamayla yapar (**Commit**, sonra **Sync Changes**). Teslim, push'tan ibarettir; ayrıca bir yere yükleme yoktur. Ayrıntılı Git özeti: [GitHub ve Codespaces rehberi](/rehber/github-ve-codespaces).

## 4 · Otomatik kontrol: Releases ve Feedback

Her push'ta deponuzda GitHub Actions çalışır (1-2 dakika). Sonuç iki yerde görünür:

- Deponun **Releases** sayfası: hangi test geçti, hangi test kaldı, toplam puan.
- Depoda otomatik açılan **Feedback** pull request'i: aynı sonuç ve lab sorumlu hocanızın yorumları.

Kontrol yalnızca dosyaların **derlenip derlenmediğine** ve **birkaç beklenen çıktı satırına** bakar. Bu yüzden dosya adı, sınıf adı ve beklenen satır (ör. `5 x 10 = 50`) lab sayfasında yazıldığı gibi **birebir** olmalı. Bir test kaldıysa düzeltin, tekrar push edin; son teslim saatine kadar sınırsız deneme hakkınız var, en son push geçerlidir.

> [!not] Otomatik puan her şey değildir
> Otomatik kontrol lab notunun bir parçasıdır. Kodun okunabilirliği, isimlendirme ve lab'daki "30 saniye anlat" ritüeli lab sorumlu hocanızın değerlendirmesidir. Anlatamadığınız kod sizin değildir.

## 5 · Son teslim kuralı

**Her lab'ın son teslimi, o lab haftasının Cuma günü 23.59'udur.** Lab saatinde bitiremeyenler Cuma gecesine kadar evden push edebilir. Cuma'dan sonra gelen push'lar puanlanmaz. Portfolyo kilometre taşları (KT1-KT4) için de aynı kural geçerlidir: ilgili lab haftasının Cuma 23.59'u.

Portfolyo deposu, lab depolarından **ayrıdır** ve ilerleyen haftalarda (KT1 5. hafta; bağlantı 3-4. haftada) aynı yöntemle, ayrı bir kabul bağlantısıyla verilecektir.

## Sık sorunlar

| Belirti | Çözüm |
|---|---|
| Kabul sayfası "Not a member yet" diyor | Organizasyon davetini henüz kabul etmediniz; e-postanıza ya da [github.com/FiratUniversity-FerhatUcarsLAB](https://github.com/FiratUniversity-FerhatUcarsLAB) adresine bakın, daveti kabul edin, sonra **Check again** |
| Davet e-postası gelmedi | GitHub'daki e-posta adresiniz farklı olabilir; GitHub bildirimlerine ve organizasyon sayfasına bakın, olmadı lab sorumlu hocanıza kullanıcı adınızı yeniden bildirin |
| Releases sayfasında sonuç yok | Push'tan sonra 1-2 dakika bekleyin; deponun **Actions** sekmesinde çalışmayı görebilirsiniz |
| Actions sekmesinde kırmızı çarpı | Derleme hatası olabilir; çalışmaya tıklayıp mesajı okuyun, `javac` ile yerelde deneyin |
| Puan düşük ama kod çalışıyor | Dosya adı, sınıf adı ve beklenen çıktı satırı birebir eşleşmeli (büyük-küçük harf, boşluklar dahil); dosyalar deponun kök dizininde olmalı |
| Dosyalar GitHub'da görünmüyor | Commit ettiniz ama push etmediniz; `git push` ya da Codespaces'te **Sync Changes** |
| Yanlışlıkla iki depo aldım / depo adını değiştirdim | Lab sorumlu hocanıza söyleyin; kendiniz düzeltmeye çalışmayın |
