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
.startswith(prefix, 0, 12)              # Dize verilen ek, başlangıç ve bitiş belirtilerek başlıyor ise true yoksa false döner.         örn: x.startswith("Ş", 6, 10)
.endswith(prefix)                       # Dize verilen ek bitiyor ise true yoksa false döner.                                           örn: x.endswith("k")
.endswith(prefix, 0, 12)                # Dize verilen ek, başlangıç ve bitiş belirtilerek bitiyor ise true yoksa false döner.          örn: x.endswith("türk", 0, 13)

