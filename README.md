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

## Testler

```bash
python -m unittest
```
