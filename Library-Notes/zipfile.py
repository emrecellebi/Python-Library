# !----------------> import zipfile <----------------!  # https://docs.python.org/2.7/library/zipfile.html
# -------> ZipFile class <-------
ZipFile(str): object                   # Zip açar.
ZipFile(str, "w"): object              # Zip oluşurur
.close()                               # Açılan zip dosyasını kapatır.
.write(str)                            # Zip içeriğine aklar w modunda
.infolist():list                       # Zip içeriği hakkında bilgi verir.
.namelist():list                       # Zip içeriğindeki dosya isimlerini verir.
.extract(str)                          # Zip içerisinden verilen dosya ismini bulunduğu yere çıkartır.
.extract(str, str)                     # verilen dosya ismini verilen klasör altına çıkart.
.extractall()                          # Tümünü çıkart
.is_zipfile(str)                       # Zip dosyası olup olmadığını kontrol eder
.setpassword(str)                      # Şifreli zipler için sifre tanımlaması yapılır.

.getinfo(str):object                   # Verilen dosya isminin bilgilerini verir.
.filename                              # Verilen dosyanın adını döner.
.datetime                              # Verilen dosyanın tarihini döner.


