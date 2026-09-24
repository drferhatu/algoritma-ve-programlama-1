---
week: 8
title: "Metotlar I: Tanım, Parametre, return ve Math"
topic: "Metot tanımlama ve çağırma, void ve değer döndüren metotlar, parametre ve argüman, çalışma akışı, Math sınıfı ve kompozisyon"
description: "Programı parçalara bölmenin ilk aracı: metot. Tarifin içindeki tarifi ayrı yazmak, parametreyle genelleştirmek, return ile sonucu geri almak. KT2 teslim haftası."
module: m3
semester: 1
exam: false
status: taslak
changeNote: ""
milestone: "KT2"
tags:
  - "metot"
  - "parametre"
  - "return"
  - "void"
  - "Math"
  - "KT2"
objectives:
  - "void ve değer döndüren metot tanımlar, çağırır; çalışma akışını izler."
  - "Parametre ile argüman farkını açıklar; çok parametreli metot yazar."
  - "Math sınıfının sık metotlarını (pow, sqrt, abs, max, random) kullanır."
  - "Tekrar eden kodu metoda çıkararak programı kısaltır."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
  - "GitHub Codespaces"
---

## Haftanın Bulmacası

Tarifin içindeki tarif: kağıttaki kek tarifinde "sosu hazırla" adımı üç yerde geçiyor. Sosu ayrı bir kağıda yazın, tarifte yalnızca adını çağırın. Şeker miktarını her seferinde farklı istiyorsanız? İşte parametre.

> [!uyari] KT2 teslim haftası
> Bu hafta portfolyo kilometre taşı **KT2** teslim edilir; son an, bu haftanın laboratuvar saatidir. Ayrıntı: [Ders Hakkında · Portfolyo](/ders-hakkinda).

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **Metot tanımlama ve çağırma, void ve değer döndüren metotlar, parametre ve argüman, çalışma akışı, Math sınıfı ve kompozisyon**

İşlenecek başlıklar:

- Metot nedir; neden: tekrar azaltma, okunabilirlik, test edilebilirlik
- İlk metot: newLine, threeLine; çağrı ve tanım farkı
- Çalışma akışı (flow of execution): main'den başlar, çağrıya gider, geri döner
- Parametreler ve argümanlar; çok parametreli metotlar
- void metot ile değer döndüren metot; return ifadesi
- Math sınıfı: pow, sqrt, abs, max, min, round, random
- Kompozisyon: metot içinde metot çağırma; ifadelerin içinde çağrı
- Metot imzası; aşırı yükleme (overloading) kısa bakış
- KT2: gözcü değerle biten menü döngüsü, girdi doğrulama

## Temel Kavramlar

- **Metot (method)**: Adı olan, tekrar çağrılabilen kod bloğu.
- **Parametre / argüman**: Tanımda beklenen değişken / çağrıda gönderilen değer.
- **return**: Metodun sonucunu çağırana geri verip metodu bitirir.
- **void**: Değer döndürmeyen metot.
- **Kompozisyon**: Küçük metotları birleştirerek büyük iş yapmak.

## Sahadan Örnekler

- Kütüphaneler: Math.sqrt'yi siz yazmadınız; her programlama dili milyonlarca hazır metottan oluşan bir ekosistemdir.
- Uçuş kontrol yazılımı: her hesaplama küçük, test edilmiş metotlardır; Apollo yazılımının önceliklendirmesi de metot çağrılarıyla çalışıyordu.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 8](/laboratuvar/lab-08). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
