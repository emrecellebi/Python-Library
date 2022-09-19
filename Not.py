# !----------------> import os <----------------!   # https://docs.python.org/2.7/library/os.path.html
os.path.isdir(path)                     # Verilen yol mevcut ise true olarak dönüşyapar
os.chdir(path)                          # Geçerli çalışma alanını verilen yol ile değiştir. Dönüş değeri yoktur
os.listdir(path)                        # Verilen yol içerisindekileri liste olarak döner.

# !----------------> import subprocess <----------------!   # https://docs.python.org/2.7/library/subprocess.html
subprocess.call(args)                  # Array olarak verilen bir komutları çalıştırır dönüş olarak int değeri döner.

# !----------------> import popen2 <----------------!   # https://docs.python.org/2.7/library/popen2.html Deprecated since version 2.6

# !----------------> File Object <----------------!  # https://docs.python.org/2.7/library/stdtypes.html#file-objects
open(filename, mode)                    # Bir dosya oluşturur yada açar
.write(strData)                         # Dosya içeriğine veri yazar. Dönüş değeri yoktur.
.close()                                # Açık olan dosyayı kapatır. Dönüş değeri yoktur.
.readlines()                            # Dosyayı sonuna kadar satır satır oku ve liste olarak dönüşyapar.
.readlines(sizehint)                    # Dosyayı belritilen size kadar oku ve liste olarak dönüşyapar.

# !----------------> Data Structures <----------------! # https://docs.python.org/2.7/tutorial/datastructures.html
list()                                  # Liste oluşturur.
.append(x)                              # Listenin sonuna bir öge ekler. Dönüş değeri yoktur                  örn: x.append("1")

# !----------------> String Methods <----------------!  # https://docs.python.org/2.7/library/stdtypes.html#string-methods
.startswith(prefix)                     # Dize verilen ek ile başlıyor ise true yoksa false döner.                                      örn: x.startswith("M")
.startswith(prefix, start, end)         # Dize verilen ek, başlangıç ve bitiş belirtilerek başlıyor ise true yoksa false döner.         örn: x.startswith("Ş", 6, 10)
.endswith(prefix)                       # Dize verilen ek bitiyor ise true yoksa false döner.                                           örn: x.endswith("k")
.endswith(prefix, start, end)           # Dize verilen ek, başlangıç ve bitiş belirtilerek bitiyor ise true yoksa false döner.          örn: x.endswith("türk", 0, 13)
.count(sub)                             # Dize içerisinde a karakterini sayar ve döner                                                  örn: x.count("M") 
.count(sub, start, end)                 # Dize içerisinde a karakterini belirtilen başlangıç ve bitiş arasında sayar ve döner           örn: x.count("M", 0, 12) 

# !----------------> Methods <----------------!
input("Please enter something")         # Sadece Interger data tipi okur
raw_input("Please enter something")     # String data tipi okur
str()                                   # Verilen değeri string olarak döner.
range(10)                               # Verilen değer arasında bir list oluşturur.
range(2, 10)                            # Verilen iki değer arasında bir list oluşturur.
range(2, 10, 5)                         # Verilen iki değer arasında 5 er olarak artırılmş bir list oluşturur.
len()                                   # Uzunluk verir


















# !----------------> Inheritance <----------------!
class Mother:
    def __init__(self):
        self.first_name = "Alice"
        self.last_name = "Hawkings"
        self.full_name = self.first_name + " " + self.last_name
    def say_hello(self):
        print(self.full_name + " says hello!")
    def set_first_name(self, name):
        self.first_name = name
class Child(Mother):                    # Kalıtım Multiple Kalıtım ise virgül ile ayırlarak gider örn: class Child(Mother, Mother2):
    def get_married(self, soulmate):
        self.last_name = soulmate.last_name
class Soulmate:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
    def say_hello(self):
        print(self.full_name + " says hello!")

alice = Mother()
alice.say_hello()

bob = Child()
bob.set_first_name("Bob")
bob.say_hello()

allie = Soulmate("Allie", "Deering")
allie.say_hello()

bob.get_married(allie)
bob.say_hello()

# !----------------> Class <----------------!
class Person:
    def set_name(self, name = ''):
        self.name = name
    def say_hello(self):
        print(self.name + " says hello")
andrew = Person()
andrew.set_name("Test");
andrew.say_hello()

class Person2:
    def __init__(self):             # Constructures
        self.name = "Test"
    def __init__(self, name, age):  # Constructures Patameters
        self.name = name
        self.age = age
    def __del__(self):              # Deconstructures
        print(self.name + " has die.")

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
\r          --> # 

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