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

## Tek Terimli Operatorler

```python
+			# Pozitif operatörü
-			# Negetif operatörü
~			# Tümleme operatörü (Değili anlamınada geliyor.)

t = 5;
m = ~t		# 0101 		işaret bitleri 0 pozitif 1 negatif değerler alır. Her bir sayının başında bir işaret biti vardır.

# Bit bazın da değilini almak nasıl olur.
# (0101)' = 1010 olarak değili alınır.
```

## Benzerlik Operatorleri

```python
is				# Tip ve değer eşitliğini sağlar.
is not			# Tip ve değer eşitliğinin tersini sağlar.
```

## Bitwise Operatorleri
Pyhton ile ikilik tabanda karşılaştırma operatörleri

```python
&		# Bitwise and
|		# Bitwise or
~		# Bitwise not (Complement - Tümleyeni)
^		# Bitwise xor
>>		# Bitwise right shift
<<		# Bitwise left shift

# Yapılacak işlem bit bazında karşılıklarına bakarız.
x = 3;			# 0011
y = 2;			# 0010
s = x & y		# 0010

x = 11;			# 1011
y = 10;			# 1010
s = x | y		# 1011
s = x ^ y		# 0001

t = 7;
s = t >>= 2		# 0111 -> 0001

t = 3;
s = t <<= 2		# 0011 -> 1100
```

## Membership Operatorleri
```python
in				# Bir değerin içerisinde var mı
not in			# Bir değerin içerisinde yok mu
```

## Veri Tipleri
```python
# Tipsiz veritipi
x1 = None

# Numeric Veri tipi
x1 = 25			# int
x1 = 3.14		# float
x1 = True		# bool
x1 = 3 + 5j		# complex

# String halindeki veri tipleri
x1 = (1,2,3,4,5) 	# Tuple bir veritipi içeriği değiştirilemez.
z1 = "String data"; # String tipinde veri tipi.

```

