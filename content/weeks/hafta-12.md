---
week: 12
title: "Çok Boyutlu Diziler: Matris, Sudoku ve Hava Durumu"
topic: "İki boyutlu dizi tanımlama, satır ve sütun, iç içe döngüyle gezinme, satır/sütun toplamları, sudoku doğrulama ve hava durumu tablosu örnekleri; düzensiz diziler"
description: "Tablo şeklindeki veriler: matris, mesafe tablosu, sudoku tahtası. İki boyutlu dizi ile 7. haftanın iç içe döngüsü buluşuyor."
module: m4
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "iki boyutlu dizi"
  - "matris"
  - "sudoku"
  - "iç içe döngü"
  - "hava durumu"
objectives:
  - "İki boyutlu dizi tanımlar, oluşturur ve başlangıç değeri verir; length'in satır/sütun anlamını bilir."
  - "İç içe döngüyle 2B diziyi gezer; satır ve sütun toplamlarını hesaplar."
  - "Sudoku çözümünü doğrulayan programı parçalara bölerek yazar."
  - "Düzensiz (ragged) diziyi tanır."
tools:
  - "JDK 21"
  - "VS Code"
  - "GitHub Codespaces"
---

## Haftanın Bulmacası

Kağıt sudoku: sınıfa dolu bir sudoku dağıtılır; ikili gruplar bir satırı, bir sütunu ve bir 3×3 kutuyu elle doğrular. Doğrulama adımlarını yazın: kaç iç içe döngü gerekiyor?

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **İki boyutlu dizi tanımlama, satır ve sütun, iç içe döngüyle gezinme, satır/sütun toplamları, sudoku doğrulama ve hava durumu tablosu örnekleri; düzensiz diziler**

İşlenecek başlıklar:

- Neden 2B dizi: mesafe tablosu, sınav sonuçları (öğrenci × soru), sudoku
- Tanımlama: int[][] m = new int[3][4]; m.length ve m[0].length
- Başlangıç değeri listesiyle oluşturma
- İç içe döngüyle gezinme, yazdırma, toplam
- Satır toplamları, sütun toplamları, en büyük satır
- Sınav notlandırma (02_gradeExam), en yakın nokta (03_findNearest)
- Sudoku doğrulama (04_sudoku): satır, sütun, kutu
- Hava durumu analizi (06_weather, WeatherAnalyzer): günlük ortalama
- Düzensiz diziler; 2B diziyi metoda gönderme

## Temel Kavramlar

- **İki boyutlu dizi**: Dizilerin dizisi; m[satır][sütun].
- **Satır / sütun**: İlk indeks satır, ikinci sütun; m.length satır sayısı.
- **Düzensiz dizi (ragged)**: Her satırın uzunluğu farklı olabilir.
- **Matris**: Sayısal 2B dizi; toplama, çarpma gibi işlemler.
- **Doğrulama**: Verinin kurallara uyduğunu kontrol eden algoritma.

## Sahadan Örnekler

- Dijital görüntü: her fotoğraf piksellerden oluşan 2B (renkli ise 3B) bir dizidir; Instagram filtresi bu dizinin üstünde iç içe döngüdür.
- Satranç motoru ve oyun tahtaları: 8×8 dizi; her hamle bir hücre değişimi, her kural bir doğrulama döngüsü.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 12](/laboratuvar/lab-12). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
