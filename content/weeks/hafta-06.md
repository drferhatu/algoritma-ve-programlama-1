---
week: 6
title: "Döngüler I: while, do-while, for ve Gözcü Değer"
topic: "Tekrar yapıları: while, do-while ve for döngüleri; sayaç kontrollü ve gözcü değer (sentinel) kontrollü döngüler; girdi doğrulama döngüsü"
description: "Bilgisayarın asıl gücü tekrar: üç döngü türü, hangi durumda hangisi, gözcü değerle biten döngü ve kullanıcıyı doğru girdiye zorlayan döngü."
module: m2
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "while"
  - "do-while"
  - "for"
  - "gözcü değer"
  - "sentinel"
  - "döngü"
objectives:
  - "while, do-while ve for döngülerini yazar; aralarındaki farkı bir cümleyle söyler."
  - "Sayaç kontrollü ve gözcü değer kontrollü döngü tasarlar."
  - "Girdi doğrulama döngüsü (geçerli sayı girene kadar sor) yazar."
  - "Sonsuz döngü ve bir eksik/bir fazla (off-by-one) hatalarını tanır ve düzeltir."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
---

## Haftanın Bulmacası

Sayı tahmin oyunu kağıtta: aklımda 1-100 arası bir sayı var, yalnızca "büyük/küçük" diyorum. En kötü durumda kaç soruda bulursunuz? (7.) Bu, hem döngünün hem de 11. haftadaki ikili aramanın tohumu.

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **Tekrar yapıları: while, do-while ve for döngüleri; sayaç kontrollü ve gözcü değer (sentinel) kontrollü döngüler; girdi doğrulama döngüsü**

İşlenecek başlıklar:

- Neden döngü: 100 kez println yazmamak için
- while döngüsü: koşul, gövde, güncelleme; sonsuz döngü
- do-while: en az bir kez çalışan döngü; menüler için
- for döngüsü: başlangıç, koşul, artış; hangi döngü ne zaman
- Sayaç kontrollü döngü; toplam ve ortalama hesaplama
- Gözcü değer (sentinel) kontrollü döngü: 0 girilene kadar topla
- Girdi doğrulama döngüsü: geçerli değere kadar tekrar sor
- Sayı tahmin oyunu (while), çıkarma quiz'i (while)
- Sayısal hata: 0.1'i on kez toplamak; double ile eşitlik karşılaştırmama
- Off-by-one hataları

## Temel Kavramlar

- **Döngü (loop)**: Bir bloğu koşul doğru olduğu sürece tekrar çalıştırma.
- **Sayaç kontrollü döngü**: Kaç kez döneceği baştan belli.
- **Gözcü değer (sentinel)**: Girdinin bittiğini bildiren özel değer; ör. 0 veya -1.
- **do-while**: Koşulu sonda kontrol eden, gövdesi en az bir kez çalışan döngü.
- **Sonsuz döngü**: Koşulu hiç false olmayan döngü; güncelleme satırı unutulunca.

## Sahadan Örnekler

- Kasa yazılımı: ürün okut, okut, okut, "toplam" tuşu gözcü değerdir.
- Şifre denemesi: doğru girene kadar sor ama üç denemeden sonra kilitle; iki koşullu döngü.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 6](/laboratuvar/lab-06). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
