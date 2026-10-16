# Hafta 4 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 16 Ekim 2026 Cuma · A şubesi 09.15 (fiilen 09.30 başla, 10.30-10.45 arası bitir) · B şubesi 13.15 (fiilen 13.30 başla, aynı akış, 14.30-14.45 bitir).
**Tek oturum, 60-75 dakika.** Slayt yok; yansıda `/haftalar/hafta-04` açık. İkinci ekranda Java Playground sekmesi ve **Codespaces ya da yerel terminal** (üç tam dosya için). Poll Everywhere soruları `docs/hafta-04-polleverywhere.md`.
**Slogan:** program ilk kez yol ayrımında.
**Üslup notu:** 3. haftanın hikayeli anlatımı tuttu; bu hafta aynı tonda ama örnek sayısı iki kat. Her kavram önce 3-5 cümlelik sahne, sonra kod. Sahneler sayfada yazılı; derste sahneyi anlat, kodu sonra aç, **her kutuda önce tahmin, sonra Run**. Bu hafta 10 CodeTry var, hepsini çalıştırmaya süre yetmez; aşağıdaki tabloda "canlı" yazanlar çalıştırılır, kalanı "evde çalıştırın" denir.

## Hazırlık (derse girmeden)

- Yansı: site sayfası + Playground sekmesi + terminalde `ArtikYil.java`, `EnBuyuk.java`, `Taksi.java` önceden kaydedilmiş ve bir kez derlenmiş. ChatGPT sekmesinde "Java'da sarkan else nedir, bir örnekle açıkla" yazılı, Enter'a basılmamış.
- Yedek: üç tam dosyanın terminal çıktılarının ekran görüntüsü (2024 / 1900 / 2000; 3 42 7 / -5 -2 -9; 4 14 / 4 3).
- Kağıt: her sıraya A5 (karar ağacı için yeter). Tahta kalemi iki renk: siyah elmas ve kutular, kırmızı izlenen yol (85 puanın yolunu kırmızıyla çiz).
- Geçen haftadan: Poll 5 duvarından 2-3 cümle (açılışta oku); Poll 1'de "para: double" diyenlerin yüzdesi (açılışta tek cümle: "geçen hafta yüzde X'iniz double dedi, bugün o yüzdeyi düşürmeye devam"); Lab 3'te en çok takılan nokta (lab sorumlu hocasından al; muhtemelen Enter tuzağı ve VKİ merdiveni; merdiven bloğunda kullan).
- Poll Everywhere "Hafta 4" grubu etkin.
- Hata avı programı yansıda satır numaralı görünmeli; 9, 12, 14 numaraları tahtaya yazmaya hazır ol.
- Lab 3 son teslim **bugün 23.59**: açılışta ve kapanışta söyle.

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Öğrenci ne yapar | Tahtaya yazılacak |
|---|---|---|---|---|
| 0-8 | Açılış + harf notu ağacı | Geçen haftanın duvarından 2-3 cümle (1 dk). "Lab 3 son teslim bu akşam 23.59." Bulmacayı oku; 4 dk ver. Tahtaya ağacı çiz (5 elmas, 5 yaprak), 85'in yolunu kırmızıyla izle. Zor soru: ağacı ters çevir, ilk elmasa "60 ve üstü mü?" yaz, 85'i yürüt, D'ye vardır. Diyagramı aç (h04-harf-agaci). İki kuralı tahtaya yaz. | Kağıda ağacı çizer; 85, 59, 90'ı izler; ters ağaçta 85'i tartışır | Sol üst: **SIRAYLA SOR · İLK EVETTE DUR** · Ağaç (siyah) · 85'in yolu (kırmızı) · Ters ağaç: `85 → D ✗` |
| 8-12 | Apollo 11 | Hikayeyi anlat (sayfadaki üç paragraf, 3 dk): 1202 alarmı, radar anahtarı, Hamilton ekibinin öncelik kararı, "Go". Kilit cümle: "İyi bir karar yapısı kriz anında ne yapacağını bilen yapıdır." Kod yok, Playground yok. | Dinler | `APOLLO 11 · 1202 · "ya kapasite yetmezse?" → yıllar önce koda yazıldı` |
| 12-22 | boolean ve `==` | Kantin kasası sahnesi: "Öğrenci misiniz?" evet/hayır, üçüncüsü yok. Tabloyu aç, altı operatör; "eşittir hep sağda". **Canlı:** CodeTry "Altı soru, altı cevap": önce tahmin, sonra Run. "Hesap 50 mi?" ile "hesabı 50 yap" sahnesi. Poll 1 ("`if (x = 5)` ne olur?") oyla; **canlı:** CodeTry "Soru mu, emir mi?": `ogrenci = true` ile çalıştır, false olduğu halde indirim uygulandığını göster; sonra `if (puan = 85)` yazdır ve derleyici mesajını okut: "int ise bağırır, boolean ise susar." `== true` yazmayın: "evet mi, evet mi?" | Kağıda altı satırın sonucunu yazar; Playground'da ikisini çalıştırır | `boolean: true / false` · `== != < > <= >=` (eşittir sağda) · `hesap == 50 → SORU` · `hesap = 50 → EMİR` · `if (ogrenci == true) ✗ → if (ogrenci) ✓` |
| 22-30 | Tek yönlü if + if/else | Şemsiye sahnesi (3 cümle). Sözdizimi tahtaya; "süslü parantez her zaman, tek satır olsa bile; sebebini Yaygın Hatalar'da göreceksiniz." Diyagram h04-if. **Canlı:** CodeTry "Pozitif mi?" 7 ve -3; "-3'te sessiz kaldı, hayır cevabında bir şey yapmak istersek?" Güneş gözlüğü sahnesi; diyagram h04-if-else: "2. haftanın çift/tek elması." CodeTry "Çift mi tek mi" evde; **canlı:** CodeTry "Yetişkin mi?" `yas = 18`, sonra `>` yap: "sınır değeri, labda her dalla birlikte test." | Playground'da pozitif ve yetişkin kutuları; sınırı değiştirir | `if (koşul) { ... }` · `SÜSLÜ PARANTEZ HER ZAMAN` · `if / else: BİRİ MUTLAKA, İKİSİ ASLA` · `yas > 18` vs `yas >= 18` (18 nereye düşer?) |
| 30-40 | else-if merdiveni | "Beş cevap, iki yol yetmez; beş ayrı if yazarsak 85'e üç harf." Merdiven = else'in içine if/else. **Canlı:** CodeTry "Harf notu" 85, sonra **merdiveni ters çevirt** ve D'yi göster (Poll 2 önce). "Her basamak üstündekilerin hayır dediği varsayımıyla yazılır." VKİ: "Lab 3'te ezbere yazdınız, bugün kitapta"; CodeTry "VKİ" evde ya da hızlı. Uyarı kutusu: merdiven mi ardışık if mi? **Canlı:** CodeTry "Üç soruluk quiz": önce 3/3, sonra if'leri else if yapıp 1/3 göster: "Lab 4 Görev 5 bu." | Merdiveni ters çevirir, D görür; quiz kutusunda else if deneyini yapar | `else if` merdiveni (5 basamak, büyükten küçüğe) · `TERS SIRA → 85 = D` · `DIŞLAYAN → merdiven · BAĞIMSIZ → ardışık if` · `dogru++` |
| 40-50 | İç içe if + sarkan else | "Önce kapıdan gir, sonra odayı seç" sahnesi. Sinema gişesi: önce yaş, 18+ ise öğrenci sorusu. Diyagram h04-ic-ice. **Canlı:** CodeTry "Sinema bileti" üç yol (17/e, 20/e, 20/h). "Girinti yalnızca sizin için; Java paranteze bakar." Poll 3 ("sarkan else hangi if'e ait?") oyla; **canlı:** CodeTry "Sarkan else: tahmin edin": önce kağıda tahmin, sonra Run, "Cocuk bileti" görülsün, 20 yaşında. Kural: "else en yakın if'e aittir, girinti değiştirmez." Parantezli düzeltmeyi yaz ve çalıştır. | Üç yolu dener; sarkan else'te önce tahmin yazar, sonra çalıştırır, sonra parantezle düzeltir | `İÇ İÇE: önce kapı, sonra oda` · `else EN YAKIN if'E AİTTİR` · `GİRİNTİ ≠ PARANTEZ` · parantezli düzeltme |
| 50-60 | Üç tam dosya (terminalde canlı) | "Playground'da çalışmaz" uyarısı, terminale geç. `ArtikYil`: 2024, 1900, 2000, 2023 gir; üç kapı metaforu; "üç kat okunması zor, haklısınız, gelecek hafta 've' ile 'ya da' bunu tek satıra indirecek; labda üç katlı yazacaksınız." `EnBuyuk`: 3 42 7, sonra -5 -2 -9; "enBuyuk = 0 ile başlasaydık?" sor. `Taksi`: 4 14 → 110.00, 4 3 → 165.00; "karar ekrana yazmıyor, değişkeni değiştiriyor"; `final` sabitler. "Lab 4'ün üç görevi bu üç program." | Terminali izler; her girdi için hangi dal çalıştığını yanındakine söyler | `2024 ✓ · 1900 ✗ · 2000 ✓ · 2023 ✗` (üç kapı) · `enBuyuk = a (0 değil!)` · `110.00 / 165.00` · `karar → değişkeni değiştir → en sonda printf` |
| 60-67 | Yaygın hatalar hızlı tur + hata avı | Altı tuzağı yansıda hızlı geç (her biri 30 sn, kodu okut, "ne yazar?" sor): `;` → her zaman Pozitif; `= true`; Poll 4 (`0.1+0.2 == 0.3`?) oyla ve 3. tuzağı çalıştır; bloksuz if → "Bilet kesildi"; ters merdiven; girinti yalanı. "Altısı da derlenir." Hata avı: "Üç hata, üç dakika, bulun, düzeltmeyin." Sıra: 9 (`= true`), 12 (`;`), 14-20 (merdiven sırası). "Üçü de çalışıyor görünür; 3.8'e 'tam' beklediğinizi bildiğiniz için fark edersiniz." | Yansıdaki kodları okur, çıktıyı tahmin eder; hata avında satır numarası yazar | `6 TUZAK, 6'SI DA DERLENİR` · `SATIR 9: = true` · `SATIR 12: if (...);` · `SATIR 14: merdiven ters` |
| 67-72 | Kantin + gelecek hafta | Sözde kodu aç: dört kat iç içe; "doğru çalışıyor ama altı ay sonra beşinci katı nereye açacaksınız?" "Gelecek hafta iki araç: 've' / 'ya da' (mantıksal operatörler) saat kontrolünü tek satıra indirir, `switch` on ürünlük merdiveni kaldırır. İkisi de yeni bir şey yapmaz, bugünkü ağacı kısa yazar." | Sözde kodda dört elması sayar | `4 KAT İÇ İÇE → OKUNMAZ` · `GELECEK HAFTA: ve / ya da · switch · KT1` |
| 72-75 | YZ anı, kapanış | Süre varsa ChatGPT'ye sarkan else sorusunu gönder, örneği Playground'a yapıştır, sınıf çıktıyı önce tahmin eder, sonra çalıştır; "kodu doğrulamanın yolu çalıştırmak, ama ne beklediğinizi bilmek zorundasınız." Trafik ışığı: "Labda kavram sorulur, program yazdırılmaz." Poll 5 (tek cümle). Kapanış: Lab 3 bu akşam 23.59; Lab 4 21-22 Ekim; gelecek hafta KT1 ve konu dağıtımı duyurulacak, "uygulamanız en az bir if/else ile karar verecek." | Anket | `Lab 3 son teslim BU AKŞAM 23.59` · `Lab 4: 21 Ekim (A) · 22 Ekim (B)` · `Gelecek hafta: KT1 + konu dağıtımı` |

## Kilit cümleler (blok blok)

**Açılış.** "Şimdiye kadar yazdığınız her program tek yoldan yürüdü. Bugün ilk kez yol ayrımına gelecek." · "Karar yapısının iki kuralı var: soruları sırayla sorar, ilk evette durur. Sırayı bozarsanız 85 puan D alır ve derleyici bunu göremez."

**Apollo.** "Alarm 1202: bilgisayarın yapacak işi kapasitesini aşıyor. İniş iptal mi, devam mı?" · "Hamilton'ın ekibi 'ya kapasite yetmezse?' sorusunu uçuştan yıllar önce sordu ve cevabı koda yazdı. İyi bir karar yapısı kriz anında ne yapacağını bilen yapıdır." · "Bugün yazacağınız her `else` bloğu aynı sorunun küçük bir cevabı."

**boolean ve ==.** "Kasadaki kişi 'öğrenci misiniz?' diye sorar; evet ya da hayır, 'biraz' yok. `boolean` o cevaptır." · "Altı operatör, hepsi bir `boolean` üretir. Eşittir hep sağda, `=<` diye bir şey yok." · "'Hesap 50 mi?' sorudur, hesaba dokunmaz. 'Hesabı 50 yap' emirdir, fişi siler. Java'da aralarında tek karakter var." · "`if (puan = 85)` için Java bağırır, `if (ogrenci = true)` için susar. Boolean'ı `== true` ile karşılaştırmayın, 'evet mi, evet mi?' diye sormuş olursunuz."

**if ve if/else.** "Yağmur yağıyorsa şemsiye al, yağmıyorsa alma, iki durumda da kapıdan çık. Soru, evetse yapılan iş, ortak yol." · "Süslü parantez her zaman, tek satır olsa bile. Altı ay sonra ikinci satırı eklediğinizde o satır koşula bağlı olmaz ve siz fark etmezsiniz." · "if/else: ikisinden biri mutlaka, ikisi birden asla." · "`yas > 18` mi `yas >= 18` mi? 18 yaşındaki kişi hangi dala düşer? Sınır değerini her dalla birlikte test edeceksiniz."

**Merdiven.** "Beş cevap var, if/else iki yol veriyor. Beş ayrı if yazarsanız 85 puana üç harf birden." · "Merdiven yeni bir şey değil: else'in içine bir if/else daha. Yukarıdan aşağıya sorar, ilk evette durur, gerisini atlar." · "Her basamak üstündekilerin hayır dediği varsayımıyla yazılır. 95'in ikinci basamağa gelmemesinin tek sebebi ilk basamakta yakalanmış olması." · "Cevaplar birbirini dışlıyorsa merdiven, bağımsızsa ardışık if. Quiz'de else if yazarsanız tam puan alan öğrenciye 1/3 yazarsınız."

**İç içe ve sarkan else.** "Önce kapıdaki görevli, sonra odayı soran görevli. Kapıda kalana oda sorulmaz." · "Girinti yalnızca sizin için. Java boşlukları görmez, paranteze bakar." · "else en yakın if'e aittir, girinti bunu değiştirmez. 20 yaşındaki adama 'çocuk bileti' yazan kod bu." · "Çare hep aynı: içteki if'i paranteze al, belirsizlik hiç doğmaz."

**Tam dosyalar.** "Artık yıl üç kapı: 4 kapısı, 100 kapısı, 400 kapısı. 2000 üçünden de geçer, 1900 ikincide takılır." · "Üç kat iç içe okunmuyor, haklısınız. Gelecek hafta 've' ile 'ya da' bunu tek satıra indirecek; bugün elle kurmayı öğreniyoruz." · "En büyük bir anda bulunmaz, adım adım bulunur. İlkini ilan et, sonrakilere bak. Sıfırdan başlatırsanız üç negatif sayı için sıfır yazar." · "Taksi'de karar ekrana yazmıyor, ücreti değiştiriyor. Yazdırma tek satır, en sonda."

**Yaygın hatalar.** "Altı tuzak, altısı da derlenir, beşi çalışırken tek kelime etmez." · "if'ten sonraki noktalı virgül boş bir gövdedir; alttaki blok her zaman çalışır." · "0.1 + 0.2 tam 0.3 değil; double'ı eşitlikle değil aralıkla karşılaştırın." · "Üç hata, üç dakika, bulun, düzeltmeyin. Üçü de 'çalışıyor' görünür; 3.8 ortalamaya 'tam' beklediğinizi bildiğiniz için fark edersiniz."

**Kantin.** "Dört kat iç içe karar doğru çalışıyor; altı ay sonra beşinci katı nereye açacaksınız?" · "Gelecek hafta iki araç gelecek ve ikisi de yeni bir şey yapmayacak, yalnızca bugün elle kurduğunuz ağacı kısa yazacak."

**YZ anı.** "Yapay zekanın kodunu doğrulamanın yolu çalıştırmaktır, ama çalıştırmadan önce ne beklediğinizi bilmek zorundasınız." · "'else en yakın if'e aittir' kuralını bilmeden hangisinin yanıldığını bulamazsınız: siz mi, model mi?"

**Kapanış.** "Lab 3'ün son teslimi bu akşam 23.59." · "Lab 4'te altı program, altısı karar veriyor; her dalı ayrı girdiyle test edin, ritüelde 'üç dalı da nasıl test ettin?' sorulacak." · "Gelecek hafta KT1: uygulamanız en az bir if/else ile karar verecek. Konu dağıtımı duyuruyla gelecek."

## Olası aksaklıklar ve B planı

| Sorun | B planı |
|---|---|
| **Terminal / Codespaces açılmıyor** | Masaüstündeki ekran görüntülerini yansıya koy; üç programın çıktısını görüntüden oku. Playground'da `nextInt()` satırlarını `int yil = 1900;` gibi sabitlerle değiştirip çalıştır; "girdi sabit ama karar aynı" de. |
| **İnternet yok** | Diyagramlar sayfada gömülü SVG; sayfayı derse girmeden bir kez aç. Playground kodlarını tahtaya yaz, sınıf kağıtta tahmin eder; sarkan else'in çıktısını sen söyle ve tahtada parantezle düzelt. YZ anını atla. |
| Ters ağaç sorusunda sınıf "yine B" diyor | Beklenen; tahtada 85'i ters ağaçta **adım adım** yürüt, ilk elmasta durdur: "soru 'altmış ve üstü mü?', cevap evet, ağaç burada durur, geri kalan soruları hiç sormaz." Playground'da merdiveni ters çevirip D'yi göster. |
| Poll 1'de "program çöker" ya da "her zaman çalışır" çoğunlukta | İyi tartışma: "C dilinde her zaman çalışırdı, Java int için bağırır ama boolean için susar." `if (puan = 85)` ve `if (ogrenci = true)` ikisini de Playground'da göster. |
| Sarkan else kutusunda sınıf doğru tahmin ediyor ("Cocuk bileti") | Güzel; ek soru: "Şimdi `ogrenci = true` yapın, ne yazar? Peki `yas = 15` yapın?" (15 için hiçbir şey yazmaz, çünkü else iç if'e ait ve dış if false). Bu ikinci sürpriz daha öğretici. |
| Hata avında merdiven hatasını (14-20) kimse bulamıyor | "3.8 ortalamalı öğrenciye ne yazar?" diye sor; satırları parmağınla yürüt; bulmacadaki ters ağaca bağla. |
| Poll Everywhere çalışmıyor | El kaldırma: "`if (x = 5)` için çöker diyen, derlenmez diyen, çalışır diyen"; "0.1+0.2 == 0.3 için true diyen". |
| Süre taşıyor | Kesilecek sıra: YZ anı (siteye bırak) → Sahadan örnekler (siteye bırak) → Kantin sözde kodu yalnızca "gelecek hafta" cümlesi → CodeTry "VKİ" ve "Çift mi tek mi" evde → Yaygın hatalar altıdan üçe (`;`, `= true`, girinti yalanı). Bulmaca, Apollo (kısa), `==` sahnesi, merdiven ters çevirme, **sarkan else canlı** ve **üç tam dosya terminalde** kesilmez. |
| B şubesi öğle sonrası, enerji düşük | Bulmacayı yarışma yap: ters ağaçta 85'in harfini ilk doğru söyleyen sıra. Sinema gişesi için iki gönüllü: biri gişe, biri müşteri, üç müşteri senaryosu canlandırılır. Hata avını 4 dakika, yarışma havası. |

## B şubesi (13.15)

Aynı akış, aynı dakikalar (13.30 başla, 14.30-14.45 bitir). A şubesinden not: ters ağaç sorusunda "D" diyenlerin oranı, Poll 1'de "çöker" diyenlerin oranı, sarkan else tahmininde doğru oranı, hata avında en geç bulunan hata, terminalde takılan nokta. B'de o noktaya iki cümle fazla ayır. Poll sonuçlarının ekran görüntüsünü iki şube için ayrı al.

## Ders sonrası (5 dk)

- Hata avında en geç bulunan hata → Lab 4 için lab sorumlu hocasına not: öğrenciler orada takılacak (muhtemelen merdiven sırası; NotHarfi2 ve Bilet'te sıra hatası bekleniyor), labın başında bir kez daha anlatsın.
- Poll 3'te (sarkan else) yanlış diyenlerin yüzdesi → Lab 4 ritüelinde "parantezsiz blok" kontrolünü sıkı tutması için lab sorumlu hocasına söyle.
- Poll 4'te (`0.1+0.2 == 0.3`) true diyenlerin yüzdesi → 5. haftada kısa devre anlatırken bir kez daha hatırlat; vize öncesi (9. hafta) tekrar sor.
- Poll 5'ten 2-3 cümle → 5. haftanın açılışında oku.
- KT1 duyurusu (konu dağıtımı, teslim biçimi, "en az bir if/else" kuralı) hafta içinde yazılacak; derste öğrencilerden gelen "konu ne olacak?" sorularını not al ve duyuruda cevapla.
