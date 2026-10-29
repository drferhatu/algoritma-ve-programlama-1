---
week: 14
title: "String İşlemleri, Nehir Bulmacası ve Üç Dil: Dönem Kapanışı"
topic: "char tipi ve Unicode, String'in değişmezliği, length/charAt/substring/indexOf/equals, karakter sayma ve palindrom; 1. haftanın nehir bulmacasını dizilerle kodlama; aynı algoritmanın Java, Python ve C sürümleri; dönemin özeti ve KT4 son teslim"
description: "Metin de bir dizidir: karakterler, String metotları ve metin algoritmaları. Dönemin kapanışı: 1. haftada elle çözdüğünüz nehir bulmacasını bu kez durum dizisiyle Java'da yazıyor, sonra aynı algoritmayı yapay zekayla Python ve C'de görüyoruz: sözdizimi değişir, algoritma değişmez. Portfolyo son teslimi (KT4) 25 Aralık Cuma 23.59."
module: m4
semester: 1
exam: false
status: taslak
changeNote: "Bayram nedeniyle bir hafta ötelendi: String dersi 25 Aralık'a kaydı ve eski 14. haftanın 'aynı algoritma üç dil' bölümüyle birleştirildi."
milestone: "KT4"
tags:
  - "String"
  - "char"
  - "charAt"
  - "substring"
  - "equals"
  - "palindrom"
  - "nehir bulmacası"
  - "Python"
  - "C"
  - "KT4"
  - "özet"
objectives:
  - "char ile int ilişkisini ve String'in değişmez olduğunu açıklar."
  - "length, charAt, substring, indexOf, equals, toUpperCase metotlarını kullanır; == ile equals farkını bilir."
  - "Karakter sayma, ters çevirme ve palindrom algoritmalarını yazar."
  - "Nehir bulmacasını durum dizisi, hamle döngüsü ve kısıt kontrolü ile Java'da kodlar."
  - "Aynı algoritmanın Java, Python ve C sürümlerinde değişen ve değişmeyen kısımları işaretler; tip sistemi, derleme/yorumlama ve sözdizimi farklarını bir tabloyla açıklar."
  - "Portfolyo uygulamasını README ve AI beyanıyla teslim eder; dönem boyunca öğrenilen yapıları (seçim, döngü, metot, dizi) tek bir programda gösterir."
tools:
  - "JDK 21"
  - "VS Code"
  - "GitHub Codespaces"
  - "Python"
  - "C"
---

## Haftanın Bulmacası

Nehir bulmacası geri döndü. 1. haftada sakladığınız kağıdı çıkarın. Bu kez durumu dört kutulu bir boolean dizisi olarak yazın: [çiftçi, tilki, tavuk, mısır] karşı kıyıda mı? Her hamle bir kutuyu (ve çiftçiyi) çevirir; kısıtlar iki if. Kağıtta kodlayın, sonra Java'da.

> [!uyari] KT4 son teslim: 25 Aralık Cuma 23.59
> Portfolyonun son sürümü **KT4** bugün **25 Aralık Cuma 23.59**'da toplanır: README tam, `AI-BEYANI.md` dolu, çalışan son sürüm; çekirdek algoritma yapay zeka yardımıyla Python ve C'ye çevrilmiş (`uc-dil/` klasörü) ve üç dil arasındaki farklar bir paragrafta anlatılmış. Finaldeki 15 puanlık soru bu sürümden gelir. Lab 14'te (30-31 Aralık) bir metodunuzu 30 saniyede anlatacaksınız. Ayrıntı: [Proje](/proje), [AI beyanı](/rehber/ai-beyani).

## Ders Notları

> [!not] Hazırlanıyor
> Bu haftanın ders notları hazırlanıyor; ders günü bu sayfa yansıda açık olacak. Şimdilik konu başlıkları: **char tipi ve Unicode, String'in değişmezliği, length/charAt/substring/indexOf/equals, karakter sayma ve palindrom; 1. haftanın nehir bulmacasını dizilerle kodlama; aynı algoritma üç dilde; dönemin özeti**

İşlenecek başlıklar:

- char: 16 bit sayı, Unicode; karakter aritmetiği ('A' + 1)
- String nesneleri değişmezdir (immutable); her değişiklik yeni String
- length(), charAt(), substring(), indexOf(), contains()
- Karşılaştırma: equals ve compareTo; == neden yanlış
- toUpperCase, toLowerCase, trim, split
- Karakter sayma; String'i char dizisine çevirme; ters çevirme; palindrom
- Doubloon problemi (Think Java 7.9): dizi ile harf sayma
- Nehir bulmacasının kodlanması: durum dizisi, güvenli mi metodu, hamle döngüsü, çözüm yolu yazdırma
- Yapay zekanın 1. haftada yazdığı çözümle karşılaştırma

### Aynı algoritma, üç dil: Java, Python ve C

Üç kağıt, üç dil: aynı EBOB algoritması Java, Python ve C ile yazılmış. Renkli kalemle işaretleyin: yeşil = üç dilde aynı olan satırlar, kırmızı = yalnızca sözdizimi farkı, mavi = gerçekten farklı düşünülen yer. Mavi neredeyse hiç çıkmaz; ders bu.

- Dil yüzeydir, algoritma özdür: aynı akış diyagramı üç dil
- Java, Python, C karşılaştırma: tip bildirimi, noktalı virgül ve girinti, derleme ve yorumlama, bellek
- Yapay zeka ile çeviri: istem yazma, çıktıyı doğrulama (aynı girdiye aynı çıktı)
- Çeviride sık kırılan yerler: tam sayı bölmesi, dizi sınırı, karakter/String farkı
- KT4 teslim: README, AI beyanı, üç dilli çekirdek
- Finale hazırlık: 15 puanlık portfolyo metot sorusu nasıl gelir
- Dönemin özeti: durum, hamle, kısıt, hedef; 1. haftadan 14. haftaya
- Algo-II'de sizi ne bekliyor: nesneler, sınıflar, veri yapıları

## Temel Kavramlar

- **char**: Tek karakter; aslında bir sayı.
- **Değişmezlik (immutability)**: String bir kez oluşunca değişmez; metotlar yeni String döndürür.
- **charAt(i)**: i. karakteri verir; 0'dan başlar.
- **equals**: İçerik karşılaştırması; == referans karşılaştırır.
- **Durum dizisi**: Bulmacanın anlık durumunu tutan dizi; 1. haftanın "kim hangi kıyıda" sorusu.
- **Sözdizimi (syntax) / anlam (semantics)**: Dilden dile değişen yazım / değişmeyen algoritma.
- **Statik / dinamik tip**: Java ve C tipi baştan ister; Python çalışırken çıkarır.
- **Derleme / yorumlama**: C ve Java derlenir; Python satır satır yorumlanır.
- **AI beyanı**: Hangi araç, ne için, hangi kısım sizin, hangi hata yakalandı.

## Sahadan Örnekler

- Arama motoru ve otomatik tamamlama: yazdığınız her harf bir String algoritmasını tetikler.
- DNA dizileri: ACGT harflerinden oluşan devasa String'ler; gen arama tam olarak indexOf'un akıllı halidir.
- Gerçek projelerde diller karışır: web arayüzü JavaScript, sunucu Java, veri analizi Python, cihaz sürücüsü C; algoritma hepsinde aynıdır. Kod çevirisi bugün yapay zekanın en iyi yaptığı işlerden biri; doğrulamak ise hâlâ mühendisin işi.

## Laboratuvar

Bu haftanın laboratuvarı bir hafta sonra yapılır (A Çarşamba 13.15, B Perşembe 15.15): [Lab 14](/laboratuvar/lab-14). Tarihler için [Ders Hakkında](/ders-hakkinda) sayfasındaki takvime bakın.
