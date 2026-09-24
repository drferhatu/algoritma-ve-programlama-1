---
week: 2
title: "Akış Diyagramı, Sözde Kod ve Java Program Yapısı"
topic: "Algoritmayı akış diyagramı ve sözde kodla ifade etme; bir Java programının anatomisi (class, main), derleme süreci (JDK, javac, bytecode) ve üç hata türü"
description: "Kağıttaki adımları akış diyagramına ve sözde koda çeviriyor; ilk kez tam bir Java dosyasını derleyip çalıştırıyor, sözdizimi, çalışma zamanı ve mantık hatalarını ayırt ediyoruz."
module: m1
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "akış diyagramı"
  - "sözde kod"
  - "JDK"
  - "javac"
  - "main"
  - "hata türleri"
objectives:
  - "Basit bir algoritmayı standart sembollerle akış diyagramı ve sözde kod olarak yazar."
  - "Bir Java dosyasının zorunlu iskeletini (class, main) açıklar; javac ile derleyip java ile çalıştırır."
  - "JDK, JVM ve bytecode kavramlarını bir cümleyle söyler."
  - "Sözdizimi, çalışma zamanı ve mantık hatalarını örnekle ayırt eder."
tools:
  - "Java Playground"
  - "JDK 21"
  - "VS Code"
---

## Haftanın Bulmacası

Tahmin et, sonra çalıştır: yansıdaki 12 satırlık akış diyagramını kağıt üzerinde elle izleyip çıktıyı yazın; sonra aynı program Playground'da çalışır ve tahminler karşılaştırılır. Ardından "insan bilgisayar" yeniden tahtada: bu kez komutları sözde kodla veriyorsunuz.

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **Algoritmayı akış diyagramı ve sözde kodla ifade etme; bir Java programının anatomisi (class, main), derleme süreci (JDK, javac, bytecode) ve üç hata türü**

İşlenecek başlıklar:

- Algoritmanın özellikleri: başlangıç, sonluluk, kesinlik, en az adım
- Akış diyagramı sembolleri: başla/bitir, işlem, karar, girdi/çıktı, ok
- Üç temel yapı: sıra, seçim, tekrar (her program bu üçünden kurulur)
- Sözde kod (pseudocode) yazım kuralları; Türkçe sözde kod örnekleri
- Çizim araçları: kağıt, draw.io
- Bir Java programının anatomisi: class, main, süslü parantezler, noktalı virgül
- JDK, JRE, JVM; kaynak kod → javac → bytecode (.class) → java
- Programlama stili: girinti, isimlendirme, yorum satırı
- Üç hata türü: sözdizimi (derleyici yakalar), çalışma zamanı (çöker), mantık (sessizce yanlış)
- Hata avı ritüelinin ilk turu: 15 satırlık bilerek hatalı program

## Temel Kavramlar

- **Akış diyagramı (flowchart)**: Algoritmanın sembollerle çizimi; elmas karar, dikdörtgen işlem.
- **Sözde kod (pseudocode)**: Programlama diline benzeyen ama derlenmeyen, insan için yazılmış adımlar.
- **Derleyici (javac)**: Kaynak kodu bytecode'a çeviren program; hata varsa çevirmez.
- **JVM**: Bytecode'u çalıştıran sanal makine; Java'nın "bir kez yaz, her yerde çalıştır" sözünün sebebi.
- **Mantık hatası**: Derlenen ve çalışan ama yanlış sonuç veren program; en sinsi hata.

## Sahadan Örnekler

- Ariane 5 (1996): 64 bitlik sayıyı 16 bite sığdırmaya çalışan tek satır, 370 milyon dolarlık roketi patlattı; çalışma zamanı hatasının en pahalı örneği.
- Havayolu check-in sistemleri: her yolcu akışı bir akış diyagramıdır; "bagaj 23 kg'dan fazla mı?" elması her gün milyonlarca kez değerlendirilir.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 2](/laboratuvar/lab-02). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
