# CODEXPROJE1

Basit bir doğrusal eşlenik üreteç (LCG) ile deterministik bir rastgele sayı üreteci.

## Kullanım

CLI aracını çalıştırmak için:

```bash
python rng.py <adet> <minimum> <maksimum> [--seed <tohum>]
```

Örnek:

```bash
python rng.py 5 1 10 --seed 12345
```

## Form arayüzü

Basit Tkinter formunu açmak için:

```bash
python rng.py --gui
```

Formda bir metin kutusu ve "Üret" düğmesi bulunur. Metin kutusuna 0 veya daha
büyük bir sayı yazıp düğmeye bastığınızda, 0 ile girdiğiniz sayı arasında bir
değer üretir. İsterseniz deterministik davranış için `--seed` bayrağını da
kullanabilirsiniz.

## C# alternatifi (Form ve CLI)

Python sürümünün yanında, aynı doğrusal eşlenik üreteci ile çalışan C# tabanlı
bir WinForms uygulaması da eklendi. Bu sürüm Windows ve .NET 6+ ortamı
gerektirir.

### C# GUI

```bash
dotnet run --project csharp/RandomGenerator.csproj
```

Uygulamada bir metin kutusu ve "Üret" düğmesi bulunur; 0 ile girdiğiniz üst sınır
arasında sayı üretir.

### C# CLI

```bash
dotnet run --project csharp/RandomGenerator.csproj -- --cli <üst_sınır>
```

İsteğe bağlı olarak ilk argüman olarak bir tohum değeri verebilirsiniz:

```bash
dotnet run --project csharp/RandomGenerator.csproj -- --cli 12345 50
```

Bu komut 0 ile 50 arasında deterministik bir değer üretir.

### Neden Python ve C#?

Başlangıçta Python tercih edilmesinin nedeni platform bağımsızlığı ve GUI için
minimum bağımlılıkla hızla çalıştırılabilir olmasıydı. C# tercih edenler için
aynı algoritma ve arayüz artık WinForms ile sağlandı; .NET kurulu bir Windows
makinede doğrudan çalıştırabilirsiniz.

## Testler

```bash
python -m unittest
```
