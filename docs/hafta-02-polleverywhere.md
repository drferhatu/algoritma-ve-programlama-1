# Hafta 2 · Poll Everywhere soru seti

Öğretim üyesi notu (siteye girmez). Sıra, ders akışına göre: açılış → Örnek 2 → hata avı → kapanış. Toplam 5 soru; ★ işaretliler en etkilileri. Her iki şubede aynı set; sonuçları ayrı kaydet.

---

## Açılış (ATM bulmacasından hemen önce)

**1. Çoktan seçmeli: Daha önce akış diyagramı çizdin mi?**
Tür: Multiple Choice · Tek seçim
- Hiç çizmedim, ne olduğunu da bilmiyorum
- Lisede gördüm, çizmedim
- Birkaç kez çizdim (ders, proje, Scratch)
- Sık çizerim, elması tanırım
Not: Çoğunluk ilk iki şık çıkar; "O zaman bugün sembol bilmeden başlıyoruz; sembolleri sizin çiziminizden çıkaracağız." Son şıkkı seçenlere: "Sizden ATM çiziminde çok bitişli diyagramları yakalamanızı isteyeceğim."

## Örnek 2 (Playground'da çalıştırmadan önce)

**2. ★ Çoktan seçmeli: 1'den 10'a kadar sayıların toplamı kaç?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra kağıtta izle, sonra çalıştır)
- 45
- 50
- 55
- 100
Not: 45 diyenler döngünün `i <= 10` yerine `i < 10` çalıştığını varsayar; bu da bir mantık hatası örneğidir, sonucu gösterdikten sonra söyle: "`<=` yerine `<` yazsaydık 45 çıkardı; program çalışırdı, kimse bağırmazdı." Sonra "10'u 100 yapın" denemesi.

## Hata avı (programı açmadan hemen önce)

**3. ★ Çoktan seçmeli: Bir Java programı bir sayıyı sıfıra bölmeye çalışırsa ne olur?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme
- javac derlemez, program hiç çalışmaz
- Program çalışır, o satıra gelince çöker ve bir hata mesajı yazar
- Program çalışır, sonuç olarak 0 verir
- Program çalışır, sonuç olarak sonsuz verir
Not: Doğru: ikinci şık (`ArithmeticException: / by zero`). İlk şıkkı seçenlere: "javac bilmez; sıfır bir değişkenin içinde, derleme anında değeri yok." Dördüncü şıkkı seçenler `double` için haklı olurdu (Infinity); bunu söyle, 3. haftaya bağla. Hata avı tablosundaki "kim yakalar" sütunu bu sorudan sonra oturur.

**4. ★ Çoktan seçmeli: Üç hata türünden hangisi en sinsi?**
Tür: Multiple Choice · Tek seçim · Hata avı bittikten SONRA sor
- Sözdizimi: program hiç çalışmıyor, en kötüsü bu
- Çalışma zamanı: ortada çöküyor, kullanıcı görüyor
- Mantık: çalışıyor ama yanlış, kimse fark etmiyor
- Üçü de aynı derecede kötü
Not: Üçüncü şık dersin tezi. İlk şıkkı seçenlere: "Hiç çalışmayan program zararsızdır; yanlış çalışan program uydu yakar (Mars Climate Orbiter)." Sonucu 9. haftada (vize öncesi) tekrar sor.

## Kapanış (son 3 dakika)

**5. ★ Açık uçlu: Bugünden aklında kalan tek cümle?**
Tür: Open-Ended (Text Wall) · Anonim
Not: 3. haftanın açılışında bu duvardan 2-3 cümle okuyarak başla. "Kimse bağırmaz", "elmas = if", "noktalı virgül kapıda yok" cümleleri gelirse ders yerine oturmuştur. "ATM" ya da "kantin" geçen cümleleri lab sorumlu hocasıyla paylaş; Lab 2'nin Görev 4'ü için motivasyon.

---

### Kurulum ipuçları

- 2. ve 3. sorularda "Show results" kapalı başlasın; önce oy, sonra çalıştır/izle, sonra sonuç. Dersin "önce tahmin, sonra çalıştır" ritüeli.
- 4. soruyu hata avının `<details>` bloğu açıldıktan sonra sor; önce sorulursa tartışmayı bozar.
- 5. soruda küfür filtresini aç.
- 2., 3. ve 4. soruların sonuçlarını iki şube için ayrı ekran görüntüsü olarak al; 4. soruyu 9. haftada, 2. sorunun "45" yüzdesini 6. haftada (döngü sınırları) tekrar göster.
