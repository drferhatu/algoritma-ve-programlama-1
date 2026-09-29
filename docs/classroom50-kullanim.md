# Classroom 50 yönetim rehberi (öğretim üyesi ve lab sorumlu hocası)

Bu belge siteye girmez; ders ekibi içindir. Öğrenciye dönük anlatım `content/guides/classroom-50.md` dosyasında (sitede `/rehber/classroom-50`).

## 1. Kurulu yapı

| Alan | Değer |
|---|---|
| Platform | [classroom50.org](https://classroom50.org) (CS50 ekibi, ücretsiz, açık kaynak) |
| GitHub organizasyonu | `FiratUniversity-FerhatUcarsLAB` |
| Classroom | "Algoritma ve Programlama I", kısa ad (slug) `algo1` |
| Classroom sayfası | `https://classroom50.org/FiratUniversity-FerhatUcarsLAB/algo1` |
| Lab 1 ödevi | slug `lab01`, bireysel, private depo |
| Lab 1 şablon deposu | `FiratUniversity-FerhatUcarsLAB/algo1-lab01-template` (README + .gitignore) |
| Öğrenci deposu adı | `algo1-lab01-KULLANICIADI` (org içinde) |
| Kabul bağlantısı | `https://classroom50.org/FiratUniversity-FerhatUcarsLAB/algo1/assignments/lab01/accept` |
| Otomatik kontrol | Her push'ta GitHub Actions; sonuç öğrenci deposunun Releases sayfasında ve "Feedback" pull request'inde |
| Son teslim kuralı | Lab N teslimi, lab haftasının Cuma 23.59'u (Lab 1: 2 Ekim 2026) |

Portfolyo (dönem projesi) ayrı bir Classroom 50 ödevi olarak açılacak; KT1 5. hafta, bağlantı 3-4. haftada verilecek. Öğrenciler artık kendi elleriyle `algo1-portfolyo` deposu açmıyor.

## 2. Roster (öğrenci listesi) yükleme

Kabul bağlantısı yalnızca organizasyona davet edilmiş hesaplarda çalışır; davet roster üzerinden gider.

1. Classroom sayfası → **Roster** → **Upload roster**.
2. Dosya biçimi: CSV'de `github_id`, `username` ya da `email` sütunlarından **biri** yeterli; ya da sütun başlığı olmadan satır satır kullanıcı adı / e-posta. **Download template** ile örnek dosya indirilebilir.
3. Yalnızca e-posta verilen satırlar e-postayla davet edilir; öğrenci daveti kabul edince kullanıcı adı roster'a bağlanır. Kullanıcı adı verilen satırlar doğrudan org davetine dönüşür.
4. **Refresh roster**: daveti kabul edenleri ve org üyeliği tamamlananları günceller. Sayfa kendi kendine yenilenmez; düğmeye basmak gerekir.

Öneri: dönem başındaki resmi listedeki üniversite e-postalarıyla bir kez toplu yükleme yapın; GitHub hesabını başka e-postayla açanlar lab günü kullanıcı adıyla eklenir.

## 3. Lab günü akışı

1. Öğrenciler GitHub hesabı açar; lab sorumlu hocası kullanıcı adlarını toplar (kağıt liste ya da anlık form).
2. Toplanan kullanıcı adları CSV'ye yazılıp **Upload roster** ile toplu yüklenir (tek tek de eklenebilir). Önceden yüklenmiş satırlar korunur; yeni satırlar eklenir.
3. 5-10 dakikada bir **Refresh roster**; daveti kabul etmemiş öğrencilere e-posta / bildirim / `github.com/FiratUniversity-FerhatUcarsLAB` → "View invitation" yolunu hatırlatın.
4. Daveti kabul eden öğrenci kabul bağlantısına tıklar, "Accept assignment" der; depo saniyeler içinde oluşur. "Not a member yet" görürse davet henüz kabul edilmemiştir: kabul edip **Check again**.
5. Öğrenci depoyu Codespaces'te açar ya da klonlar; dosyaları kök dizine koyar; commit + push.
6. Push'tan 1-2 dakika sonra Releases sayfasında sonuç. Öğrenci Cuma 23.59'a kadar istediği kadar push edebilir.

## 4. Puanları toplama (Submissions)

1. Classroom → ödev (`lab01`) → **Submissions**.
2. **Collect now**: bütün öğrenci depolarındaki son otomatik kontrol sonuçlarını toplar (arka planda `collect-scores` iş akışı çalışır; birkaç dakika sürebilir, sayfayı yenileyin).
3. **Download scores**: CSV indirir (kullanıcı adı, puan, son commit zamanı). Cuma 23.59 sonrası bir kez toplayıp CSV'yi saklamak yeterli; geç push'ları ayıklamak için commit zamanına bakın.
4. Kod kalitesi ve "30 saniye anlat" değerlendirmesi otomatik puana dahil değildir; lab sorumlu hocası bunu ayrıca tutar (CSV'ye sütun ekleyerek).
5. Bireysel geri bildirim: öğrenci deposundaki **Feedback** pull request'ine yorum yazın; öğrenci depo sayfasında görür. Kod satırına yorum yapmak için PR'daki "Files changed" sekmesi kullanılır.

## 5. Staff (ders ekibi) ekleme ve roller

Classroom → **Settings** → **Staff and roles**.

| Rol | GitHub gereksinimi | Ödev oluşturur | Notları görür | Geri bildirim verir | Collect çalıştırır |
|---|---|---|---|---|---|
| Teacher | Org **owner** olmalı | Evet | Evet | Evet | Evet |
| Head TA | Org üyesi | Hayır | Evet | Evet | Evet |
| TA | Org üyesi | Hayır | Evet | Evet | Hayır |

Lab sorumlu hocasını önce organizasyona üye yapın (GitHub → org → People → Invite member), sonra Classroom 50'de TA ya da Head TA olarak ekleyin. Ödev oluşturması gerekiyorsa org owner yapılıp Teacher rolü verilmelidir.

## 6. Yeni lab ödevi açma

1. Şablon deposu hazırlayın: org altında `algo1-labXX-template` (README ile görev özeti, `.gitignore` içinde `*.class`). Depo ayarlarında **Template repository** işaretli olmalı.
2. Classroom → **Create assignment**: slug `labXX`, başlık "Lab XX · ...", türü bireysel, görünürlük private, şablon depo seçilir. Öğrenci deposu adı otomatik `algo1-labXX-KULLANICIADI` olur.
3. **Tests** bölümünde testleri ekleyin (bkz. 7). Her testin adı, puanı ve tipi vardır; toplam 100 olacak şekilde dağıtın.
4. Kaydedin; kabul bağlantısı `.../assignments/labXX/accept` biçiminde üretilir. Bağlantıyı lab sayfasına (`content/labs/lab-XX.md`, "Lab XX kabul bağlantısı" kutusu) ekleyin.
5. Kendi hesabınızla bir kez kabul edip testin çalıştığını doğrulayın (deneme deposunu sonra silin).

## 7. Test tipleri ve Lab 1 test tablosu

İki test tipi var:

- **Run command**: verilen komut çalıştırılır; çıkış kodu 0 ise test geçer. Derleme kontrolü için: `javac Merhaba.java`.
- **Input/Output**: komut çalıştırılır (isteğe bağlı stdin verilir), çıktı beklenen metinle karşılaştırılır. Karşılaştırma modu: `included` (beklenen metin çıktıda geçiyor), `exact` (birebir eşit) ya da `regex`. Lab görevlerinde `included` kullanıyoruz; öğrencinin ek satırları teste takılmaz.

Lab 1 testleri (toplam 100):

| # | Test | Tip | Komut | Beklenen | Puan |
|---|---|---|---|---|---|
| 1 | Merhaba derlenir | Run command | `javac Merhaba.java` | çıkış kodu 0 | 20 |
| 2 | Merhaba çıktısı | Input/Output (included) | `javac Merhaba.java && java Merhaba` | `Merhaba` | 10 |
| 3 | UcMesaj derlenir | Run command | `javac UcMesaj.java` | çıkış kodu 0 | 10 |
| 4 | IkiIslem kalan | Input/Output (included) | `javac IkiIslem.java && java IkiIslem` | `17 % 5 = 2` | 10 |
| 5 | DaireHesap alan | Input/Output (included) | `javac DaireHesap.java && java DaireHesap` | `38.48` | 10 |
| 6 | IsimKarti derlenir | Run command | `javac IsimKarti.java` | çıkış kodu 0 | 10 |
| 7 | CarpimTablosu | Input/Output (included) | `javac CarpimTablosu.java && java CarpimTablosu` | `5 x 10 = 50` | 20 |
| 8 | Bonus SaatDonusturme | Input/Output (included) | `javac SaatDonusturme.java && java SaatDonusturme` | `2 saat 3 dakika 4 saniye` | 10 |

Notlar: dosyalar deponun kök dizininde aranır (alt klasör yok). Çıktıda Türkçe karakter eşleşmesi için beklenen metinler ASCII tutuldu. Sonraki lablarda Scanner'lı programlar için stdin alanına girdi satırları yazılır.

## 8. Bilinen sınırlar

- Bağlantıyla katılım yok: öğrenci önce organizasyona davet edilmeli (roster). Davet edilmemiş öğrencide kabul sayfası "Not a member yet" der.
- Public depoda autograding çalışmaz; öğrenci depoları private kalmalı, öğrenci görünürlüğü değiştirmemeli.
- Roster, Submissions ve durum sayfaları kendini yenilemez; "Refresh roster", "Collect now" ve sayfa yenileme gerekir.
- Öğrenci depo adını değiştirmemeli, Actions'ı kapatmamalı; aksi halde sonuç toplanamaz.
- Otomatik puan yalnızca derleme ve belirtilen çıktı satırlarını ölçer; kod kalitesi ayrıca değerlendirilir.
- Classroom 50 aktif geliştirilen bir araç; arayüz adları (düğme etiketleri) sürümle değişebilir. Bir şey bulunamazsa [classroom50.org](https://classroom50.org) belgelerine bakın.

## 9. Komut satırı (gh-teacher)

GitHub CLI (`gh`) kuruluysa:

```bash
gh extension install foundation50/gh-teacher
gh teacher login          # admin:org kapsamı gerekir (org owner hesabıyla)
```

Örnekler:

```bash
# roster yükleme (CSV: github_id / username / email sütunlarından biri)
gh teacher roster import FiratUniversity-FerhatUcarsLAB algo1 roster.csv

# lab sorumlu hocasını TA olarak ekleme
gh teacher staff add FiratUniversity-FerhatUcarsLAB algo1 KULLANICI --role ta

# bütün öğrenci depolarını indirme (kod okuma, kopya kontrolü)
gh teacher download FiratUniversity-FerhatUcarsLAB algo1 lab01

# puan toplama iş akışını elle tetikleme
gh workflow run collect-scores.yaml --repo FiratUniversity-FerhatUcarsLAB/classroom50 -f classroom=algo1 -f assignment=lab01
```

Öğrenci tarafındaki karşılığı `gh extension install foundation50/gh-student` ve `gh student accept FiratUniversity-FerhatUcarsLAB algo1 lab01` (isteğe bağlı; rehberde küçük not olarak geçiyor).
