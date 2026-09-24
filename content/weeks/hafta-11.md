---
week: 11
title: "Diziler II: Arama, Sıralama ve Kopyalama"
topic: "Doğrusal ve ikili arama, seçmeli sıralama, dizi kopyalama (sığ ve derin), diziyi metoda gönderme ve metottan dizi döndürme, java.util.Arrays"
description: "Dizilerle klasik algoritmalar: aramak (doğrusal ve ikili), sıralamak, doğru kopyalamak ve diziyi metotlarla birlikte kullanmak. KT3 teslim haftası: dizi alıp tek değer döndüren metot."
module: m4
semester: 1
exam: false
status: taslak
changeNote: ""
milestone: "KT3"
tags:
  - "doğrusal arama"
  - "ikili arama"
  - "sıralama"
  - "kopyalama"
  - "Arrays"
  - "KT3"
objectives:
  - "Doğrusal ve ikili aramayı yazar; adım sayılarını karşılaştırır."
  - "Seçmeli sıralamayı elle izler ve Java'da yazar."
  - "Sığ ve derin kopyalama farkını bellek çizimiyle açıklar."
  - "Dizi alan ve dizi döndüren metot yazar; değişikliğin çağırana yansıdığını fark eder."
tools:
  - "JDK 21"
  - "VS Code"
  - "GitHub Codespaces"
  - "java.util.Arrays"
---

## Haftanın Bulmacası

Kart destesi: 16 kapalı kart, birini arıyorsunuz. Karışık desteyi en kötü kaç bakışta bulursunuz? Sıralı desteyi? (16 ve 4.) 6. haftanın sayı tahmin oyunu geri döndü; adı ikili arama.

> [!uyari] KT3 teslim haftası
> Bu hafta portfolyo kilometre taşı **KT3** teslim edilir; son an, bu haftanın laboratuvar saatidir. Ayrıntı: [Ders Hakkında · Portfolyo](/ders-hakkinda).

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **Doğrusal ve ikili arama, seçmeli sıralama, dizi kopyalama (sığ ve derin), diziyi metoda gönderme ve metottan dizi döndürme, java.util.Arrays**

İşlenecek başlıklar:

- Doğrusal arama: baştan sona; bulununca dur
- İkili arama: sıralı dizide ortadan böl; adım sayısı log2(n)
- Seçmeli sıralama (selection sort): en küçüğü bul, başa al
- Dizi kopyalama: = ile sığ, döngüyle derin, System.arraycopy, Arrays.copyOf
- Diziyi metoda gönderme: referans geçer, metot diziyi değiştirebilir
- Metottan dizi döndürme; dizi ters çevirme
- java.util.Arrays: sort, toString, fill, binarySearch
- Harf sayma örneği (11-HarfSay), sayı analizi
- KT3: dizi alıp tek değer döndüren metot + girdi doğrulayan metot

## Temel Kavramlar

- **Doğrusal arama**: Her elemana sırayla bakma; n adım.
- **İkili arama**: Sıralı dizide aralığı yarıya bölerek arama; log n adım.
- **Seçmeli sıralama**: Her turda kalanların en küçüğünü öne alma.
- **Sığ kopya**: İki değişken aynı diziyi gösterir; biri değişince öteki de.
- **Derin kopya**: Yeni dizi oluşturup elemanları tek tek kopyalama.

## Sahadan Örnekler

- Telefon rehberi: alfabetik sıralı olduğu için ikili arama; milyar kayıtta 30 adım.
- Veritabanı indeksleri: sıralı tutulan sütunlar sayesinde arama saniyeler yerine milisaniyeler sürer; SQL'in altında bu haftanın algoritmaları var.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 11](/laboratuvar/lab-11). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
