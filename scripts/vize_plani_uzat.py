"""Vize planını 24 Kasım 2026 Salı sınav tarihine göre günceller ve 16-23 Kasım için 8 gün ekler.
Tek seferlik; tekrar çalıştırılırsa (gün sayısı zaten 25 ise) yalnızca metin düzeltmelerini uygular."""
import json, pathlib

P = pathlib.Path(__file__).resolve().parent.parent / "content/data/vize-plani.json"
d = json.loads(P.read_text(encoding="utf-8"))

VIZE = "24 Kasım'da kağıt üzerinde vizem var"

# 1) sinav nesnesi
s = d["sinav"]
s["hafta"] = 10
s["aralik"] = "24 Kasım 2026 Salı"
s["tarih"] = "2026-11-24"
s["saat"] = "17.00-18.00"
s["salonlar"] = [
    {"sube": "A şubesi", "salon": "A304, A305, A306"},
    {"sube": "B şubesi", "salon": "A306, A404, A405, A406"},
]
s["not"] = "sınavlar derslerle birlikte yapılıyor; 20 Kasım Cuma dersi ile 18-19 ve 25-26 Kasım labları her zamanki saatinde"
s["kapsamNotu"] = ("Sınav kapsamı 1-8. hafta içerikleridir (döngüler II dahil); döngüler 7. ve 8. haftada işlendi. "
                   "20 Kasım'da işlenecek 9. haftanın konusu olan metotlar kapsam dışıdır.")

d["_aciklama"] = ("Vize çalışma planı (/vize-plani sayfası bu dosyayı okur). Sınav 24 Kasım 2026 Salı 17.00-18.00. "
                  "30 Ekim - 23 Kasım arası 25 gün; hafta içi tek blok (25 dk), hafta sonu iki blok. İlk tur 1-17. günler "
                  "(30 Ekim - 15 Kasım), ikinci tur 18-25. günler (16-23 Kasım). Her blokta konu, yapılacaklar, kopyalanabilir "
                  "bot istemi (dört parçalı: rol, görev, biçim, bağlam; her birinde doğrulama adımı), varsa ajan istemi ve 3 soruluk "
                  "kendini sınama. 'kodlar' alanı isteğe bağlı: kağıtta izlenecek ya da hatası avlanacak kodlar. Tarih formatı "
                  "YYYY-AA-GG. Hoca sınava benzer soru yayımlamaz; deneme sınavını öğrenci kendi üretir (16. ve 23. gün).")

# 2) Tüm metinlerde eski ifadeler
def fix(x):
    if isinstance(x, str):
        for a, b in [
            ("9. haftada kağıt üzerinde vizem var", VIZE),
            ("gelecek hafta kağıt üzerinde vizem var", VIZE),
            ("bu hafta kağıt üzerinde vizem var", VIZE),
        ]:
            x = x.replace(a, b)
        return x
    if isinstance(x, list):
        return [fix(i) for i in x]
    if isinstance(x, dict):
        return {k: fix(v) for k, v in x.items()}
    return x

d = fix(d)
g = {x["gun"]: x for x in d["gunler"]}

# 3) 13-15 Kasım günlerindeki eskiyen ifadeler
g[15]["ozet"] = ("Cuma: 8. hafta dersi (Döngüler II: iç içe döngü, break/continue, EBOB), vize kapsamının son konusu; "
                 "20 Kasım'ın metotları kapsam dışı. Bir haftadır ön bakışta takıldığınız yerleri derste sorun; akşam kısa bir "
                 "flash kart turu ve iç içe döngü için tek bir izleme. Sınav 24 Kasım Salı 17.00'de; yarın ilk deneme kağıdınızı "
                 "yazıyorsunuz, ikincisi 21 Kasım'da.")
g[15]["tekrar"] = ["Üçüncü tur (flash kart): Hafta 1-8'nin tamamı.", "Yarın: ilk deneme kağıdınız (ikincisi 23. günde)."]
g[15]["bloklar"][0]["yap"][1] = "Takıldığınız kartları 17. günün zayıf konu listesine ekleyin."
g[16]["baslik"] = "Kendi deneme sınavını kendin yaz (ilk kağıt)"
g[16]["tekrar"] = ["Üçüncü tur: Hafta 1-8'nin tamamı (kendi deneme kağıdınızla).",
                   "Yanlış listesi yarının (17. gün) programını belirler; ikinci kağıt 23. günde."]
g[17]["baslik"] = "İlk turun sonu: zayıf konular ve ikinci portfolyo provası"
g[17]["ozet"] = ("Pazar, ilk turun son günü. Yeni konu yok; dünkü yanlış listesine göre hedefli tekrar, sonra portfolyo sorusunun "
                 "ikinci provası ve cep kartıyla kapanış. Sınava dokuz gün var: yarından itibaren ikinci tur başlıyor ve bu kez "
                 "ağırlık 8. haftanın döngülerinde. Akşam erken bitirin; ikinci tura dinlenmiş girin.")
g[17]["bloklar"][1]["konu"] = "Portfolyo provası (ikinci) ve ilk turun kapanışı"
g[17]["bloklar"][1]["yap"][2] = ("Sınav günü kutusunu okuyun; kağıt, kalem ve izleme tablosu alışkanlığı. Bu akşam yeni bir şey "
                                 "çalışmayın; yarın ikinci tur iç içe döngülerle başlıyor.")
g[17]["bloklar"][1]["sina"][2] = "İlk turun on yedi gününde hangi konu 'bilmiyordum, artık biliyorum' oldu?"
g[17]["tekrar"] = ["Hedefli tekrar: yalnızca dünkü yanlış listesi. Portfolyo provası 2/3.",
                   "Yarın ikinci tur: 16-23 Kasım, sekiz gün; sınav 24 Kasım Salı 17.00."]

# 4) Yeni günler (18-25)
BAGLAM = "Bağlam: 1. sınıf öğrencisiyim, metot ve dizi görmedim, " + VIZE
YENI = [
 {"gun": 18, "tarih": "2026-11-16", "baslik": "İkinci tur başlıyor: iç içe döngüde iz tablosu", "yogunluk": "orta",
  "ozet": "Pazartesi, tek blok. İkinci turun ilk günü ve konusu sınavın en çok puan getiren becerisi: iç içe döngüyü kağıtta izlemek. Cuma günkü dersin ilk kapsüllerini kapalı kitapla hatırlayıp her (i, j) çifti için bir satır açtığınız bir iz tablosu tutuyorsunuz; iç döngünün sınırı dış sayaca bağlı olduğunda tablonun nasıl daraldığını kendi elinizle görmek bugünün bütün işi.",
  "bloklar": [{"sure": 25, "konu": "İç içe döngü: (i, j) çiftleri ve iz tablosu",
    "yap": ["8. haftanın sayfasını açmadan, dış döngü 1'den 3'e ve iç döngü 1'den 4'e dönen bir çarpım tablosunu kağıda yazın ve kaç satır, kaç sayı çıkacağını söyleyin; sonra sayfayı açıp karşılaştırın.",
            "Aşağıdaki kodu kağıtta izleyin: i, j ve ekrana yazılan değer için üç sütun açın, her tur için bir satır yazın; iç döngü bittiğinde alt satıra geçildiğini tabloda işaretleyin. Cevabı ancak tablonuz bittikten sonra açın ve Playground'da çalıştırarak doğrulayın.",
            "Aynı kodda iç döngünün başlangıcını j = i yerine j = 1 yapın ve tabloyu yeniden tutun: kaç satır eklendi? İç döngünün sınırını dış sayaca bağlamanın etkisini bir cümleyle yazın."],
    "istem": "Birinci sınıfa Java öğreten sabırlı bir hoca gibi davran. Görev: bana iç içe iki for döngüsü içeren, 8 satırı geçmeyen, Scanner'sız üç küçük kod ver; birinde iç döngünün sınırı sabit, birinde dış sayaca bağlı (j <= i), birinde iç döngü geriye saysın. Her kod için ekrana ne yazılacağını SÖYLEME; ben her (i, j) çifti için bir satır olan iz tablomu yazınca tablomu satır satır kontrol et ve yalnızca ilk yanlış satırımı göster. Biçim: her seferinde tek kod, cevabımı bekle. " + BAGLAM + "; her kodu Playground'da çalıştırıp senin kontrolünle karşılaştıracağım, uymayan yerde kazanan Playground.",
    "ajan": None,
    "sina": ["Dış döngü 3, iç döngü 4 tur dönüyorsa gövde toplam kaç kez çalışır?",
             "İç döngü bittiğinde iç sayaç ne olur; dış döngünün bir sonraki turunda nereden başlar?",
             "System.out.println() satırı iç döngünün içinde mi dışında mı olmalı ki her satır ayrı yazılsın?"],
    "kodlar": [{"baslik": "İzleme: sınırı dışa bağlı iç döngü",
      "kod": "for (int i = 1; i <= 3; i++) {\n    for (int j = i; j <= 3; j++) {\n        System.out.print(i * j + \" \");\n    }\n    System.out.println();\n}",
      "cevap": "Üç satır: \"1 2 3\", \"4 6\", \"9\". Açıklama: i = 1 iken j 1, 2, 3 (çarpımlar 1, 2, 3); i = 2 iken j 2'den başlar (4, 6); i = 3 iken yalnızca j = 3 (9). İç döngü her dış turda i'den başladığı için satırlar kısalır; gövde toplam 3 + 2 + 1 = 6 kez çalışır."}]}],
  "tekrar": ["Dördüncü tur: Hafta 8 (iç içe döngü), dersten üç gün sonra.", "Yarın: break, continue, asal ve EBOB."]},

 {"gun": 19, "tarih": "2026-11-17", "baslik": "break, continue, asal sayı ve elle Euclid", "yogunluk": "orta",
  "ozet": "Salı, tek blok. Sınava tam bir hafta var. Döngüyü erken bitiren break ile turu atlayan continue'yu aynı kodda izliyor, sonra bir sayının asal olup olmadığını ve iki sayının EBOB'unu kağıtta, bölme kalanıyla buluyorsunuz. Bugünün ölçüsü basit: Euclid'i üç sayı çifti için adım adım yazabiliyorsanız kod zaten elinizde demektir.",
  "bloklar": [{"sure": 25, "konu": "break ve continue izleme; asal testi ve Euclid'i elle çalıştırma",
    "yap": ["Aşağıdaki ilk kodu kağıtta izleyin: her tur için i'yi, hangi if'in doğru olduğunu ve toplamın yeni değerini yazın; continue'nun atladığı ve break'in bitirdiği turu işaretleyin.",
            "91 asal mı? 2'den başlayıp bölen arayın ve ilk böleni bulduğunuz an durun; kaç deneme yaptınız, break olmasaydı kaç deneme yapılırdı?",
            "Euclid'i elle üç çift için çalıştırın: (84, 36), (252, 105), (1920, 1080). Her adımda a, b ve kalan sütunlarını yazın; ikinci koddaki adım sayacının ne yazacağını tahmin edin, sonra Playground'da doğrulayın."],
    "istem": "Java hocası gibi davran. Görev: beni break, continue ve Euclid EBOB algoritması konusunda sorguya çek. Her seferinde tek soru sor ve cevabımı bekle; soruların yarısı 'bu kod ne yazar?' biçiminde (Scanner'sız, 10 satırı geçmeyen, içinde break ya da continue olan bir döngü), diğer yarısı 'şu iki sayının EBOB'unu Euclid ile adım adım bul' biçiminde olsun. Doğruysam bir zorlaştır, yanlışsam önce ipucu ver, ikinci yanlışta açıkla. Biçim: 6 soru, sonunda en zayıf noktam tek cümle. " + BAGLAM + "; her kodu Playground'da çalıştırıp senin cevabınla karşılaştıracağım, uymazsa kazanan Playground.",
    "ajan": None,
    "sina": ["continue döngüyü bitirir mi; break'ten farkı tek cümleyle nedir?",
             "İç içe iki döngüde iç döngüdeki break hangi döngüyü bitirir?",
             "Euclid'de döngü ne zaman durur ve cevap o anda hangi değişkendedir?"],
    "kodlar": [{"baslik": "İzleme: continue ve break aynı döngüde",
      "kod": "int toplam = 0;\nfor (int i = 1; i <= 10; i++) {\n    if (i % 3 == 0) {\n        continue;\n    }\n    if (i > 7) {\n        break;\n    }\n    toplam = toplam + i;\n}\nSystem.out.println(\"Toplam: \" + toplam);",
      "cevap": "Toplam: 19. Açıklama: 3 ve 6 continue ile atlanır; 1 + 2 + 4 + 5 + 7 = 19. i = 8 olduğunda ilk if yanlış, ikinci if doğru ve break döngüyü bitirir; 9 ve 10 hiç denenmez."},
     {"baslik": "İzleme: Euclid ve adım sayacı",
      "kod": "int a = 84;\nint b = 36;\nint adim = 0;\nwhile (b != 0) {\n    int kalan = a % b;\n    a = b;\n    b = kalan;\n    adim++;\n}\nSystem.out.println(\"EBOB: \" + a + \", adim: \" + adim);",
      "cevap": "EBOB: 12, adim: 2. Açıklama: 84 % 36 = 12, yeni çift (36, 12); 36 % 12 = 0, yeni çift (12, 0). b sıfır olunca döngü biter ve cevap a'dadır. (252, 105) için 21 ve 3 adım; (1920, 1080) için 120 ve 4 adım."}]}],
  "tekrar": ["Dördüncü tur: Hafta 8 (break/continue, EBOB). Hafta 7'nin gözcü değeri de Euclid'in koşulunda: b sıfır olana kadar.", "Yarın ve Perşembe: Lab 8, yani sınav provası."]},

 {"gun": 20, "tarih": "2026-11-18", "baslik": "Lab 8 günü (A şubesi): lab sınav provasıdır", "yogunluk": "orta",
  "ozet": "Çarşamba, tek blok. A şubesi bugün, B şubesi yarın Lab 8'de. Lab görevleri iç içe döngü, asal, EBOB ve FizzBuzz; yani sınav kapsamının son konusunun tamamı. Labda yazdığınız her döngüyü push etmeden önce bir kez kağıtta izlemek en verimli sınav çalışmasıdır. Akşam bloğunda bir kalıp daha var: bir sayıyı basamaklarına ayıran döngü.",
  "bloklar": [{"sure": 25, "konu": "Lab 8 döngülerini kağıtta izle; basamak döngüsü (palindrom sayı)",
    "yap": ["Lab 8'de yazdığınız (ya da yarın yazacağınız) programlardan ikisini seçin ve örnek girdiyle kağıtta izleyin; çıktınız Releases sayfasındaki testle aynı mı? B şubesindeyseniz bugün görevleri okuyup ilk ikisinin döngüsünü kağıda taslak olarak yazın.",
            "Aşağıdaki kodu kağıtta izleyin: kopya, kopya % 10 ve ters için üç sütun açın; döngü kaç tur döner ve bittiğinde kopya kaçtır?",
            "Aynı kalıpla 4096 sayısının basamak sayısını ve basamakları toplamını bulan döngüyü kağıda yazın (cevap: 4 basamak, toplam 19), sonra Playground'da çalıştırın."],
    "istem": "Java hocası gibi davran. Görev: bana 'bir tam sayıyı % 10 ve / 10 ile basamaklarına ayıran while döngüsü' kalıbını kullanan üç küçük alıştırma ver (basamak sayısı, basamaklar toplamı, sayının tersi); çözümleri YAZMA. Ben her birini kağıtta yazıp sana gönderince kodumu satır satır oku, hata varsa yalnızca hangi satırda olduğunu söyle ve o satır için bir soru sor; düzeltmeyi ben yapacağım. Biçim: her seferinde tek alıştırma. " + BAGLAM + "; her çözümü Playground'da en az iki sayıyla (biri tek basamaklı) çalıştırıp doğrulayacağım.",
    "ajan": "Bu klasör benim Lab 8 depom. İçindeki .java dosyalarını derle ve her birini lab sayfasındaki örnek girdiyle çalıştır; her dosya için programın yazdığı çıktıyı ve hangi komutu çalıştırdığını bir tabloya yaz. Hiçbir dosyayı DEĞİŞTİRME, düzeltme ya da iyileştirme önerme; derlenmeyen dosya varsa yalnızca derleyicinin ilk hata satırını aynen aktar.",
    "sina": ["sayi % 10 ne verir, sayi / 10 ne verir? 1221 için ikisini söyleyin.",
             "Basamak döngüsü neden sayının kendisinde değil bir kopyasında çalışır?",
             "Labda yazdığınız iç içe döngülerden birinde gövde toplam kaç kez çalışıyor?"],
    "kodlar": [{"baslik": "İzleme: sayıyı ters çevir, palindrom mu?",
      "kod": "int sayi = 1221;\nint kopya = sayi;\nint ters = 0;\nwhile (kopya > 0) {\n    ters = ters * 10 + kopya % 10;\n    kopya = kopya / 10;\n}\nSystem.out.println(ters);\nSystem.out.println(sayi == ters);",
      "cevap": "1221 ve true. Açıklama: turlar sırasıyla ters = 1, 12, 122, 1221; kopya = 122, 12, 1, 0. Dört tur döner ve kopya 0 olunca biter. sayi değişmediği için karşılaştırma yapılabilir; döngü sayi üzerinde çalışsaydı sayi 0 olurdu ve karşılaştırma hep false çıkardı (1221 yerine 0 == 1221)."}]}],
  "tekrar": ["Dördüncü tur: Hafta 7-8 (lab görevleriyle).", "Yarın: 1-5. haftanın karışık izlemesi."]},

 {"gun": 21, "tarih": "2026-11-19", "baslik": "Lab 8 günü (B şubesi) ve eski konuların karışık izlemesi", "yogunluk": "orta",
  "ozet": "Perşembe, tek blok. B şubesi bugün Lab 8'de. Üç gündür döngü çalışıyorsunuz; bugün bilerek geriye dönüyoruz, çünkü sınav kağıdında tipler, seçim ve switch döngülerle aynı sayfada duracak ve en çok puan, en eski konuda dikkatsizlikten gider. Tek bir kod, içinde beş haftanın beş tuzağı.",
  "bloklar": [{"sure": 25, "konu": "Karışık izleme, üçüncü tur: tam sayı bölmesi, kısa devre, switch'te break, + ile birleştirme",
    "yap": ["Aşağıdaki kodu kağıtta izleyin ve dört çıktı satırını yazın; her satırın yanına hangi haftanın tuzağı olduğunu not edin. Cevabı ancak dört satırı yazdıktan sonra açın.",
            "Yanlış yaptığınız her satır için o haftanın 'Temel Kavramlar' maddesini açın, tek cümleyi sesli okuyun ve kodu Playground'da bir değer değiştirerek yeniden çalıştırın (örneğin x = 9).",
            "B şubesi: lab görevlerini yazdıktan sonra dünkü kartın ilk maddesini yapın, yani iki döngünüzü kağıtta izleyin."],
    "istem": "Sınav yazarı ve Java hocası gibi davran. Görev: 1-5. hafta konularını (tam sayı bölmesi ve %, tür dönüşümü, if/else ve sarkan else, mantıksal operatörler ve kısa devre, switch ve unutulan break, String ile + birleştirme) tek programda karıştıran, 12-15 satırlık, Scanner'sız iki kod yaz; her biri 4 satır çıktı üretsin. Çıktıları SÖYLEME. Ben cevaplarımı yazınca her satırı kontrol et, yanlışsam hangi kuralı atladığımı bir soruyla sor. Biçim: önce birinci kod, cevabımdan sonra ikinci kod. " + BAGLAM + "; iki kodu da Playground'da çalıştırıp senin anahtarınla karşılaştıracağım, uymazsa kazanan Playground.",
    "ajan": None,
    "sina": ["int x = 7; double y = x / 2; satırından sonra y kaçtır ve neden 3.5 değildir?",
             "break'i olmayan bir case çalıştıktan sonra ne olur?",
             "x + 1 + \"!\" + x + 1 ifadesinde ilk + ile son + neden farklı iş yapar?"],
    "kodlar": [{"baslik": "İzleme: beş haftanın beş tuzağı",
      "kod": "int x = 7;\ndouble y = x / 2;\nint z = x % 4;\nif (y > 3 || z == 3 && x < 5) {\n    System.out.println(\"A \" + y);\n} else {\n    System.out.println(\"B \" + y);\n}\nswitch (z) {\n    case 1:\n        System.out.println(\"bir\");\n    case 3:\n        System.out.println(\"uc\");\n    case 4:\n        System.out.println(\"dort\");\n        break;\n    default:\n        System.out.println(\"hicbiri\");\n}\nSystem.out.println(x + 1 + \"!\" + x + 1);",
      "cevap": "Dört satır: \"B 3.0\", \"uc\", \"dort\", \"8!71\". Açıklama: 7 / 2 tam sayı bölmesiyle 3, double kutusunda 3.0; 3.0 > 3 yanlış, z == 3 doğru ama x < 5 yanlış olduğu için && yanlış, tüm koşul yanlış ve else çalışır. z = 3 olduğundan case 3'ten girilir, break olmadığı için case 4'e düşülür ve orada break ile çıkılır. Son satırda önce 7 + 1 = 8 hesaplanır, sonra String'e dönüşür: \"8!\" + 7 = \"8!7\", ardından + 1 ile \"8!71\"."}]}],
  "tekrar": ["Dördüncü tur: Hafta 3, 4 ve 5 (karışık).", "Yarın Cuma: 9. hafta dersi (metotlar, kapsam dışı) ve akşam cep kartı."]},

 {"gun": 22, "tarih": "2026-11-20", "baslik": "9. hafta dersi (metotlar, kapsam dışı), akşam cep kartı", "yogunluk": "hafif",
  "ozet": "Cuma: 9. hafta dersi her zamanki saatinde ve konusu metotlar. Metotlar sınav kapsamında değil, ama derse gelmek sınava da yarar, çünkü metot dediğimiz şey sekiz haftadır yazdığınız döngü ve seçimlerin bir ad altında toplanmasıdır ve örneklerin hepsi kapsamdaki konulardan kurulur. Akşam kısa bir flash kart turu; yarın ikinci deneme kağıdınız.",
  "bloklar": [{"sure": 15, "konu": "Cep kartı: 1-8. hafta flash kart turu (kısa blok)",
    "yap": ["Sayfanın sonundaki cep kartından flash kart istemini çalıştırın ve 10 kartı sesli cevaplayın; bu kez en az dört kart 7-8. haftadan gelsin.",
            "Takıldığınız kartları Pazar gününün (24. gün) zayıf konu listesine ekleyin; ilk kağıdınızdaki (16. gün) yanlış listesini de yanına koyun.",
            "Yarın için kağıt, kalem ve 60 dakikalık sessiz bir yer ayarlayın; ikinci deneme kağıdını da telefonsuz çözeceksiniz."],
    "istem": "Birinci sınıfa Java öğreten bir hoca gibi davran. Görev: Algoritma ve Programlama I dersinin 1-8. haftasından (algoritma ve akış diyagramı, program yapısı ve hata türleri, tipler ve operatörler, if/else ve sarkan else, switch ve mantıksal operatörler, while/do-while/for ve gözcü, iç içe döngü, break/continue ve EBOB) hatırlama gerektiren 10 flash kart hazırla; en az dört kart döngülerden ve en az üç kart küçük bir kod parçasından oluşsun, metot ve dizi içermesin. Biçim: ön yüzde tek soru, cevapları başta verme; ben 'arkasını çevir' dediğimde yalnızca o kartın cevabını yaz. " + BAGLAM + ", yarın ikinci deneme kağıdımı çözeceğim. Her cevabı ders notuyla karşılaştıracağım; uymayan yerde ders notu kazanır.",
    "ajan": None,
    "sina": ["Bugünkü dersin konusu sınav kapsamında mı; kapsamın son konusu hangisi?",
             "İlk deneme kağıdınızda en çok hangi soru türünde puan kaybettiniz?",
             "Sınav hangi gün, saat kaçta ve sizin şubeniz hangi salonlarda?"]}],
  "tekrar": ["Beşinci tur (flash kart): Hafta 1-8'nin tamamı.", "Yarın: ikinci deneme kağıdınız."]},

 {"gun": 23, "tarih": "2026-11-21", "baslik": "İkinci deneme kağıdı: yeni sorular, ağırlık döngülerde", "yogunluk": "yogun",
  "ozet": "Cumartesi, iki blok. Bir hafta önce ilk kağıdınızı yazdınız; bugün yenisini yazdırıyorsunuz ve bu kez soruların yarısı döngülerden geliyor, çünkü 8. haftayı artık işlediniz. Kural aynı: hoca sınava benzer soru yayımlamaz, provayı siz üretirsiniz; asistan soruları yazar, cevapları söylemez, siz 60 dakikada kağıt ve kalemle çözer, sonra puanlatır ve her kodu Playground'da doğrularsınız. İki kağıdın puanını yan yana koymak bugünün en öğretici dakikası olacak.",
  "bloklar": [{"sure": 30, "konu": "İkinci deneme kağıdını ürettir ve çöz (ilk 30 dakika)",
    "yap": ["Aşağıdaki istemi Java Hocam becerinize verin; yalnızca soruları alın, cevap anahtarını İSTEMEYİN. İlk kağıttaki soruların tekrar gelmemesi için yeni bir sohbet açın.",
            "Telefon kapalı, 60 dakika. İç içe döngü sorusunda her (i, j) çifti için bir satır açın; break ve continue gördüğünüz yerde o turu işaretleyin; basamak döngüsünde kopya ve ters sütunlarını ayrı tutun.",
            "Emin olmadığınız soruya soru işareti koyup geçin; süre bitmeden geri dönün. Bu blok bitince beş dakika mola, sonra ikinci blokta devam."],
    "istem": "Sınav yazarı ve Java hocası gibi davran. Görev: Algoritma ve Programlama I dersinin 1-8. haftasını kapsayan, 60 dakikalık, kağıt üzerinde çözülecek 6 soruluk YENİ bir deneme kağıdı yaz ve ağırlığı döngülere ver: 2 kod izleme ve çıktı yazma (12-15 satırlık, Scanner'sız; biri sınırı dış sayaca bağlı iç içe for, biri içinde break ya da continue olan while), 1 boşluk doldurma (4 boşluk; Euclid EBOB döngüsü ya da basamak ayırma döngüsü), 1 hata sayma (bir sözdizimi, bir sonsuz döngü, bir 'bir eksik/bir fazla' mantık hatası gömülü 10-12 satır), 1 kısa program tamamlama (iskelet verilsin; gözcü değerle biten toplam ya da asal testi, döngü gövdesi boş), 1 karışık izleme (tam sayı bölmesi, kısa devre ve break'i unutulmuş switch aynı kodda). Biçim: yalnızca soruları ver, her soruya puan yaz; CEVAPLARI SÖYLEME. 60 dakika sonra ben cevaplarımı yazınca puanla ve her yanlışın nedenini anlat. " + BAGLAM + ". Kodlu her sorunun çıktısını Playground'da çalıştırıp senin anahtarınla karşılaştıracağım; uymazsa kazanan Playground.",
    "ajan": None,
    "sina": ["İç içe döngü sorusunda gövdenin toplam kaç kez çalıştığını çıktıyı yazmadan önce hesapladınız mı?",
             "Hata sayma sorusundaki sonsuz döngüde 'koşulu yanlış yapan satır' neden yoktu?",
             "Boşluk doldurmada döngü koşulunu ilk seferde doğru yazabildiniz mi?"]},
   {"sure": 30, "konu": "Kağıdı bitir, puanlat, Playground'da doğrula ve iki kağıdı karşılaştır",
    "yap": ["Kalan soruları bitirin. Süre dolunca cevaplarınızı asistana yazın ve puanlatın; her yanlışın nedenini okuyun ama ona hemen inanmayın.",
            "Kodlu her soruyu Playground'da çalıştırın: asistanın anahtarı ile gerçek çıktı farklıysa kazanan Playground.",
            "İlk kağıdınızın (16. gün) puanını ve yanlış listesini yanına koyun: hangi konu listeden çıktı, hangisi hâlâ orada, hangisi yeni girdi? Bu üç sütunlu liste yarının programı."],
    "istem": "İkinci deneme kağıdındaki cevaplarım aşağıda; altında bir hafta önceki ilk kağıdımdaki yanlış konuların listesi var. Görev: her soruyu puanla, yanlışların nedenini ve doğru cevapların gerekçesini anlat; sonra iki listeyi karşılaştır ve üç başlıkta yaz: düzelen konular, hâlâ zayıf konular, yeni çıkan konular. Hâlâ zayıf her konu için yarın çalışmam gereken tek kuralı bir cümleyle ver. Biçim: soru soru, kısa; sonunda üç başlıklı liste. " + BAGLAM + "; kodlu sorularda senin anahtarınla Playground çıktısı farklıysa Playground'a güveneceğim, bu yüzden her çıktı için 'Playground'da şunu çalıştır' satırı ekle.\n[SORULAR VE CEVAPLARIM]\n[İLK KAĞIDIMDAKİ YANLIŞ KONULAR]",
    "ajan": None,
    "sina": ["İki kağıt arasında puanınız nasıl değişti; hangi soru türünde ilerlediniz?",
             "İki kağıtta da yanlış yaptığınız bir konu var mı? Varsa yarının ilk işi o.",
             "60 dakika bu kez yetti mi; süreyi en çok hangi soru yedi?"]}],
  "tekrar": ["Beşinci tur: Hafta 1-8'nin tamamı (ikinci deneme kağıdınızla).", "İki kağıdın yanlış listesi yarının (24. gün) programını belirler."]},

 {"gun": 24, "tarih": "2026-11-22", "baslik": "Zayıf konular ve portfolyo sorusunun son provası", "yogunluk": "orta",
  "ozet": "Pazar, iki blok. Sınava iki gün var ve bugün yeni hiçbir şey öğrenmiyorsunuz: iki deneme kağıdının ortak yanlışlarını kapatıyor, sonra sınavdaki 10 puanlık portfolyo sorusunu, yani KT1 sürümünüzdeki seçim yapısını son kez ezbere kağıda yazıyorsunuz. Bu soru sınavın en garanti puanı, çünkü cevabı sizin kendi kodunuz.",
  "bloklar": [{"sure": 25, "konu": "İki kağıdın ortak yanlışları: hedefli tekrar",
    "yap": ["Dünkü üç sütunlu listeden yalnızca 'hâlâ zayıf' ve 'yeni çıkan' konuları alın; her biri için ders notunun yalnızca o kapsülünü ya da bölümünü açın, 'Temel Kavramlar' maddesini sesli okuyun ve kapatın.",
            "Her zayıf konu için Playground'da iki küçük alıştırma: biri 'önce tahmin sonra çalıştır', biri 'bilerek boz ve düzelt'.",
            "Aşağıdaki istemle asistana listenizi verin ve sizi yalnızca o konularda sorguya çekmesini isteyin; cevapları Playground'da doğrulayın."],
    "istem": "Java hocası gibi davran. Görev: aşağıda iki deneme kağıdımda da yanlış yaptığım ya da ikincisinde yeni çıkan konuların listesi ve her biri için benim yanlış cevabım var. Beni yalnızca bu konularda sorguya çek: her seferinde tek soru, soruların çoğu 'bu kod ne yazar?' biçiminde (Scanner'sız, 10 satırı geçmeyen), doğru cevaplarsam aynı konuda bir zorlaştır, yanlışsa ipucu ver, ikinci yanlışta açıkla ve o konuyu listede tut. Biçim: 8 soru, sonunda hangi konunun artık tamam, hangisinin hâlâ zayıf olduğunu yaz. " + BAGLAM + ", sınava iki gün kaldı; her kodu Playground'da çalıştırıp senin cevabınla karşılaştıracağım, uymayan yerde kazanan Playground ve ders notu.\n[KONU LİSTESİ VE YANLIŞ CEVAPLARIM]",
    "ajan": "Bu klasördeki Lab dosyalarımı (Lab 1'den Lab 8'e kadar .java dosyaları) oku. Dosyalara bakarak hangi konuda en çok takıldığımı söyle: tip ve tür dönüşümü mü, seçim yapıları mı, tek döngüler mi, iç içe döngüler mi? Gerekçeni dosyalardan satır göstererek ver (dosya adı ve satır numarası). Hiçbir dosyayı DEĞİŞTİRME ve düzeltme yazma; sonunda bana o konuda sorguya çekilmem için üç soru öner, cevaplarını yazma.",
    "sina": ["İki kağıtta da yanlış çıkan konunun kuralını bakmadan tek cümleyle söyleyebiliyor musunuz?",
             "Zayıf konudaki alıştırmada 'önce tahmin' bu kez tuttu mu?",
             "Asistanın sorularından birinde Playground farklı bir sonuç verdi mi? Verdiyse kim haklıydı?"]},
   {"sure": 25, "konu": "Portfolyo sorusunun son provası (üçüncü) ve kapanış",
    "yap": ["KT1 sürümünüzdeki seçim yapısını kağıda ezbere yazın: Scanner satırı, okunan değişken, karşılaştırma, dallar, ekrana yazılan metin ve ayırt edici kuralınızın koşulu. Sonra depodaki KT1 sürümüyle satır satır karşılaştırın; 17. günden daha az eksik olmalı.",
            "Dikkat: sınavdaki soru KT1 sürümünden gelir, KT2 için eklemekte olduğunuz döngülü menüden değil. Deponuzda 6 Kasım'daki halini görmek için commit geçmişinden o tarihteki Uygulama.java'yı açın.",
            "Sınav günü kutusunu okuyun ve salonunuzu not edin: A şubesi A304-306, B şubesi A306 ve A404-406; 24 Kasım Salı 17.00."],
    "istem": "Java hocası gibi davran. Görev: aşağıya KT1 sürümümdeki seçim yapısını ezbere kağıda yazıp bilgisayara geçirdiğim halini, altına da depodaki gerçek halini yapıştıracağım. İkisini satır satır karşılaştır: ezberden yazdığımda eksik ya da farklı olan satırları söyle, ama doğrusunu yazma; her fark için 'bu satırda neyi unuttun?' biçiminde bir soru sor. Biçim: fark listesi, sonunda sarkan else, sınır değeri ve noktalı virgül açısından kısa bir kontrol. " + BAGLAM + " ve bu kodu kağıda yazmam istenecek; farkları kendim düzeltip programı çalıştırarak doğrulayacağım.\n[EZBERDEN YAZDIĞIM]\n[DEPODAKİ]",
    "ajan": None,
    "sina": ["KT1 seçim yapınızı ezbere yazdığınızda bu kez kaç satır eksikti?",
             "Ayırt edici kuralınızın koşulunu (karşılaştırma operatörüyle birlikte) bakmadan yazabiliyor musunuz?",
             "Sınavda kod izlerken ilk yapacağınız şey ne?"]}],
  "tekrar": ["Hedefli tekrar: yalnızca iki kağıdın yanlış listesi. Portfolyo provası 3/3.", "Yarın: sınavdan önceki gün, yalnızca cep kartı."]},

 {"gun": 25, "tarih": "2026-11-23", "baslik": "Sınavdan önceki gün: hafif tur, erken uyku", "yogunluk": "hafif",
  "ozet": "Pazartesi, tek ve kısa blok. Sınav yarın, 24 Kasım Salı 17.00'de. Yirmi beş günün işi bitti; bugün yeni soru çözmek puan kazandırmaz, yorgunluk ise kaybettirir. Tek bir kısa hatırlama turu yapıyor, çantanızı ve salonunuzu hazırlıyor ve erken yatıyorsunuz. Yarın kağıdın karşısında yalnız olacaksınız ama hazırlıksız olmayacaksınız.",
  "bloklar": [{"sure": 15, "konu": "Son hatırlama turu ve sınav hazırlığı (kısa blok)",
    "yap": ["Kağıda bakmadan şu beş şeyi yazın: for döngüsünün üç parçası, do-while'ın sonundaki işaret, break ile continue farkı, Euclid döngüsünün koşulu, 7 / 2 ve 7 % 2 sonuçları. Sonra ders notuyla karşılaştırın.",
            "Sınav günü kutusunu bir kez daha okuyun. Çantanıza öğrenci kimliğinizi, iki kalem ve bir silgi koyun; salonunuzu kontrol edin (A şubesi A304-306, B şubesi A306 ve A404-406) ve 16.45'te kapıda olacak şekilde plan yapın.",
            "Bu akşam ekranı erken kapatın. Aşağıdaki istem isteğe bağlıdır ve yalnızca beş dakikalık bir ısınmadır; yeni konu açmayın."],
    "istem": "Sakin ve cesaret veren bir Java hocası gibi davran. Görev: yarınki sınavdan önce bana yalnızca beş kısa ısınma sorusu sor; hepsi 1-8. haftanın en temel kurallarından olsun (tam sayı bölmesi, else-if sırası, switch'te break, döngü bitince sayacın değeri, iç içe döngüde tur sayısı) ve hiçbiri 5 satırdan uzun kod içermesin. Biçim: tek tek sor, cevabımı bekle, doğruysa tek kelimeyle onayla, yanlışsa kuralı bir cümleyle hatırlat; beş sorudan sonra dur ve yeni konu açma. " + BAGLAM.replace(VIZE, "yarın 17.00'de kağıt üzerinde vizem var") + "; emin olamadığım cevabı ders notundan doğrulayacağım.",
    "ajan": None,
    "sina": ["Sınav saat kaçta ve hangi salonda; yanınızda ne olacak?",
             "Kod izleme sorusunda kağıda ilk çizeceğiniz şey ne?",
             "Yirmi beş günde hangi konu 'bilmiyordum, artık biliyorum' oldu?"]}],
  "tekrar": ["Son tur: yalnızca cep kartı ve beş temel kural.", "Sınav: 24 Kasım Salı 17.00-18.00. A şubesi A304-306, B şubesi A306 ve A404-406."]},
]

d["gunler"] = [x for x in d["gunler"] if x["gun"] <= 17] + YENI

# 5) Sınav günü ve SSS
d["sinavGunu"] = [
    "Ne zaman, nerede: 24 Kasım Salı 17.00-18.00. A şubesi A304-306, B şubesi A306 ve A404-406. On beş dakika önce kapıda olun; öğrenci kimliğiniz yanınızda olsun.",
    "Kağıt ve kalem: sınav kağıt üzerinde, telefon ve bilgisayar kapalı (kırmızı bölge). Silgili kalem ve müsvedde için boş bir yüz ayırın.",
    "Önce tahmin: kodlu her soruda çıktıyı yazmadan önce programı satır satır kafanızda çalıştırın; bu yirmi beş gündür Playground'da yaptığınız şeyin Run'sız hali.",
    "Kod izlemede tablo tutun: her değişken için bir sütun, her tur için bir satır; iç içe döngüde her (i, j) çifti bir satırdır ve döngü değişkeninin bittikten sonraki değerini de yazın.",
    "Hata sayarken üç türü sırayla sorun: derleyici görür mü (sözdizimi), çalışırken çöker mi (çalışma zamanı), çalışır ama yanlış mı (mantık).",
    "Portfolyo sorusu sizin kodunuz: KT1'deki seçim yapısını üç kez prova ettiniz; Scanner satırı, karşılaştırma, dallar, noktalı virgüller.",
    "Takıldığınız soruya soru işareti koyup geçin; süre bitmeden geri dönün. Boş bırakılan çıktı satırı sıfır, yanlış tahmin kısmi puan alabilir.",
]
d["sss"][0] = {"q": "Yirmi beş günün hepsini yapamazsam?",
               "a": "Planı bir reçete gibi değil bir harita gibi okuyun. Bir gün kaçırdıysanız o günü yetiştirmeye çalışmayın; ertesi günün bloğunu yapın ve kaçırdığınız konuyu en yakın tekrar bloğuna sıkıştırın. Plana bugün başlıyorsanız ikinci tur (18-25. günler, 16-23 Kasım) tek başına da işe yarar. En vazgeçilmez dört gün: 18. gün (iç içe döngüde iz tablosu), 21. gün (karışık izleme), 23. gün (ikinci deneme kağıdınız) ve 24. gün (zayıf konular ve portfolyo provası)."}
d["sss"][3]["a"] = ("Hayır. Sınavın kendisi öğrenmenin parçasıdır; hoca sınava benzer soru yayımlamaz, bu yüzden provanızı kendiniz üretirsiniz. "
                    "Soru türleri ve kapsam bu sayfada açık: kod izleme, boşluk doldurma, hata sayma, program tamamlama ve portfolyo sorusu. "
                    "16. ve 23. günlerin istemleri bu formatta birer kağıt ürettirir; önemli olan cevapları ezberlemek değil, izleme tablosu tutma, "
                    "hata türünü ayırt etme ve koşulu Türkçeye çevirme alışkanlıkları.")
if not any("derslerle birlikte" in x["q"] or "Sınav günü ders" in x["q"] for x in d["sss"]):
    d["sss"].append({"q": "Sınav haftasında dersler ve lablar var mı?",
                     "a": "Var. Bu dönem ara sınavlar derslerle birlikte yapılıyor; ayrı bir sınav haftası yok. 20 Kasım Cuma dersi (metotlar I), 18-19 Kasım'daki Lab 8 ve 25-26 Kasım'daki Lab 9 her zamanki saatinde. Sınavın kendisi 24 Kasım Salı 17.00-18.00 arasında; metotlar sınav kapsamında değil."})

P.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(len(d["gunler"]), "gün,", sum(len(x["bloklar"]) for x in d["gunler"]), "blok")
