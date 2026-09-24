---
week: 7
title: "Döngüler II: İç İçe Döngü, break/continue, EBOB ve Monte Carlo"
topic: "İç içe döngüler ve desen yazdırma; break ve continue; Euclid EBOB algoritması, asal sayılar ve Monte Carlo ile pi tahmini"
description: "Döngünün içinde döngü: çarpım tablosu ve yıldız desenleri, döngüyü erken bitiren break ve turu atlayan continue; klasik algoritmalar EBOB ve asal sayı; rastgele sayılarla pi."
module: m2
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "iç içe döngü"
  - "break"
  - "continue"
  - "EBOB"
  - "Euclid"
  - "asal"
  - "Monte Carlo"
objectives:
  - "İç içe döngü ile tablo ve desen yazdırır; dış ve iç döngünün rolünü ayırt eder."
  - "break ve continue'yu yerinde kullanır, kötüye kullanımını tanır."
  - "Euclid EBOB algoritmasını elle izler ve Java'da yazar."
  - "Monte Carlo yöntemiyle pi tahmininin mantığını açıklar."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
  - "Math.random"
---

## Haftanın Bulmacası

Elle Euclid: 252 ve 105'in EBOB'unu kağıtta bölme kalanıyla bulun (kaç adım?). Sonra aynı işi "1'den küçüğe kadar hepsini dene" yöntemiyle yapmayı düşünün: kaç adım? İki algoritma, aynı cevap, çok farklı emek.

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **İç içe döngüler ve desen yazdırma; break ve continue; Euclid EBOB algoritması, asal sayılar ve Monte Carlo ile pi tahmini**

İşlenecek başlıklar:

- İç içe döngü: dış döngü satır, iç döngü sütun; çarpım tablosu
- Yıldız desenleri: üçgen, piramit; printf ile hizalama
- break: döngüyü bitir; continue: bu turu atla; etiketli break'e kısa bakış
- Sayı tahmin oyununu break ile yazmak
- EBOB: kaba kuvvet (v1), geriye doğru (v2), Euclid (v3); adım sayısı karşılaştırması
- Asal sayı bulma ve iyileştirme (kareköke kadar)
- Monte Carlo ile pi: rastgele nokta, çeyrek daire
- Gelecek değer / faiz tablosu örneği
- Döngü tasarım stratejisi: önce bir tur elle, sonra genelle

## Temel Kavramlar

- **İç içe döngü**: Bir döngünün gövdesinde başka bir döngü; toplam tur = dış × iç.
- **break**: İçinde bulunduğu döngüyü hemen bitirir.
- **continue**: Kalan gövdeyi atlayıp sonraki tura geçer.
- **Euclid algoritması**: EBOB(a, b) = EBOB(b, a mod b); 2300 yıllık, hâlâ en iyisi.
- **Monte Carlo**: Rastgele deneylerle sayısal tahmin yapma yöntemi.

## Sahadan Örnekler

- Kriptografi: RSA'nın içinde Euclid'in genişletilmiş hali çalışır; her HTTPS bağlantısı bu döngüden geçer.
- Görüntü işleme: bir fotoğrafın her pikseli satır-sütun iç içe döngüsüyle gezilir; 12 megapiksel = 12 milyon tur.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 7](/laboratuvar/lab-07). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
