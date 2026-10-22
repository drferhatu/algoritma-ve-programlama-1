# Hafta 5 · Ders senaryosu (öğretim üyesi notu, siteye girmez)

**Tarih:** 23 Ekim 2026 Cuma · A şubesi 09.15 (fiilen 09.30 başla, 10.40 bitir) · B şubesi 13.15 (fiilen 13.30 başla, 14.40 bitir).
**Tek oturum, 70 dakika fiilî.** Slayt yok; yansıda `/haftalar/hafta-05` açık. İkinci ekranda **Gemini masaüstü uygulaması** (görev modu, `Belgeler/algo1` yetkili) ve Java Playground sekmesi. Poll Everywhere soruları `docs/hafta-05-polleverywhere.md`.
**Slogan:** yazılımcı gibi sormak; artırma, otomasyon değil.
**Üslup notu:** Bu hafta ders canlı gösteri ağırlıklı; uzun anlatım yok, her bölümde sayfadaki istem kopyalanıp uygulamaya yapıştırılıyor, çıktı birlikte okunuyor, sonra **her çıktıdan sonra aynı adım**: "Playground'da çalıştır / ders notundan teyit et." Bu cümleyi dersin içinde en az sekiz kez söyle; bıkana kadar. Java konusu (switch, mantıksal operatörler) 10 dakikalık bir ada; normal ders üslubu, önce tahmin sonra Run.

## Hazırlık (derse girmeden)

- Gemini öğrenci planı kendi hesabında açık; masaüstü uygulaması kurulu ve **görev modunda `Belgeler/algo1` klasörü önceden yetkilendirilmiş**; klasörde yalnızca `Taksi.java`, `izleme.md` (bilerek bir satırı yanlış), `beceri-java-hata.md` var. `Menu.java` klasörde **olmasın**, derste oluşturulacak.
- "Java Hocam" Gem'i **önceden kurulmuş** ama derste bir kez daha canlı kurulacakmış gibi talimat metni gösterilecek (süre yetmezse hazırı kullan).
- Yansı: sayfa + Gemini uygulaması yan yana sığıyor mu, yazı büyüklüğünü dene. Uygulamada yazı tipi büyük.
- Yedek: her istemin dersten bir gün önce alınmış cevaplarının ekran görüntüsü (bulmacadaki iki cevap, sorgulama, sarkan else anlatımı, test girdisi tablosu, Menu iskeleti, tuzak sorunun cevabı). İnternet giderse bunlar yansıya.
- Playground'da "Durmayan asansör" ve "Kısa devre" kutuları sekmede hazır.
- Geçen haftadan: Poll 5 duvarından 2-3 cümle (açılışta oku); Poll 3'te "dıştaki if" diyenlerin yüzdesi (tekrar turunda sarkan else istemini açarken söyle).
- Lab 4 son teslim **bu gece 23.59**: açılışta ve kapanışta söyle. Lab 5 evde, 30 Ekim; KT1 6 Kasım.
- Kayıt sayısı: dersten önce sınıfa "kaç kişi öğrenci planına kaydoldu?" diye el kaldırt; düşükse ilk 3 dakikada kayıt bağlantısını yansıt ve "ders sonuna kadar kaydolun" de.

## Dakika dakika

| Dk | Blok | Hoca ne yapar | Öğrenci ne yapar | Tahtaya yazılacak |
|---|---|---|---|---|
| 0-5 | Bulmaca: iki istem | Geçen haftanın duvarından 2 cümle. "Lab 4 bu gece 23.59." Bulmacayı aç: Gemini'ye önce `switch nedir?` gönder, cevabı kaydırarak göster, okuma. Sonra dört parçalı istemi gönder; ikisini yan yana koy. Sor: "Hangisinden sonra ne yapacağınız belli?" El kaldırt. Cevap kutusu yok; "fark araçta değil, soruda." | İki cevabı karşılaştırır, el kaldırır | Sol üst: **FARK ARAÇTA DEĞİL, SORUDA** |
| 5-12 | Neden farklı + döngü | Ansiklopedi → arama motoru → asistan (1 dk). "Asistan sizin yerinize öğrenemez; salonda antrenör ağırlık kaldırıyor." MIT: **artırma, otomasyon değil** (tek cümle). Döngü diyagramını aç (h05-ogrenme-dongusu): sor → oku → dene → doğrula → anlat. "Turuncu kutu döngüyü döndüren kutu." Forward deployed engineer: bir paragraf, abartısız: "şirketin verisi kitapta yazmaz; doğru soran, doğrulayan kişi." Üç bölge hatırlatması: "bu ders yeşil ve sarıda NASIL çalışılacağını öğretiyor, kırmızı aynı." | Dinler; döngünün beş adımını not eder | `ARTIRMA, OTOMASYON DEĞİL` · `SOR → OKU → DENE → DOĞRULA → ANLAT` · `yeşil + sarı: NASIL?` |
| 12-18 | Kurulum ve üç mod | Uygulamayı yansıya al. Üç mod, üç benzetme: sohbet = mesaj; Gem = berber, "her zamanki gibi"; görev modu = usta atölyede. Görev modunu menüden seç, klasörü yetkilendir (canlı; yetkili zaten, "yeniden" göster). **Kilit cümle:** "Asistan sizin yetkinizle iş yapar." Uyarı kutusu: klasöre yalnızca ders dosyası, Belgeler'in tamamını değil. Not kutusu: arayüz adları değişir, ChatGPT/Claude'da aynı. | Kendi bilgisayarında klasör açar, yetkilendirir (kurabilenler) | `SOHBET · GEM · GÖREV` · `berber / usta` · `ASİSTAN SİZİN YETKİNİZLE İŞ YAPAR` · `klasör = yalnızca ders dosyası` |
| 18-26 | Dört parça yan yana | Tabloyu aç: rol, görev, biçim, bağlam; ofis benzetmesi. Diyagram h05-istem. Bulmacadaki ikinci istemi parçalara ayır, her parçayı tahtada işaretle. "En çok atlanan: bağlam; doktor-hasta." Poll 1 ("AI'yı en çok ne için kullanıyorsun") oyla, sonucu oku, "çoğunuz … için kullanıyor, bugün ona bir şablon veriyoruz." **İlk kez söyle:** "Güzel cevap doğru cevap değildir; Playground + ders notu." | Bulmacadaki istemi dört parçaya ayırır, kağıda yazar | `ROL · GÖREV · BİÇİM · BAĞLAM` · `en çok atlanan: BAĞLAM` · `GÜZEL ≠ DOĞRU → Playground + ders notu` |
| 26-32 | Java Hocam Gem | Gem talimatını sayfadan göster, satır satır değil, 7 kuralı başlıklarıyla oku (30 sn): çözme, önce sor, kendini sına, Playground'da dene, satır satır, Türkçe, fikrini değiştirme. Gem'i aç (hazır), üç soru sor: "merdivende sıra neden önemli?", "= ile ==?", "sarkan else?". Her cevabın "Kendini sına" sorusunu sınıfa sor. Cevapları **ders notundan teyit** (4. hafta sayfası ikinci sekmede). | "Kendini sına" sorularını cevaplar | `GEM = dört parçanın değişmeyen kısmı, bir kez` · `7 kural` · `kural 7: BENİ HAKLI ÇIKARMA` |
| 32-42 | Tekrar turu: dört istem | **Hafta 1-2:** nehir DOT istemi → Graphviz Online'a yapıştır → "kurt ile keçi yalnız mı?" diye sınıf baksın; yanlışsa sevin. **Hafta 3:** sorgulama istemi; öğrenci sensin, sınıf bağırır; 5. soruda Playground'a git. **Hafta 4:** sarkan else "anlat ama düzeltme" istemi; Poll 2'yi burada değil, 64. dakikada sor. Cevap "Cocuk bileti" mi? Playground'da çalıştır. **Hata protokolü:** kötü/iyi yan yana; "çalışmıyor bir duygu bildirimi." "İyi soru yazan hatayı yazarken bulur." Süre darsa nehir istemini atla, ekran görüntüsünü göster. | Nehir diyagramına bakar, sorgulamada bağırır, sarkan else çıktısını tahmin eder | `H1-2: DOT → resme bak` · `H3: SORGUYA ÇEK` · `H4: ANLAT, DÜZELTME` · `"çalışmıyor" ≠ hata raporu` · `MESAJ + 10 SATIR + NE DENEDİM` |
| 42-52 | switch + mantıksal op. (Playground) | Normal ders üslubu. "On ürünlük merdiven"den switch'e; dört kelime: switch, case, break, default. Diyagram h05-switch. **Canlı:** CodeTry "Gün adı" 3, 6, 9. Asansör hikayesi: "3'e bastın, asansör durmadı." **Canlı, önce tahmin:** "Durmayan asansör" kat = 3 → üç satır. Kural: her case'te break. Kırtasiye menüsü hızlı (ya da evde). Mantıksal operatörler tablosu; iki görevli benzetmesi. **Canlı:** "Artık yıl, tek satır" 1900 ve 2000; "geçen haftanın üç katı tek satır." Kısa devre: iki kapılı bina; **canlı:** "Kısa devre" kutusu, ikinci satırın yorumunu kaldır, ArithmeticException'ı okut. Her kutunun altındaki "Gemini'ye şunu sor" satırını göster: "evde bunları soracaksınız, cevabı Playground'la karşılaştıracaksınız." | Kağıda tahmin, Playground'da çalıştırır | `switch (x) { case 1: … break; default: }` · `BREAK = DUR DÜĞMESİ` · `&& ve · \|\| ya da · ! değil` · `b != 0 && a / b > 2` (tehlikeli soru SAĞA) |
| 52-60 | Görev modu canlı | Gemini'ye dön, klasör yetkili. **İstem 1:** Taksi.java'yı oku, üç test girdisi öner, çıktıları söyleme → tablo gelince sınıf çıktıları hesaplar, terminalde çalıştır, karşılaştır. **İstem 2:** izleme.md'yi kontrol et, yanlış satırı söyle, doğrusunu söyleme → bilerek yanlış satırı bulmalı; bulursa "ipucu ne?" diye oku, doğrusunu sınıf söyler. **İstem 3:** Menu.java iskeleti, gövdeler boş → dosya yazma iznini **yüksek sesle okuyup** onayla ("asistan benim yetkimle"); dosyayı aç, gövdeleri sınıfla birlikte doldur (1 Kitap ara, 2 Odunc al…). "İskelet asistandan, mantık sizden." Uyarı: "Taksi'yi düzelteyim mi derse HAYIR." | Test girdileri için çıktı hesaplar; iskelet gövdesini söyler | `İSKELET ASİSTANDAN · MANTIK SİZDEN` · `doğrusunu SÖYLEME` · `izin = okuyarak ver` |
| 60-64 | Beceri | `beceri-java-hata.md` dosyasını klasörden aç, 5 adımı oku (30 sn). Çağır: "beceri-java-hata.md'deki beceriyi uygula" + Menu.java'da bilerek yapılmış bir hata (ör. `ogrenci == "e"` ya da silinmiş break). İpucu gelince düzeltmeyi sınıf söyler. Diğer beceri fikirleri tek cümle: kod anlatıcı, test girdisi üretici, DOT çizici. Berber benzetmesi: "her zamanki gibi ama bugün sakal da." | İpucuyla hatayı bulur | `BECERİ = dosyada talimat, tek satırla çağır` · `kod anlatıcı · test üretici · DOT çizici` |
| 64-67 | Doğrulama anı | Poll 2 ("break olmadan switch durur mu?") oyla, sonucu gösterme. Tuzak istemi gönder: "break yazmazsam da çıkar, değil mi?" Cevabı oku: direndi mi, onayladı mı? Her iki durumda Playground: asansör kutusu kat = 3 → üç satır. "Soruya yanlış gömerseniz araç onu doğru sanabilir, Playground sanmaz." "'Değil mi?' değil, 'ne olur?' diye sorun." Poll 3 ve 4 hızlı (en iyi istem; nasıl doğrularsın). | Oylar; tahmin, çalıştır | `"DEĞİL Mİ?" → "NE OLUR?"` · `Playground sanmaz` |
| 67-70 | Cep kartı + kapanış | Cep kartını kaydır, altı istemi say: dört parçalı soru, Java Hocam, sorguya çek, hata protokolü, kodu anlat, test üret. "Telefonunuza ya da algo1 klasörüne." Kapanış: Lab 4 **bu gece 23.59**; Lab 5 **evde, yeşil bölge, günlük zorunlu, 30 Ekim Cuma 23.59**; lab tatil (28 arife, 29 bayram); KT1 **6 Kasım**, menü iskeletini yaptırabilirsiniz ama her satırını anlatacaksınız. Poll 5 (tek cümle). Haftaya döngüler. | Cep kartını kaydeder; anket | `Lab 4: BU GECE 23.59` · `Lab 5: EVDE · YEŞİL · 30 Ekim` · `KT1: 6 Kasım` · `Haftaya: döngü` |

## Kilit cümleler (blok blok)

**Bulmaca.** "Aynı araç, aynı dakika, iki cevap. Fark araçta değil, soruda." · "Birinci cevabı okudunuz, ikincisinden bir şey öğrendiniz."

**Neden farklı.** "Ansiklopedi, arama motoru, asistan: üçüncüsü size nasip oldu, ama asistan sizin yerinize öğrenemez." · "Salonda antrenör ağırlık kaldırırsa antrenör güçlenir." · "Artırma, otomasyon değil: öğrenmeyi otomatikleştirmek değil, güçlendirmek." · "Bu döngüyü bugün Playground'da kuran, yarın bir şirketin verisiyle kurar; o rolün adı beş yıl önce yoktu."

**Üç mod.** "Gem, berbere 'her zamanki gibi' demek." · "Görev modu, ustayı atölyeye çağırmak; kapıyı siz açıyorsunuz." · "Asistan sizin yetkinizle iş yapar. Yetkiyi veren siz, sorumluluk sizde." · "Klasöre yalnızca ders dosyası."

**Dört parça.** "Rol, görev, biçim, bağlam: kime soruyorum, ne istiyorum, nasıl istiyorum, ben kimim." · "En çok atlanan bağlam; 'başım ağrıyor' deyip gerisini söylemeyen hasta." · "Güzel bir cevap doğru bir cevap değildir. Playground'da çalıştır, ders notundan teyit et."

**Gem.** "Dört parçanın değişmeyen kısmını bir kez kaydet." · "Yedinci kural: beni haklı çıkarmak için fikrini değiştirme. Her zaman tutmaz; tutmadığında görürsünüz, görmek de derstir."

**Tekrar turu.** "DOT kodunu okumayın, resme bakın: kurt ile keçi yalnız mı?" · "Sorguya çekilmek, bildiğinizi savunabildiğinizi göstermek." · "Anlat ama düzeltme: doğruyu asistan söylerse okumuş olursunuz, kendiniz bulursanız öğrenmiş olursunuz." · "'Çalışmıyor' bir hata raporu değil, bir duygu bildirimi." · "İyi bir soru yazmak cevabın yarısıdır; yazan çoğu zaman cevabı kendisi görür."

**switch ve mantıksal operatörler.** "switch eşitlik sorar, aralık sormaz; aralık için merdiven hâlâ doğru araç." · "break dur düğmesi; basmazsanız asansör son kata kadar her katta kapıyı açar." · "Her case'in sonunda break; bilerek düşürdüğünüz yere yorum." · "İki görevli de 'geç' demeli: &&. Birinin demesi yeter: ||." · "İlk kapıdan geçemeyen ikinci kapıya gitmez; tehlikeli soruyu sağa yazın."

**Görev modu.** "Üç girdi öner ama çıktıları söyleme; çıktıları biz hesaplıyoruz." · "Yanlış satırı söyle, doğrusunu söyleme." · "İskelet asistandan, mantık sizden; bu cümleyi dönem boyunca duyacaksınız." · "İzin isteyince okuyun, sonra onaylayın. Taksi'yi düzelteyim mi derse hayır."

**Beceri.** "Aynı olan şey dosyaya girer." · "Gem 'her zamanki gibi', beceri 'bugün bir de sakal'."

**Doğrulama anı.** "Soruya yanlış bilgi gömerseniz araç onu doğru sanabilir, Playground sanmaz." · "'Değil mi?' diye sormayın, 'ne olur?' diye sorun ve çalıştırın."

**Kapanış.** "Lab 4 bu gece 23.59." · "Lab 5 evde ve yeşil bölge: yapay zeka serbest, günlük zorunlu; 30 Ekim Cuma 23.59." · "KT1 6 Kasım; menü iskeletini yaptırabilirsiniz, her satırını anlatacaksınız."

## Olası aksaklıklar ve B planı

| Sorun | B planı |
|---|---|
| **İnternet yok / Gemini açılmıyor** | Bütün istemler sayfada ve sayfa önceden açık; her istem için bir gün önce alınmış cevap ekran görüntüleri yansıya. Playground yerine tahta: asansör kodunu tahtaya yaz, sınıf tahmin eder, çıktıyı sen söyle. Görev modu bölümünde Menu iskeletini tahtaya elle yaz, gövdeleri sınıf doldurur. Dersin omurgası (dört parça, doğrulama, hata protokolü) internetsiz de anlatılır. |
| **Görev modu klasörü görmüyor / izin akışı farklı** | "Arayüz adları değişir" notunu göster, menüde birlikte ara (1 dk). Bulunamazsa sohbet moduna düş: Taksi.java'yı kopyala-yapıştır ile ver, aynı üç istemi uygula; "görev modu olmadan da aynı akış, yalnızca yapıştırma işi sizde." Menu iskeletini sohbetten kopyalayıp dosyaya kendin yapıştır. |
| **Öğrenci planı kaydı açılmıyor (kampanya koşulu, e-posta doğrulama)** | "Ücretsiz sohbet modu labın tamamı için yeter" de; Lab 5 sayfasında da yazıyor. Kampanya koşulları değişmiş olabilir; course.json'daki "koşullar değişebilir" notunu hatırlat. |
| Bulmacada sınıf "ikisi de aynı" diyor | İkinci cevabın sonundaki "kendini sına" sorusunu oku ve sor: "Birincide bu var mı? Birinci cevap size ne yapmanızı söylüyor?" |
| Asistan tuzak soruda doğru cevap veriyor (direniyor) | Güzel; "bugün iyi gününde" de ve yine Playground'da çalıştır: "aracın sözü değil, çıktı." Ardından ikinci tuzak: "switch'te default en üste yazılırsa önce o çalışır, değil mi?" (Hayır; default sırası fark etmez, eşleşme yoksa çalışır; ama break yoksa düşme sırası değişir.) Playground'da dene. |
| Asistan Menu.java gövdelerini kendisi dolduruyor | Beklenen bir ihlal; sevin. "İstemde 'boş bırak' dedik, dinlemedi; işte bu yüzden okuyup onaylıyoruz." Gövdeleri sil ya da sınıfla yeniden yaz; AI-BEYANI'nın dördüncü satırına örnek olarak göster. |
| Nehir DOT diyagramı bozuk (kurt-keçi yalnız) | En iyi senaryo; "DOT bilmeden yakaladınız, çünkü resme baktınız." Düzeltmesini istemeyin, "siz düzeltin" deyin, geçilir. |
| Sorgulama simülasyonunda asistan yanlış değerlendirme yapıyor | Playground'a git, tartışmalı soruyu çalıştır; "asistanın 'doğru' dediği şey yanlış çıkabilir, bu yüzden doğrulama." |
| Poll Everywhere çalışmıyor | El kaldırma: "break olmadan durur diyen / durmaz diyen"; "en iyi istem A/B/C". |
| **Süre taşıyor** | Kesilecek sıra: nehir DOT istemi (ekran görüntüsü) → kırtasiye menüsü CodeTry (evde) → "Dört ihtimal" CodeTry (evde) → beceri bölümü yalnızca dosyayı gösterip "Lab 5 başlık 4" demek → sorgulama 5 soru yerine 3. **Kesilmeyecekler:** bulmaca, dört parça, Gem'in üç sorusu, asansör canlı, görev modu üç istem, doğrulama anı, cep kartı + Lab 5 duyurusu. |
| B şubesi öğle sonrası, enerji düşük | Sorgulama simülasyonunu yarışma yap: sıra sıra cevap, ilk doğru sıra puan. Görev modunda izleme.md'nin yanlış satırını "asistandan önce bulan" kazanır. Tuzak soruyu sınıfa yazdır: "kendi tuzak sorunuzu yazın, en iyisini deneyelim." |

## B şubesi (13.15)

Aynı akış (13.30 başla, 14.40 bitir). A şubesinden not: bulmacada "ikisi aynı" diyenlerin oranı; Poll 1'de en sık kullanım; tuzak soruda asistanın cevabı (direndi mi); görev modunda izin akışında takılan nokta; asistan Menu gövdesini doldurdu mu. B'de o noktalara iki cümle fazla ayır. Poll sonuçlarının ekran görüntüsünü iki şube için ayrı al.

## Ders sonrası (5 dk)

- Poll 1 sonuçlarını (AI'yı ne için kullanıyorlar) not et; Lab 5 günlüklerini okurken lab sorumlu hocasına "sınıfın yüzde X'i kod yazdırmak için kullanıyor, günlüklerde 'kodumu anlattım' başlığına dikkat" diye ilet.
- Poll 2'de (break olmadan durur mu) "durur" diyenlerin yüzdesi → Lab 5 otomatik kontrolünde break hatası beklenir; 6. haftanın açılışında asansörü bir cümleyle hatırlat.
- Görev modunda izin akışında ne değişmişse Lab 5 sayfasındaki genel ifadeleri gerekirse güncelle (yalnızca gerçekten yanıltıcıysa).
- Poll 5'ten 2-3 cümle → 6. haftanın açılışında oku.
- Lab 5 evde olduğu için Pazartesi bir hatırlatma duyurusu: "günlüğün beş başlığı birebir, Cuma 23.59."
- 6. hafta: döngüler; bu haftanın Menu iskeleti "0 girilene kadar" döngüye alınacak, açılışta o dosyayla başla.
