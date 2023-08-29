# Python Programlamak

## Yorum Satırları
Pyhton dilinde yorum satırı nasıl oluşturulur.

```python
# Single Line Comment (Tek Satır Yorum)

"""
Multi Line Comment (Çok Satır Yorum)
"""
```

## String İşlemleri
Python dilinde iki diziyi bir leş tirmek için `+` karakteri kullanılır.

```python
"Concat" + "enate";
```

Python ile Strinlerin elemanlarına erişim sağlamak. Stringler de bir array olarak bilinir.

```python
string = "Data type is string array"

string[:]           # Tüm elemanları verir.
string[6]           # Altıncı elemenı verir.
string[5:8]         # Beş ile Sekiz arasındaki elemanları verir.
string[5:]          # Beşinci elemandan başlayıp son elemana kadar verir.
string[:10]         # Baştan başlayıp onuncu elemana kadar verir.
string[::2]         # Baştan başlayıp ikişer artırarak bütün elemanları verir.
string[0:19:2]      # Sıfırdan başlayıp on dokuza kadar ikişer artırarak elemanları verir.
string[-1:]         # Sondan eksi bir karakteri verir.
string[:-1]         # Baştan eksi bir yapılırsa tüm elemanlar verir.
```

## Aritmatik Operatorler
Pyhton ile aritmatik işlemler.

```python
num1 = 2 + 4			# Addition
num2 = 6 - 4			# Subraction
num3 = 3 * 3			# Multiplication
num4 = 10 / 2			# Divition
num5 = 10 % 3			# Modules
num6 = 2 ** 3			# Exponent
num7 = 8 // 3			# Floor Divition
```

## Karşılaştırma Operatorleri
Python ile karşılaştırma operatörleri.

```python
==          # Equal
!=          # Not Equal
<           # Less than
>           # Greater than
<=          # Less than or equal
>=          # Greater than or equal
is          # The same object as
in          # Içinde
```

## Mantıksal Operatorler
Python ile mantıksal operatörleri

```python
and         # Her iki şart gerçekleşir ise True döner.
or          # Her iki Şart dan biri gerçekleşir ise True döner
not         # Gerçekleşen şartın tam tersini alır.
```
