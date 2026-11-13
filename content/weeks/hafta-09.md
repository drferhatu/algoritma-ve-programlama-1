---
week: 9
title: "Metotlar I: Tanım, Parametre, return ve Math"
topic: "Metot tanımlama ve çağırma, void ve değer döndüren metotlar, parametre ve argüman, çalışma akışı, Math sınıfı ve kompozisyon"
description: "Programı parçalara bölmenin ilk aracı: metot. Tarifin içindeki tarifi ayrı yazmak, parametreyle genelleştirmek, return ile sonucu geri almak. Ara sınav 24 Kasım Salı 17.00'de; metotlar sınav kapsamında değil."
module: m3
semester: 1
exam: false
status: taslak
changeNote: "Program güncellemesi: metotlar I 20 Kasım'da işlenir. Ara sınav 24 Kasım Salı 17.00'de; bu haftanın konusu kapsam dışıdır."
tags:
  - "ara sınav"
  - "metot"
  - "parametre"
  - "return"
  - "void"
  - "Math"
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

> [!uyari] Ara sınav 24 Kasım Salı 17.00
> Ara sınav **24 Kasım Salı 17.00-18.00**; A şubesi A304-306, B şubesi A306 ve A404-406. Kağıt üzerinde, kırmızı bölge. Kapsam **1-8. haftalar** (döngüler II dahil); bu haftanın konusu olan metotlar kapsam dışıdır. Bu dönem sınavlar derslerle birlikte yapılıyor, yani bu Cuma dersi ve labları her zamanki saatinde. Kod izleme, boşluk doldurma, hata sayma, program tamamlama ve KT1 sürümünüzden 10 puanlık portfolyo sorusu. Plan: [/vize-plani](/vize-plani).

## Haftanın Bulmacası

Tarifin içindeki tarif: kağıttaki kek tarifinde "sosu hazırla" adımı üç yerde geçiyor. Sosu ayrı bir kağıda yazın, tarifte yalnızca adını çağırın. Şeker miktarını her seferinde farklı istiyorsanız? İşte parametre.

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
- Ara sınav: 24 Kasım Salı 17.00 (A: A304-306, B: A306 ve A404-406); kırmızı bölge, metotlar kapsam dışı
- Portfolyo: KT2 (menü döngüsü ve girdi doğrulama) gelecek hafta, 27 Kasım Cuma 23.59'da toplanır

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

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 9](/laboratuvar/lab-09). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
