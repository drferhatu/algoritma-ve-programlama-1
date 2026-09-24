---
week: 13
title: "String İşlemleri ve Nehir Bulmacasının Kodlanması"
topic: "char tipi ve Unicode, String'in değişmezliği, length/charAt/substring/indexOf/equals, karakter sayma ve palindrom; 1. haftanın nehir bulmacasını dizilerle kodlama"
description: "Metin de bir dizidir: karakterler, String metotları ve metin algoritmaları. Dönemin kapanış motifi: 1. haftada elle çözdüğünüz nehir bulmacasını bu kez durum dizisiyle Java'da yazıyoruz."
module: m4
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "String"
  - "char"
  - "charAt"
  - "substring"
  - "equals"
  - "palindrom"
  - "nehir bulmacası"
objectives:
  - "char ile int ilişkisini ve String'in değişmez olduğunu açıklar."
  - "length, charAt, substring, indexOf, equals, toUpperCase metotlarını kullanır; == ile equals farkını bilir."
  - "Karakter sayma, ters çevirme ve palindrom algoritmalarını yazar."
  - "Nehir bulmacasını durum dizisi, hamle döngüsü ve kısıt kontrolü ile Java'da kodlar."
tools:
  - "JDK 21"
  - "VS Code"
  - "GitHub Codespaces"
---

## Haftanın Bulmacası

Nehir bulmacası geri döndü. 1. haftada sakladığınız kağıdı çıkarın. Bu kez durumu dört kutulu bir boolean dizisi olarak yazın: [çiftçi, tilki, tavuk, mısır] karşı kıyıda mı? Her hamle bir kutuyu (ve çiftçiyi) çevirir; kısıtlar iki if. Kağıtta kodlayın, sonra Java'da.

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **char tipi ve Unicode, String'in değişmezliği, length/charAt/substring/indexOf/equals, karakter sayma ve palindrom; 1. haftanın nehir bulmacasını dizilerle kodlama**

İşlenecek başlıklar:

- char: 16 bit sayı, Unicode; karakter aritmetiği ('A' + 1)
- String nesneleri değişmezdir (immutable); her değişiklik yeni String
- length(), charAt(), substring(), indexOf(), contains()
- Karşılaştırma: equals ve compareTo; == neden yanlış
- toUpperCase, toLowerCase, trim, split
- Karakter sayma; String'i char dizisine çevirme; ters çevirme; palindrom
- Doubloon problemi (Think Java 7.9): dizi ile harf sayma
- Nehir bulmacasının kodlanması: durum dizisi, güvenli mi metodu, hamle döngüsü, çözüm yolu yazdırma
- Yapay zekanın 1. haftada yazdığı çözümle karşılaştırma

## Temel Kavramlar

- **char**: Tek karakter; aslında bir sayı.
- **Değişmezlik (immutability)**: String bir kez oluşunca değişmez; metotlar yeni String döndürür.
- **charAt(i)**: i. karakteri verir; 0'dan başlar.
- **equals**: İçerik karşılaştırması; == referans karşılaştırır.
- **Durum dizisi**: Bulmacanın anlık durumunu tutan dizi; 1. haftanın "kim hangi kıyıda" sorusu.

## Sahadan Örnekler

- Arama motoru ve otomatik tamamlama: yazdığınız her harf bir String algoritmasını tetikler.
- DNA dizileri: ACGT harflerinden oluşan devasa String'ler; gen arama tam olarak indexOf'un akıllı halidir.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 13](/laboratuvar/lab-13). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
