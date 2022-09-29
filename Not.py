# !----------------> import os <----------------!   # https://docs.python.org/2.7/library/os.path.html
os.path.isdir(path)                     # Verilen yol mevcut ise true olarak dönüşyapar
os.chdir(path)                          # Geçerli çalışma alanını verilen yol ile değiştir. Dönüş değeri yoktur
os.listdir(path)                        # Verilen yol içerisindekileri liste olarak döner.

# !----------------> import subprocess <----------------!   # https://docs.python.org/2.7/library/subprocess.html
subprocess.call(args)                  # Array olarak verilen bir komutları çalıştırır dönüş olarak int değeri döner.

# !----------------> import popen2 <----------------!   # https://docs.python.org/2.7/library/popen2.html Deprecated since version 2.6

# !----------------> File Object <----------------!  # https://docs.python.org/2.7/library/stdtypes.html#file-objects
.write(strData)                         # Dosya içeriğine veri yazar. Dönüş değeri yoktur.
.close()                                # Açık olan dosyayı kapatır. Dönüş değeri yoktur.
.read()                                 # Dosya donuna kadar okur ve bir string olarak döner.
.read(size)                             # Verilen bayt kadar okur ve bir string olarak döner.
.readline()                             # Dosyadan ilk statırı okur ve string olarak döner.
.readline(size)                         # Verilen bayt kadar ilk statırı okur ve string olarak döner.
.readlines()                            # Dosyayı sonuna kadar satır satır oku ve liste olarak dönüşyapar.
.readlines(sizehint)                    # Dosyayı belritilen size kadar oku ve liste olarak dönüşyapar.
.seek(offset)                           # Dosya imlecinin konumunu ayarla

# !----------------> Mapping Types <----------------!  # https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
.items()                                # Dictionary için bir key, value listesi döner.
.iteritems()                            # Dictionary için bir key, value listesi döner.

# !----------------> String Methods <----------------!  # https://docs.python.org/2.7/library/stdtypes.html#string-methods
.ascii_letters                          # Alfabetik olan büyük küçük karakterlerin tanımı.
.ascii_lowercase                        # Alfabetik olan küçük karakterlerin tanımı.
.ascii_uppercase                        # Alfabetik olan büyük karakterlerin tanımı.
.digits                                 # Tüm rakamları verir.
.whitespace                             # Tüm boşluk karakterleri
.capitalize()                           # Dizenin ilk karakterini büyük geri kalanı küçük olarak döner.
.center(width)                          # Belitilen değer kadar boşluk bırakır.
.center(width, fillchar)                # Belitilen değer ve karakter kadar karakteri doldurur.
.startswith(prefix)                     # Dize verilen ek ile başlıyor ise true yoksa false döner.                                      örn: x.startswith("M")
.startswith(prefix, start, end)         # Dize verilen ek, başlangıç ve bitiş belirtilerek başlıyor ise true yoksa false döner.         örn: x.startswith("Ş", 6, 10)
.endswith(prefix)                       # Dize verilen ek bitiyor ise true yoksa false döner.                                           örn: x.endswith("k")
.endswith(prefix, start, end)           # Dize verilen ek, başlangıç ve bitiş belirtilerek bitiyor ise true yoksa false döner.          örn: x.endswith("türk", 0, 13)
.count(sub)                             # Dize içerisinde a karakterini sayar ve döner                                                  örn: x.count("M") 
.count(sub, start, end)                 # Dize içerisinde a karakterini belirtilen başlangıç ve bitiş arasında sayar ve döner           örn: x.count("M", 0, 12) 
.find(sub)                              # Dize içerisinde belitilen kelimeyi sayar.
.find(sub, start, end)                  # Dize içerisinde Start ve end arasındaki belitilen kelimeyi sayar.
.isalpha()                              # Dizedeki tüm karakterler alfabetikse ture olarak döner.
.isdigit()                              # Dizedeki tüm karakterler rakamsa ture olarak döner.
.islower()                              # Dizideki tüm karaktarler küçük ise ture olarak döner.
.isupper()                              # Dizideki tüm karaktarler büyük ise ture olarak döner.
.isspace()                              # Dizede yalnızca boşluk karakterleri varsa ture olarak döner.
.join(iterable)                         # Verilen Dizeyi birleiştirmeisi ile bir dize döner.
.ljust(width)                           # Verilen width kadar sağdan boşluk bırakır
.ljust(width, fillchar)                 # Verilen width kadar sağdan fillchar ile doldurur
.lower()                                # Tüm Büyük karakterleri küçük karakter olarak dönüştürür.
.lstrip(chars)                          # Dizenin başında verilen karakterlerden eşleşen varsa onları siler.
.replace(old, new)                      # Dizenin içerisinde var olan bir kelimeyi yenisi ile değiştirir.
.replace(old, new, count)               # Dizenin içerisinde var olan bir kelimeyi yenisi ile değiştirir. Belirtilen count kadar değiştirir.
.rfind(sub)                             # Dizin içerisin sağdan arama işlemi yapar.
.rfind(sub, start, end)                 # Dizin içerisin Başlangıç ve bitiş rasında sağdan arama işlemi yapar.
.rjust(width)                           # Verilen width kadar soldan boşluk bırakır
.rjust(width, fillchar)                 # Verilen width kadar soldan fillchar ile doldurur
.split(sep)                             # Verilen kelime ile böl array olarak dönüş yapar.
.split(sep, maxsplit)                   # Verilen kelime ile maxsplit kadar böl array olarak dönüş yapar.
.rstrip(chars)                          # Dizenin sonundan verilen karakterlerden eşleşen varsa onları siler.
.splitlines()                           # Dizedeki new linelardan bölerek bir array döner.
.splitlines(keepends)                   # Dizedeki new linelardan bölerek keepends True olarak verilirse new linelarıda ekleyip bir array döner.
.swapcase()                             # Dizenin içerisinde bğyğk harfli karakter var ise küçük harfe çevirir.
.upper()                                # Dize içerisindeki tüm karaktarleri büyük yapar.
.zfill(width)                           # Dize içerisine sıfırlar doldurur.

# !----------------> List Data Structures <----------------! # https://docs.python.org/2.7/tutorial/datastructures.html
.append(x)                              # Listenin sonuna bir öge ekler. Dönüş değeri yoktur                  örn: x.append("1")
.count(x)                               # Liste içerisin x değerinin sayısını döner.
.index(x)                               # Liste içerisinde x değerinde bir değer varsa onun indexini döner.
.insert(i, x)                           # Liste içerisine belitilen indexe insert eder.

# !----------------> Methods <----------------! # https://docs.python.org/2.7/library/functions.html
open(filename, mode)                    # Bir dosya oluşturur yada açar
input(prompt)                           # Sadece Interger data tipi okur
raw_input(prompt)                       # String data tipi okur
range(stop)                             # Verilen değer arasında bir list oluşturur.
range(start, stop)                      # Verilen iki değer arasında bir list oluşturur.
range(start, stop, step)                # Verilen iki değer arasında 5 er olarak artırılmş bir list oluşturur.
len(s)                                  # Verilen nesnenin öge sayısını verir.
type(obj)                               # Verline nesnenin tipini verir
list()                                  # Liste oluşturur.
min(iterable)                           # Bir liste içerisindeki en küçük sayı değerini döner.
max(iterable)                           # Bir liste içerisindeki en büyük sayı değerini döner.
pow(x, y)                               # x değerinin y kuvvettini döner.
abs(x)                                  # Bir sayının mutlak değerini döner.
sum(iterable)                           # Bir ögenin ögelerinin toplamını döner.
sorted(iterable)                        # Yeni bir sıralanmış liste döner.
str(obj)                                # Verilen değeri string olarak döner.
int(x)                                  # Bir string tipinde tam sayı değerini int tipne dönüştür.
chr(i)                                  # Berilen sayı değerinin ASCII kod karşılığını dönderir.





# !----------------> List <----------------!
new_list = [49, 3.14, 'Joke']       # list Tanımlanır
new_list[0] = 50                    # listenin ilk elemenına değer atanır.

string = "Data type is string array"
string[6]           # Altıncı elemenı verir.
string[5:8]         # Beş ile Sekiz arasındaki elemanları verir.
string[:]           # Tüm elemanları verir.
string[5:]          # Beşinci elemandan başlayıp son elemana kadar verir.
string[:10]         # Baştan başlayıp onuncu elemana kadar verir.
string[::2]         # Baştan başlayıp ikişer olarak artırarak bütün elemanları verir.
string[0:19:2]      # Sıfırdan başlayıp on dokuza kadar ikişer olarak artırarak elemanları verir.
string[-1:]         # Sondan eksi bir karakteri verir.
string[:-1]         # Baştan eksi bir yapılırsa tüm elemanlar verir.

dictionary = {"key_1": 1, "key_2": 2, "key_3": 3}

# !----------------> Basic Functions <----------------!
def get_info():                     # Function
    print("Test")
def get_info2(name, index):         # Function parameters
    print(name + " " + index)
def get_info3(name = "Test", index = 0):     # Function default parameters
    print(name + " " + index)
def get_info4():                     # Function return type
    return 4 * 3

# !----------------> Loops <----------------!
while(True):
    print("Test")

for i in range(10):
    print("Test")

# !----------------> If Statement <----------------!
x = 25
if(x == 25):
    print("Equalse")
elif(x == 15):
    print("Equalse")
else:
    print("Not Equalse")

# !----------------> Logical Opertators <----------------!
and         --> # Her iki şart gerçekleşir ise True döner.
or          --> # Her iki Şart dan biri gerçekleşir ise True döner
not         --> # Gerçekleşen şartın tam tersini alır.

# !----------------> Opertators <----------------!
==          --> # Equal
<           --> # Less than
>           --> # Greater than
<=          --> # Less than or equal
>=          --> # Greater than or equal
is          --> # The same object as
in          --> # Içinde 

# !----------------> Escape Characters <----------------!
\n          --> # Yeni satır
\t          --> # Tab boşluk
\\          --> # Backslah
\r          --> # Yenileme

# !----------------> Operating on Data <----------------!
Addition            ---> 2 + 4 = 6
Subraction          ---> 6 - 4 = 2
Multiplication      ---> 3 * 3 = 9
Divition            ---> 10 / 2 = 5
Modules             ---> 10 % 3 = 1
Exponent            ---> 2 ** 3 = 8
Floor Divition      ---> 8 // 3 = 2

# !----------------> Data Types <----------------!
Interger    ---> -3, -2, -1, 0, 1, 2, 3
Floats      ---> -3.14, -1.2, 0.1442, 8.91
Booleans    ---> True = 1 or False = 0
Strings     ---> "Hello World!", 'Hello World!'
Characters  ---> 'a', 'b', 'c', 'd', 'e'