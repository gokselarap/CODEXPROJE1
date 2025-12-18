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

## Testler

```bash
python -m unittest
```
