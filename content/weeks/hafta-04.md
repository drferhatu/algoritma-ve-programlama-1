---
week: 4
title: "Seçim Yapıları I: boolean, if/else ve İç İçe if"
topic: "boolean tipi ve karşılaştırma operatörleri; tek yönlü if, if/else, else-if merdiveni ve iç içe if; yaygın seçim hataları"
description: "Programın yol ayrımı: koşulları boolean olarak ifade etmek, if/else ile karar vermek, iç içe kararları düzgün kurmak."
module: m2
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "boolean"
  - "if"
  - "else"
  - "iç içe if"
  - "karşılaştırma"
objectives:
  - "Karşılaştırma operatörleriyle boolean ifadeler yazar ve elle değerlendirir."
  - "if, if/else ve else-if merdiveniyle çok yollu karar yapıları kurar."
  - "İç içe if'i doğru girintiler ve bloklarla yazar; sarkan else tuzağını tanır."
  - "= ile == ve if (x = 5) gibi klasik hataları yakalar."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
---

## Haftanın Bulmacası

Harf notu karar ağacı: sınıf, 0-100 arası puanı harfe çeviren kuralı kağıtta ağaç olarak çizer; sonra üç öğrenci tahtada üç farklı puanı elle izler. Aynı ağaç iki farklı if sırasıyla yazıldığında sonuç değişir mi?

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **boolean tipi ve karşılaştırma operatörleri; tek yönlü if, if/else, else-if merdiveni ve iç içe if; yaygın seçim hataları**

İşlenecek başlıklar:

- boolean tipi; karşılaştırma operatörleri < <= > >= == !=
- Tek yönlü if; blok ve süslü parantez alışkanlığı
- İki yönlü if/else; else-if merdiveni (not hesaplama, vergi dilimi)
- İç içe if; sarkan else (dangling else) sorunu
- Rastgele sayı ile toplama/çıkarma quiz'i (geçen yılın sınıf içi örneği)
- Artık yıl, BMI sınıflaması örnekleri
- Yaygın hatalar: = / == karışıklığı, noktalı virgüllü if, gereksiz boolean karşılaştırma
- Kod izleme alıştırması: verilen girdiyle hangi dal çalışır?

## Temel Kavramlar

- **boolean**: Yalnızca true veya false alan tip.
- **Koşul (condition)**: if'in parantezindeki boolean ifade.
- **Blok**: Süslü parantez arasındaki satırlar; tek satır bile olsa parantez koyun.
- **else-if merdiveni**: Birbirini dışlayan çok yollu karar.
- **Sarkan else**: else'in hangi if'e ait olduğu belirsizliği; girinti değil parantez belirler.

## Sahadan Örnekler

- Termostat ve klima: sıcaklık eşiğine göre aç/kapa; dünyadaki en yaygın if/else.
- Vergi dilimi hesabı: else-if merdiveninin kanunla yazılmış hali; sıra yanlışsa herkes yanlış vergi öder.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 4](/laboratuvar/lab-04). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
