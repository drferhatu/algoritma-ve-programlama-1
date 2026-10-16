---
week: 5
title: "Seçim Yapıları II: switch, Ternary ve Mantıksal Operatörler"
topic: "switch ifadesi, ternary (?:) operatörü, mantıksal operatörler (&&, ||, !, ^), kısa devre değerlendirme ve operatör önceliği"
description: "Karar yapılarını tamamlıyoruz: çok yollu switch, tek satırlık ternary, koşulları birleştiren mantıksal operatörler ve kısa devrenin neden önemli olduğu. Portfolyo deposu bu hafta açılır; KT1 teslimi 6 Kasım."
module: m2
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "switch"
  - "ternary"
  - "mantıksal operatör"
  - "kısa devre"
  - "portfolyo"
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

> [!not] Portfolyo başlıyor
> Proje konuları dağıtıldı: konunuzu ve ayırt edici kuralınızı [Proje](/proje) sayfasında numaranızla bulun, Classroom 50 bağlantısıyla deponuzu açın. İlk kilometre taşı **KT1**, [6. haftanın](/haftalar/hafta-06) lab haftasında, **6 Kasım Cuma 23.59**'da toplanır; bu haftaki switch ve mantıksal operatörler o ilk sürümün karar kısmını yazmanız için tam zamanında geliyor.

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
- Portfolyo: depo açma, README'ye konu ve kuralı yazma; KT1'e doğru ilk seçim yapısı

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
