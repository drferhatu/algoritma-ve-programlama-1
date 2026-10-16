# Hafta 4 · Poll Everywhere soru seti

Öğretim üyesi notu (siteye girmez). Sıra, ders akışına göre: `=` ile `==` → merdiven → sarkan else → double eşitliği → kapanış. Toplam 5 soru; ★ işaretliler en etkilileri. Her iki şubede aynı set; sonuçları ayrı kaydet.

---

## boolean ve == bloğu (kantin sahnesinden hemen sonra, CodeTry "Soru mu, emir mi?" çalıştırılmadan önce)

**1. ★ Çoktan seçmeli: `int x = 3;` tanımlıyken `if (x = 5) { ... }` yazarsanız Java'da ne olur?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra Playground'da çalıştır)
- Program çalışır ve blok her zaman çalışır
- Program çalışır ve blok hiçbir zaman çalışmaz
- Derleyici hata verir, program hiç çalışmaz
- Program çalışırken çöker
Not: Üçüncü şık doğru (`incompatible types: int cannot be converted to boolean`). Birinci şıkkı seçenlere: "C dilinde haklıydınız; Java int için bağırır." Sonucu gösterdikten hemen sonra sözlü ek soru: "Peki `boolean ogrenci = false;` iken `if (ogrenci = true)`?" Bu kez derleyici susar; CodeTry'da göster. Dersin asıl mesajı bu ikinci kısımda: Java sizi yarı yolda korur, kalan yarısı sizin.

## Merdiven bloğu (CodeTry "Harf notu" çalıştırıldıktan sonra, ters çevirmeden önce)

**2. ★ Çoktan seçmeli: Harf notu merdiveni ters sırada yazılırsa (ilk basamak `puan >= 60`, sonra 70, 80, 90) 85 puan hangi harfi alır?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra merdiveni ters çevirip çalıştır)
- B
- D
- A
- Derleyici hata verir
Not: İkinci şık doğru. Bulmacada aynı soruyu kağıtta çözdüler, bu yüzden D oranı yüksek olmalı; düşükse ters ağacı tahtada bir kez daha adım adım yürüt. "A" diyenler "en büyük tutan basamak kazanır" sanıyor: "merdiven en iyi cevabı aramaz, ilk evette durur." "Derleyici hata verir" diyenlere: "Derleyici sırayı bilmez; bu bir mantık hatası ve sessizdir."

## İç içe if bloğu (CodeTry "Sarkan else: tahmin edin" çalıştırılmadan hemen önce)

**3. ★ Çoktan seçmeli: Aşağıdaki kodda `else` hangi `if`'e aittir?**
```
if (yas >= 18)
    if (ogrenci)
        System.out.println("Ogrenci bileti");
else
    System.out.println("Cocuk bileti");
```
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra çalıştır)
- Dıştaki `if (yas >= 18)`'e, çünkü girintisi onunla hizalı
- İçteki `if (ogrenci)`'ye, çünkü en yakın `if` o
- İkisine birden
- Derleyici belirsizlik hatası verir
Not: İkinci şık doğru. Birinci şık çoğunlukta çıkarsa ders yerine oturmuş demek, çünkü tuzağın sebebi tam olarak bu inanç. Sonucu gösterdikten sonra Playground'da çalıştır, 20 yaş ve `ogrenci = false` için "Cocuk bileti" görülsün. Dördüncü şıkkı seçenlere: "Keşke verseydi; Java kuralı kesin olduğu için belirsizlik görmez, sizin gördüğünüzü görmez." Düzeltmeyi parantezle yap ve tekrar çalıştır.

## Yaygın hatalar bloğu (3. tuzak gösterilmeden hemen önce)

**4. ★ Çoktan seçmeli: Java'da `0.1 + 0.2 == 0.3` ifadesinin değeri nedir?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra çalıştır)
- `true`
- `false`
- Derleyici hata verir
- Bilgisayara göre değişir
Not: İkinci şık doğru. Geçen hafta CodeTry "Bardaklar"ın ipucunda bu satırı denemeleri istenmişti; deneyenler `false` der. `true` diyenlere `0.30000000000000004`'ü hatırlat ve kuralı söyle: "double'ı eşitlikle değil aralıkla karşılaştırın; para için kuruş cinsinden int." Dördüncü şıkka: "Hayır, IEEE 754 her bilgisayarda aynı; hata tutarlıdır, rastgele değil." Vize öncesi (9. hafta) tekrar sorulacak.

## Kapanış (son 3 dakika)

**5. ★ Açık uçlu: Bugünden aklında kalan tek cümle?**
Tür: Open-Ended (Text Wall) · Anonim
Not: 5. haftanın açılışında bu duvardan 2-3 cümle okuyarak başla. "İlk evette durur", "else en yakın if'e ait", "hesap 50 mi / hesabı 50 yap", "süslü parantez her zaman" cümleleri gelirse hikayeler tutmuş demektir. "Apollo" geçen cümleleri say; "ve / ya da" ya da "switch" bekleyen cümleler varsa 5. haftanın açılışında kullan. Sarkan else'i yanlış anlatan bir cümle gelirse lab sorumlu hocasıyla paylaş.

---

### Kurulum ipuçları

- 1., 2., 3. ve 4. sorularda "Show results" kapalı başlasın; önce oy, sonra çalıştır, sonra sonuç. Dersin "önce tahmin, sonra çalıştır" ritüeli.
- 3. sorunun kod bloğu Poll Everywhere'de düz metin olarak girilir; girintiyi boşlukla koru, çünkü soru girintinin yanıltıcılığı üstüne.
- 5. soruda küfür filtresini aç.
- 1., 3. ve 4. soruların sonuçlarını iki şube için ayrı ekran görüntüsü olarak al; 3. sorunun "dıştaki if" yüzdesini Lab 4 ritüeli için lab sorumlu hocasına ilet, 4. sorunun "true" yüzdesini 9. haftada tekrar göster.
