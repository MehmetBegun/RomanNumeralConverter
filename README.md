# RomanNumeralConverter

Roma rakamlarını ondalık sayılara dönüştüren basit bir Python programı.

## Özellikler

- Tek haneli Roma rakamlarını dönüştürme (I, V, X, L, C, D, M)
- Çıkarma kurallarını uygulama (örn. IV = 4, IX = 9)
- Basit komut satırı arayüzü

## Roma Rakamları Değerleri

| Roma Rakamı | Değer |
|------------|-------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

## Kullanım

```
python converter.py
```


Örnek:
```
Enter a Roman Numeral: XIV
The integer value is: 14
```


## Kurallar

- Toplama: XVI = 10 + 5 + 1 = 16
- Çıkarma: IV = 5 - 1 = 4
