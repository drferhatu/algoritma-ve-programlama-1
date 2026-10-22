# Hafta 5 · Poll Everywhere soru seti

Öğretim üyesi notu (siteye girmez). Sıra, ders akışına göre: kullanım alışkanlığı → break tuzağı → en iyi istem → doğrulama yöntemi → kapanış. Toplam 5 soru; ★ işaretliler en etkilileri. Her iki şubede aynı set; sonuçları ayrı kaydet.

---

## Dört parça bloğu (tablo açıldıktan sonra, 18-26. dk)

**1. ★ Çoktan seçmeli: Yapay zekayı bu derste şimdiye kadar en çok ne için kullandın?**
Tür: Multiple Choice · Tek seçim · Anonim · Sonuçları hemen göster
- Bir kavramı açıklatmak için ("sarkan else nedir?")
- Hata mesajını yapıştırıp "bu ne demek?" diye sormak için
- Lab görevinin kodunu yazdırmak için
- Kendi kodumu anlattırmak ya da kontrol ettirmek için
- Hiç kullanmadım
Not: Yargı yok, anonim; sonucu olduğu gibi oku. "Kod yazdırmak" yüksekse: "Sarı bölgede yasaktı, bugün yeşilde nasıl yapılacağını öğreniyorsunuz: iskelet asistandan, mantık sizden." "Hiç kullanmadım" yüksekse: "Bugün ilk kez, birlikte." Üçüncü ve dördüncü şıkkın oranını Lab 5 günlükleri için lab sorumlu hocasına ilet.

## Doğrulama anı (tuzak istem gönderilmeden hemen önce, 64. dk)

**2. ★ Çoktan seçmeli: Java'da `switch` içinde bir `case`'in sonuna `break` yazmazsanız ne olur?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme (önce oyla, sonra tuzak istem, sonra Playground)
- `case` bitince `switch`'ten çıkar, `break` yalnızca okunabilirlik için
- Derleyici "missing break" hatası verir
- Bir sonraki `case`'in satırları da çalışır, `break` görene kadar devam eder
- Yalnızca `default` çalışır
Not: Üçüncü şık doğru (fall-through, durmayan asansör). Dersin 42-52. dakikasında asansör kutusu canlı çalıştırıldığı için doğru oranı yüksek olmalı; düşükse kutuyu bir kez daha kat = 3 ile çalıştır. Birinci şıkkı seçenler tuzak istemdeki iddiayı da onaylayacak kişiler: "Soruya gömülü yanlışı asistan da onaylayabilir; siz de onayladınız; Playground onaylamaz." İkinci şıkka: "Keşke verseydi; Java bilerek vermez, çünkü bazen düşme istenir (case 6: case 7:)."

## Doğrulama anından hemen sonra (65. dk)

**3. ★ Çoktan seçmeli: Aşağıdaki üç istemden hangisi en iyi cevabı getirir?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme
- A) "kısa devre nedir"
- B) "Java'da kısa devre nedir, 5 cümleyle anlat"
- C) "Java hocası gibi davran; && ve || için kısa devreyi, b != 0 && a / b > 2 örneğiyle anlat; 5 cümle ve Playground'da deneyebileceğim 6 satırlık Scanner'sız kod; 1. sınıfım, if/else biliyorum"
- D) Üçü de aynı cevabı getirir
Not: C doğru; dört parçanın dördü var. B'yi seçenlere: "Biçim var, rol ve bağlam yok; cevap size değil ortalama öğrenciye." D diyenlere bulmacadaki iki cevabı hatırlat. Bu soru cep kartının birinci istemine köprü.

**4. Çoktan seçmeli: Asistan size "`b != 0 && a / b > 2` ifadesi b = 0 için çöker" dedi. Ne yaparsınız?**
Tür: Multiple Choice · Tek seçim · Doğru cevabı gösterme
- "Emin misin?" diye sorarım, fikrini değiştirirse doğrudur
- Playground'da b = 0 ile çalıştırırım ve ders notundaki kısa devre bölümüyle karşılaştırırım
- Asistan bilir, kabul ederim
- Başka bir asistana sorarım, iki asistan aynı şeyi derse doğrudur
Not: İkinci şık doğru; ifade çökmez, kısa devre sağ tarafı hiç hesaplamaz. Birinci şıkka: "Fikrini değiştirmesi bir şey kanıtlamaz; geçen haftanın 'emin misin' dersi." Dördüncü şıkka: "İki asistan aynı yanlışı yapabilir; Playground tek, çıktı tek." Bu soru doğrulama alışkanlığının ölçüsü; "kabul ederim" yüzdesini 9. haftada tekrar sor.

## Kapanış (son 3 dakika)

**5. ★ Açık uçlu: Bugünden aklında kalan tek cümle?**
Tür: Open-Ended (Text Wall) · Anonim
Not: 6. haftanın açılışında bu duvardan 2-3 cümle okuyarak başla. "Fark araçta değil soruda", "artırma otomasyon değil", "asistan benim yetkimle", "iskelet asistandan mantık benden", "break dur düğmesi", "Playground sanmaz" cümleleri gelirse hikayeler tutmuş demektir. Yapay zekayı yanlış anlatan bir cümle ("artık kod yazmam gerekmiyor" gibi) gelirse 6. haftanın açılışında adını vermeden düzelt.

---

### Kurulum ipuçları

- 2., 3. ve 4. sorularda "Show results" kapalı başlasın; önce oy, sonra gösteri, sonra sonuç. 1. soru anonim ve sonuç hemen açık, çünkü yargı değil tespit.
- 3. sorunun C şıkkı uzun; Poll Everywhere'de satır sınırı varsa "Java hocası gibi davran; kısa devreyi örnekle anlat; 5 cümle + 6 satır kod; 1. sınıfım" diye kısalt, dört parça görünsün.
- 5. soruda küfür filtresini aç.
- 1., 2. ve 4. soruların sonuçlarını iki şube için ayrı ekran görüntüsü olarak al; 1. sorunun "kod yazdırmak" ve 4. sorunun "kabul ederim" yüzdesini lab sorumlu hocasına ilet, Lab 5 günlüklerini okurken ve Lab 6 ritüelinde kullansın.
