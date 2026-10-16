---
week: 9
title: "Metotlar II: Kapsam, Yığın Diyagramı, Artımlı Geliştirme ve KT2 Teslimi"
topic: "Değişken kapsamı ve yerel değişkenler, çağrı yığını ve yığın diyagramları, artımlı geliştirme ve test etme alışkanlığı; ara sınav haftası"
description: "Metot çağrıldığında bellekte ne olur: yığın diyagramıyla adım adım izleme, kapsam kuralları ve büyük programı küçük adımlarla yazma disiplini. Ara sınav haftası; tarih bölümce ilan edilecek. KT2 teslim haftası: 27 Kasım Cuma 23.59."
module: m3
semester: 1
exam: false
status: taslak
changeNote: ""
milestone: "KT2"
tags:
  - "kapsam"
  - "yığın"
  - "stack"
  - "artımlı geliştirme"
  - "test"
  - "ara sınav"
  - "KT2"
objectives:
  - "Yerel değişken ve kapsam kurallarını açıklar; kapsam hatasını tanır."
  - "Bir metot çağrı zincirini yığın diyagramıyla çizer ve değişken değerlerini izler."
  - "Artımlı geliştirme ile bir problemi küçük, test edilen adımlarla çözer."
  - "Kod izleme sorusunda metot çağrısının dönüş değerini doğru bulur."
  - "KT2: ana akışı gözcü değerle biten bir menü döngüsünde çalışan ve girdi doğrulama döngüsü içeren sürümü 27 Kasım Cuma 23.59'a kadar push eder."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
  - "Java Visualizer"
---

## Haftanın Bulmacası

Kağıt yığını: her metot çağrısı için bir kağıt, üstteki kağıt aktif; return olunca kağıt atılır. Üç metotlu bir program tahtada kağıtlarla "çalıştırılır"; hangi değişken hangi kağıtta?

> [!uyari] KT2 teslim haftası
> Portfolyo kilometre taşı **KT2** bu haftanın lab haftasında, **27 Kasım Cuma 23.59**'da toplanır: Classroom 50 o saatte deponuzda ne varsa onu KT2 sürümü sayar. Beklenen: uygulamanın ana akışı gözcü değerle (ör. 0 veya q) biten bir menü döngüsünde çalışıyor ve yanlış girdiyi doğru girdiye kadar soran bir girdi doğrulama döngüsü var. Ayrıntı: [Proje](/proje).

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **Değişken kapsamı ve yerel değişkenler, çağrı yığını ve yığın diyagramları, artımlı geliştirme ve test etme alışkanlığı; ara sınav haftası**

İşlenecek başlıklar:

- Kapsam (scope): yerel değişkenler, blok kapsamı, aynı ad farklı metot
- Çağrı yığını ve yığın diyagramları (Think Java 4.5)
- Metot içinde değişken değiştirmek çağıranı etkiler mi? (değer ile geçirme)
- Artımlı geliştirme: mesafe hesabı örneği adım adım (Think Java 4.9)
- Test: bilinen cevaplı girdilerle metot doğrulama
- Kod tekrarını metotla giderme; iyi metot adı
- Ara sınav haftası: tarih ve yer bölümce ilan edilecek; kırmızı bölge
- Ara sınava hazırlık: kod izleme, boşluk doldurma, portfolyodan 10 puanlık soru
- KT2: gözcü değerle biten menü döngüsü, girdi doğrulama (27 Kasım Cuma 23.59)

## Temel Kavramlar

- **Kapsam (scope)**: Bir değişkenin görülebildiği kod bölgesi.
- **Yerel değişken**: Metot içinde tanımlanan, metot bitince yok olan değişken.
- **Çağrı yığını (call stack)**: Aktif metot çağrılarının üst üste dizildiği bellek bölgesi.
- **Değer ile geçirme**: Argümanın kopyası gönderilir; ilkel tiplerde çağıranın değişkeni değişmez.
- **Artımlı geliştirme**: Her seferinde küçük bir parça ekleyip test etme.

## Sahadan Örnekler

- StackOverflowError: bir metodun kendini sonsuz çağırması yığını taşırır; Stack Overflow sitesinin adı buradan gelir.
- Profesyonel ekiplerde her metot için otomatik test yazılır (JUnit); artımlı geliştirme bu alışkanlığın ilk adımıdır.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 9](/laboratuvar/lab-09). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
