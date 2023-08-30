# !----------------> import os <----------------!   # https://docs.python.org/2.7/library/os.path.html
os.path.isdir(path)                     # Verilen yol mevcut ise true olarak dönüşyapar
os.chdir(path)                          # Geçerli çalışma alanını verilen yol ile değiştir. Dönüş değeri yoktur
os.listdir(path)                        # Verilen yol içerisindekileri liste olarak döner.

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

# !----------------> Mapping Types (Dictionary) <----------------!  # https://docs.python.org/2.7/library/stdtypes.html#mapping-types-dict
.items()                                # Dictionary için bir key, value listesi döner.
.iteritems()                            # Dictionary için bir key, value listesi döner.
.has_key(key)                           # Key olup olmadığını kontrol eder dönüş olarak boolean döner.(Python 2.7)

# !----------------> List Data Structures <----------------! # https://docs.python.org/2.7/tutorial/datastructures.html
.append(x)                              # Listenin sonuna bir öge ekler. Dönüş değeri yoktur                  örn: x.append("1")
.count(x)                               # Liste içerisin x değerinin sayısını döner.
.index(x)                               # Liste içerisinde x değerinde bir değer varsa onun indexini döner.
.insert(i, x)                           # Liste içerisine belitilen indexe insert eder.
.remove(x)                              # Liste içerisinde x olan değri siler.
.reverse()                              # Liste ögelerini tersine çevirir.

# !----------------> Methods <----------------! # https://docs.python.org/2.7/library/functions.html
open(filename, mode)                    # Bir dosya oluşturur yada açar
raw_input(prompt)                       # String data tipi okur
range(stop)                             # Verilen değer arasında bir list oluşturur.
range(start, stop)                      # Verilen iki değer arasında bir list oluşturur.
range(start, stop, step)                # Verilen iki değer arasında 5 er olarak artırılmş bir list oluşturur.
list()                                  # Liste oluşturur.
min(iterable)                           # Bir liste içerisindeki en küçük sayı değerini döner.
max(iterable)                           # Bir liste içerisindeki en büyük sayı değerini döner.
pow(x, y)                               # x değerinin y kuvvettini döner.
abs(x)                                  # Bir sayının mutlak değerini döner.
sum(iterable)                           # Bir ögenin ögelerinin toplamını döner.
sorted(iterable)                        # Yeni bir sıralanmış liste döner.
str(obj)                                # Verilen değeri string olarak döner.
chr(i)                                  # Berilen sayı değerinin ASCII kod karşılığını dönderir.
exit()                                  # Çıkış
copyright                               # Telif hakkı
dir(obj)                                # Modüller içindeki kullanılan methodların isimlerini döner (Return Type List)

# !----------------> List <----------------!
new_list = [49, 3.14, 'Joke']       # list Tanımlanır
new_list[0] = 50                    # listenin ilk elemenına değer atanır.

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