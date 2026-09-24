---
week: 10
title: "Tek Boyutlu Diziler I: Oluşturma, Gezinme ve Referans"
topic: "Dizi tanımlama ve oluşturma, indeks ve length, dizide gezinme (for ve for-each), rastgele değerlerle doldurma, dizi referansı ve bellek gösterimi"
description: "Yüz sayıyı yüz değişkende tutmak yerine tek dizide: oluşturma, indeksle erişim, gezinme, en büyüğü bulma (1. haftanın insan bilgisayarı geri dönüyor) ve dizinin bir referans olduğu gerçeği."
module: m4
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "dizi"
  - "array"
  - "indeks"
  - "length"
  - "for-each"
  - "referans"
objectives:
  - "Dizi tanımlar, oluşturur ve başlangıç değeri verir; length'i kullanır."
  - "for ve for-each ile diziyi gezer; toplam, ortalama, en büyük/en küçük bulur."
  - "ArrayIndexOutOfBoundsException'ı tanır ve sebebini söyler."
  - "Dizinin bir referans olduğunu bellek çizimiyle açıklar; iki değişkenin aynı diziyi paylaşmasını fark eder."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
  - "GitHub Codespaces"
---

## Haftanın Bulmacası

Posta kutuları: tahtada 0'dan 7'ye numaralı sekiz kutu, içlerinde sayılar. "İnsan bilgisayar" 1. haftadaki tarifle en büyüğü bulur; bu kez kutu numarası (indeks) ve "kutu kalmadı mı?" (length) kelimeleriyle. Sonra aynı tarif for döngüsüyle koda döner.

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **Dizi tanımlama ve oluşturma, indeks ve length, dizide gezinme (for ve for-each), rastgele değerlerle doldurma, dizi referansı ve bellek gösterimi**

İşlenecek başlıklar:

- Neden dizi: 100 sayının ortalaması ve ortalamanın üstündekiler
- Dizi tanımlama, new ile oluşturma, başlangıç değeri listesi
- İndeks 0'dan başlar; length; sınır dışı erişim hatası
- Gezinme: for ile; for-each ile; ne zaman hangisi
- Toplam, ortalama, min/max, belirli değeri sayma
- Rastgele dizi ve histogram (Think Java 7.7)
- Dizi bir referanstır: bellek çizimi; a = b iki isim tek dizi
- Kart destesi çekme, sayı analizi örnekleri (geçen yıl)

## Temel Kavramlar

- **Dizi (array)**: Aynı tipte sabit sayıda değeri yan yana tutan yapı.
- **İndeks**: Elemanın sıra numarası; 0'dan length-1'e.
- **length**: Dizinin eleman sayısı; alan, metot değil (parantez yok).
- **for-each**: Elemanları indekse dokunmadan gezen döngü.
- **Referans**: Dizi değişkeni diziyi değil, dizinin bellekteki yerini tutar.

## Sahadan Örnekler

- Ses dosyası: bir şarkı saniyede 44.100 sayıdan oluşan devasa bir dizidir; ses seviyesi, her elemanı bir katsayıyla çarpan döngüdür.
- Sensör verisi: bir aracın son 1000 hız ölçümü dairesel bir dizide tutulur; ortalama ve en yüksek değer sürekli hesaplanır.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 10](/laboratuvar/lab-10). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
