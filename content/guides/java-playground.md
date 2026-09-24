---
title: "Java Playground"
description: "Kurulum ve hesap gerektirmeyen, telefonda çalışan tarayıcı ortamı: nasıl kullanılır, arkasındaki JShell mantığı nedir, nerede yetersiz kalır."
order: 1
icon: "▶️"
---

## Nedir?

[dev.java/playground](https://dev.java/playground/), Oracle'ın tarayıcıda çalışan resmî Java ortamıdır. Kurulum yok, hesap yok, telefonun tarayıcısında bile çalışır. Derste yansıdaki kodu aynı anda kendi telefonunuzda çalıştırmak için kullanıyoruz.

## Nasıl kullanılır?

1. Adresi açın. Ortada bir kod alanı, üstte **Run** düğmesi var.
2. Kodu yazın ya da ders sayfasındaki bloktan kopyalayın.
3. **Run** (ya da `Ctrl+Enter`, Mac'te `Cmd+Enter`). Çıktı alttaki panelde belirir; hata varsa kırmızı mesaj aynı yerde.
4. Sayfayı yenilerseniz kod silinir. Saklamak istediğinizi notlarınıza kopyalayın.

## Neden sınıf ve main yazmıyoruz? JShell mantığı

Playground'un arkasında **JShell** çalışır: Java 9 ile gelen, kodu satır satır çalıştıran etkileşimli kabuk. Normal bir Java dosyasında zorunlu olan tören kısmı burada gerekmez:

```java
// Playground'da bu kadarı yeter:
int x = 7;
System.out.println(x * 6);
```

Aynı şey bir `.java` dosyasında şöyle yazılır:

```java
public class Deneme {
    public static void main(String[] args) {
        int x = 7;
        System.out.println(x * 6);
    }
}
```

İkisi de aynı işi yapar. Playground, "önce fikri dene" ortamıdır; dosya ise "programı sakla, derle, teslim et" ortamıdır. Laboratuvarda ikincisini kullanırsınız.

JShell'in ek kolaylıkları:

- Bir ifadeyi tek başına yazarsanız sonucu gösterir: `3 + 4` yazıp Run deyin.
- Metot tanımlayabilirsiniz; `class` içinde olması gerekmez.
- Aynı değişkeni yeniden tanımlayabilirsiniz; dosyada bu hata olur.

## Sınırları

- **Klavyeden girdi yok.** `Scanner` çalışmaz; girdi bekleyen kod donar ya da hata verir. Değerleri koda yazın; girdiyi laboratuvarda kendi ortamınızda deneyin.
- **Dosya yok.** Dosya okuma-yazma yapılamaz.
- **Kayıt yok.** Kodunuz sunucuda saklanmaz.
- **Uzun döngüler** bir süre sonra kesilir; milyonlarca turluk deneme için uygun değil.
- Bazı telefon klavyeleri `{` `}` `;` karakterlerini gizler; sembol klavyesini bulun ya da kodu sayfadan kopyalayıp yalnızca sayıları değiştirin.

## Derste nasıl kullanıyoruz?

Her hafta sayfasındaki **"Deneyin"** bloklarını Playground'a kopyalayıp önce çıktıyı tahmin edin, sonra çalıştırın. Tahmin tutmadıysa sebebini yanınızdakiyle tartışın; öğrenme o anda olur.

## Alternatifler

Playground açılmıyorsa (okul ağı, eski tarayıcı):

- [JDoodle Java](https://www.jdoodle.com/online-java-compiler) veya [OneCompiler Java](https://onecompiler.com/java): tam dosya ister (`class` + `main`), Scanner girdisi için ayrı bir kutu sunar.
- Kendi bilgisayarınızda `jshell` komutu: JDK kuruluysa terminale `jshell` yazın, aynı satır satır ortam açılır. Çıkmak için `/exit`.
