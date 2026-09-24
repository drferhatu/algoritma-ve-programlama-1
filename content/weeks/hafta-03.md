---
week: 3
title: "Değişkenler, Veri Tipleri, Operatörler ve Scanner"
topic: "Java'da değişken ve ilkel veri tipleri (int, double, char, boolean, String), aritmetik operatörler ve öncelik, tür dönüşümü, sabitler, Scanner ile klavyeden girdi"
description: "Kutuların tipleri: int ile double'ın farkı, 7/2 tuzağı, tür dönüşümü ve kullanıcıdan ilk kez klavyeden veri alan program."
module: m1
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "değişken"
  - "int"
  - "double"
  - "String"
  - "operatör"
  - "tür dönüşümü"
  - "Scanner"
objectives:
  - "Uygun tipte değişken tanımlar ve değer atar; int/double/char/boolean/String'i ayırt eder."
  - "Aritmetik operatörleri ve öncelik kurallarını uygulayarak bir ifadenin sonucunu elle hesaplar."
  - "Tür dönüşümünü (otomatik ve casting) açıklar; tam sayı bölmesi tuzağını fark eder."
  - "Scanner ile klavyeden sayı ve metin okuyan bir program yazar."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
  - "Scanner"
---

## Haftanın Bulmacası

İki bardak bulmacası: elinizde su dolu bir bardak ve çay dolu bir bardak var; içerikleri takas edin. Kaç bardak gerekir? (Üç.) Tahtada `int a = 5; int b = 7;` için aynı takası yazın; `a = b; b = a;` neden çalışmaz?

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **Java'da değişken ve ilkel veri tipleri (int, double, char, boolean, String), aritmetik operatörler ve öncelik, tür dönüşümü, sabitler, Scanner ile klavyeden girdi**

İşlenecek başlıklar:

- Değişken: isim, tip, değer; tanımlama ve atama; isimlendirme kuralları (camelCase)
- İlkel tipler: byte/short/int/long, float/double, char, boolean; String bir sınıftır
- Literal'ler ve taşma (overflow): int'in sınırı
- Aritmetik operatörler: + - * / %; tam sayı bölmesi ve kalan
- Operatör önceliği; parantez kullanımı; birleşik atama (+=, -=), ++ ve --
- Tür dönüşümü: genişletme otomatik, daraltma casting (int) 3.9
- Sabitler: final double PI
- Scanner: import, nextInt, nextDouble, nextLine; nextInt sonrası nextLine tuzağı
- Math sınıfından ilk metotlar: Math.pow, Math.sqrt, Math.round
- Yaygın hatalar: tanımsız değişken, tip uyuşmazlığı, sıfıra bölme

## Temel Kavramlar

- **İlkel tip (primitive)**: Java'nın yerleşik sekiz tipi; int ve double en sık kullandıklarımız.
- **Tam sayı bölmesi**: İki int bölündüğünde kalan atılır: 7/2 = 3.
- **Tür dönüşümü (casting)**: Bir değeri başka tipe zorlamak: (int) 3.9 → 3.
- **Sabit (final)**: Bir kez atanan, sonra değişmeyen değişken.
- **Scanner**: Klavyeden okuma sınıfı; new Scanner(System.in).

## Sahadan Örnekler

- Mars Climate Orbiter: birim karışıklığı bir tip ve dönüşüm sorunudur; değişkenin adına birimi yazmak (kuvvetNewton) ucuz bir sigortadır.
- Bankacılık yazılımları para için double kullanmaz; 0.1 + 0.2'nin 0.30000000000000004 çıkması gerçek bir muhasebe sorunudur.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 3](/laboratuvar/lab-03). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
