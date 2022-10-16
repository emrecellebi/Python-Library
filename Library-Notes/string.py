# !----------------> import string <----------------!  # https://docs.python.org/2.7/library/stdtypes.html#string-methods
.digits                                 # Tüm rakamları verir.

# !----------------> String Methods <----------------!
.ascii_letters                          # Alfabetik olan büyük küçük karakterlerin tanımı.
.ascii_lowercase                        # Alfabetik olan küçük karakterlerin tanımı.
.ascii_uppercase                        # Alfabetik olan büyük karakterlerin tanımı.
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