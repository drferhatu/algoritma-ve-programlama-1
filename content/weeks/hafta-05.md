---
week: 5
title: "Seçim Yapıları II: switch, Ternary ve Mantıksal Operatörler"
topic: "switch ifadesi, ternary (?:) operatörü, mantıksal operatörler (&&, ||, !, ^), kısa devre değerlendirme ve operatör önceliği"
description: "Karar yapılarını tamamlıyoruz: çok yollu switch, tek satırlık ternary, koşulları birleştiren mantıksal operatörler ve kısa devrenin neden önemli olduğu. KT1 teslim haftası."
module: m2
semester: 1
exam: false
status: taslak
changeNote: ""
milestone: "KT1"
tags:
  - "switch"
  - "ternary"
  - "mantıksal operatör"
  - "kısa devre"
  - "KT1"
objectives:
  - "switch ile menü tarzı çok yollu seçim yazar; break'in rolünü açıklar."
  - "Ternary operatörü uygun yerde kullanır, kötüye kullanımını tanır."
  - "&&, ||, ! ile bileşik koşullar kurar ve doğruluk tablosuyla doğrular."
  - "Kısa devre değerlendirmenin bir hatayı nasıl önlediğini örnekle gösterir."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
  - "GitHub"
---

## Haftanın Bulmacası

Kısa devre bulmacası: kağıtta beş bileşik koşul; her biri için "sağ taraf hiç değerlendirilir mi?" sorusuna cevap verin. Sonra Playground'da sağ tarafa bilerek sıfıra bölme koyup tahmini sınayın.

> [!uyari] KT1 teslim haftası
> Bu hafta portfolyo kilometre taşı **KT1** teslim edilir; son an, bu haftanın laboratuvar saatidir. Ayrıntı: [Ders Hakkında · Portfolyo](/ders-hakkinda).

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **switch ifadesi, ternary (?:) operatörü, mantıksal operatörler (&&, ||, !, ^), kısa devre değerlendirme ve operatör önceliği**

İşlenecek başlıklar:

- switch: case, break, default; String ve char üzerinde switch; yeni ok (->) sözdizimi
- Ternary operatörü: koşul ? a : b
- Mantıksal operatörler: && || ! ^; doğruluk tabloları
- Kısa devre (short-circuit): && ve || sağ tarafı ne zaman atlar
- Operatör önceliği tablosu; parantezle netleştirme
- De Morgan kuralları: !(a && b)
- Örnekler: loto, Çin zodyağı, artık yıl (mantıksal operatörlerle)
- KT1: portfolyo deposu, konu ve seçim yapılı ilk sürüm

## Temel Kavramlar

- **switch**: Bir değeri birçok sabit case ile karşılaştıran yapı.
- **break**: switch'te sonraki case'e düşmeyi önler; unutulursa fall-through olur.
- **Ternary (?:)**: if/else'in ifade hali; bir değer üretir.
- **Kısa devre**: a && b'de a false ise b hiç hesaplanmaz.
- **Doğruluk tablosu**: Bir mantıksal ifadenin tüm girdi kombinasyonlarındaki sonucu.

## Sahadan Örnekler

- ATM menüsü: 1 para çek, 2 bakiye, 3 çık; switch'in doğal yaşam alanı.
- Uçuş rezervasyon kuralları: (yaş >= 18 || veliVar) && koltukBos; kısa devre, veli kontrolünü gereksiz yere yapmayı önler.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 5](/laboratuvar/lab-05). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
