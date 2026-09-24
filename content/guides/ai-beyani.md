---
title: "AI Beyanı Şablonu"
description: "Yeşil bölge teslimlerinde (portfolyo kilometre taşları ve ev çalışması) her teslime eklenecek kısa yapay zeka beyanının şablonu ve örnekleri."
order: 4
icon: "🟢"
---

## Neden beyan?

Portfolyo ve ev çalışması **yeşil bölge**: yapay zeka serbest. Ama meslekte de böyle olacak: kodu kimin, neyle, nasıl yazdığı sorulur. Beyan bir itiraf değil, bir mühendislik notu. Ve dürüst bir beyan, "anlatamadığınız kod sizin değildir" ilkesinin belgesidir; sınavda o koddan soru gelecek.

Beyan **kısa** olmalı: 4 madde, en fazla 10 satır. Her kilometre taşı teslimi ve her ev çalışması için deponuzda `AI-BEYANI.md` dosyasına yeni bir bölüm ekleyin (ya da README'nin sonuna).

## Şablon

```markdown
## AI Beyanı · KT2 (8. hafta)

1. Hangi araç(lar): ChatGPT (ücretsiz), Claude
2. Ne için kullandım: 
   - do-while ile menü döngüsü fikrini açıklattım
   - "Scanner nextInt sonrası nextLine neden boş dönüyor" hatasını sordum
3. Hangi kısmı kendim yazdım: 
   - Menü döngüsü ve girdi doğrulama tamamen benim
   - Ortalama hesaplayan kısmı AI önerisinden uyarladım, değişken adlarını değiştirdim
4. AI'nın hangi hatasını yakaladım: 
   - Önerdiği kodda gözcü değer 0 iken 0 puan girilmesi de döngüyü bitiriyordu; 
     gözcüyü -1 yaptım
```

Hiç kullanmadıysanız da yazın: "Bu teslimde yapay zeka kullanmadım." Bu da geçerli bir beyandır.

## İyi beyan, kötü beyan

| Kötü | İyi |
|---|---|
| "ChatGPT kullandım." | "ChatGPT'ye switch'te break unutulunca ne olur diye sordum; örneği kendim yazdım." |
| "Kodun hepsini AI yazdı, ben düzenledim." | "AI'nın önerdiği metot iskeletini aldım; dizi üstünde gezen döngüyü ve doğrulamayı ben yazdım; şu satırı anlamadığım için sildim ve kendi yolumla yazdım." |
| 4. madde boş | "AI, dizinin son elemanını `dizi[dizi.length]` ile okumaya çalışıyordu; sınır dışı hatasını görüp `length - 1` yaptım." |

4. madde en değerlisi. Yapay zekanın hatasını yakalayamıyorsanız kodu okumuyorsunuz demektir; okumadığınız kod sınavda sizi kurtarmaz.

## Sınırlar (hatırlatma)

- **Kırmızı** (sınavlar): beyan yok çünkü yapay zeka yok.
- **Sarı** (laboratuvar): soru serbest, kod kopyalama yasak; beyan istenmez ama lab sorumlu hocanız sorabilir.
- **Yeşil** (portfolyo, ev çalışması): serbest + beyan.

Beyansız teslim eksik teslimdir. Yanlış beyan (kullanıp "kullanmadım" demek) kopya kapsamında değerlendirilir. Tam metin ve gerekçeler: [Ders Hakkında](/ders-hakkinda).
