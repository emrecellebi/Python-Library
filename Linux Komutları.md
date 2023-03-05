# Linux Komutları

### clear
Terminal ekranını temizlemek için kullanılır.

### history
Terminal geçmişini gösterir. Kullanılan kaç tane komut var ise onları listeler.

### pwd
Terminal ekranında hangi dizin altında olduğunu görmek için kullanılır.

### cd
Dizinler arası geçiş yapmamızı sağlar.
| Args | Açıklama |
| -------- | -------- |
| . | Root dizine gider. (Current Directory) |
| . . | Bir üst dizine gider. (Parent Directory) |
| / | Ana dizine gider. (Root Directory) |
| ~ | Kullanıcı ana dizine gider. |
| - | Dizinler arası ileri geri olarak çalışır |
| -P | Dizindeki oluşturulmuş link gibi bağları çözer |

### ls
Dosyalar hakkında bilgi ala bilmek için kullanılır.
| Args | Açıklama |
| -------- | -------- |
| -a, --all | Tüm dosya ve klasörleri listler.(Gizli) |
| -h, --human-readable | İnsan tarafından okuna bilir dosyaları listele |
| -i, --inode | Her dosyanın dizin numarasını yazar. |
| -l | Uzun formatta bir listeleme yapar.(Ayrıntılı) |
| -m | Klasörler ve dosyalar arasında virgül ile ayır. |
| -r, --reverse | Sırlama sırasında ters sırala. |
| -s, --size | Her dosyanın boyutunu block halinde verir. |
| -t | Son Değiştirilmiş zamana göre sırala önce en yenisi. |
| --help | Yardım dökümanını verir. |
| --version | Verisiyonu verir. |
Ayrıntılı listeleme yaptığımız zaman bazı kısaltmaların olduğunu görürüz.

drwx — — — 35 ubuntu ubuntu 1120 Dec 27 19:54 Desktop
-rwxrw-r — 65 ubuntu ubuntu 1120 Dec 28 18:36 test.txt
lrwxr-x — — 65 ubuntu ubuntu 1120 Dec 28 18:36 file.lnk

| Komut | Açıklama |
| -------- | -------- |
| d | Dizin --> Directory |
| -	| Normal Dosya --> Regular File |
| l	| Sembolic link |
| r	| Okuma izni --> Read Permission |
| w	| Yazma izni --> Write Permisson |
| x	| Çalıştırma izni --> Execute Permisson |

### mkdir
Terminal üzerinde klasör yaratmak için kullanılır.
| Args | Açıklama |
| -------- | -------- |
| -p, --parents | Alt dizinlari oluşturur. |
| -v, --verbose | Oluşturulan her dizin için bir mesaj yazar. |
| --help | Yardım dökümanı verir |
| --version | Versiyonu verir. |

### rmdir
Boş klasörleri silmek için kullanılır. 
| Args | Açıklama |
| -------- | -------- |
| -p, --parents | Alt dizinleri siler. |
| -v, --verbose | Silinen klasör için bilgi verir. |
| --help | Yardım dökümanı verir. |
| --version | Versiyonu verir. |

### cp
Terminal üzerinden dosya kopyalama işlemi yapar.
| Args | Açıklama |
| -------- | -------- |
| -R, -r, --recursive | Recursive olarak kopyalama işlemi yapar. |
| -v, --verbose | Kopyalama yaparken bilgi verir |
| --help | Yardım dökümanı verir. |
| --verison | Versiyonu verir. |

### rm
Dosya ve klasör silmek için kullanılır.
| Args | Açıklama |
| -------- | -------- |
| -f, --forge | Var olmayan dosyaları ve argümanları görmezden gel, asla sorma |
| -r, -R, --recursive | Dizinleri ve dosyları recursive olarak kaldırır. |
| --help | Yardım dökümanı verir |
| --version | Versiyounu verir. |

### cat
Dosya içeriğini terminal ekranına yazar.
| Args | Açıklama |
| -------- | -------- |
| -E, --show-ends | Satır sonlarını işaretliyerek okuma kolaylığı sağlar. |
| -n, --number | Satır numaraları ile yazar. |
| --help | Yardım dökümanını verir. |
| --version | Versiyonu verir |

### tac
Dosya içeriğini terminal ekranına yazmaya sondan başlar.
| Args | Açıklama |
| -------- | -------- |
| --help | Yardım dökümanını verir. |
| --version | Versiyonu verir |

### touch
Dosya oluştura biliriz. 
| Args | Açıklama |
| -------- | -------- |
| --help | Yardım dökümanını verir. |
| --version | Versiyonu verir |

### man
Komutlar hakkında bilgi verir. Her komutun .man file adında dosyası mevcuttur. Bu dosyaları okumamızı sağlar.
| Args | Açıklama |
| -------- | -------- |
| -?, --help | Yardım dökümanını verir. |
| --version | Versiyonu verir |

Klavye Kısayol Tuşları 
| Tuş | Açıklama |
| -------- | -------- |
| Q | Man komutundan çıkış yapar |

### uname
Belirli system bilgilerini verir.
| Args | Açıklama |
| -------- | -------- |
| -a, --all | İşletim systemi hakkında bilgi verir. |
| -s, --kernel-name | İşletim systeminin çekirdek adını verir. |
| -n, --nodename | İşletim systemi bağlantı noktası ve host adını verir. |
| -r, --kernel-release | İşletim systeminin çekirdek sürümünü verir. |
| -v, --kernel-version | İşletim systeminin çekirdek versiyonun verir. |
| -m, --machine | İşletim systeminin makina ve donanım adını verir. |
| -p, --processor | İşletim systeminin çekirdek türünü verir. |
| -i, --hardware-platform | Donanım platformunu verir. |
| -o, --operating-system | İşletim systemini verir. |
| --help | Yardım dökümanını verir. |
| --version | Versiyonu verir |

### mv
Dosya veya dizin taşımak için kullanılır.
| Args | Açıklama |
| -------- | -------- |
| -v, --verbose | Kopyalama yaparken bilgi verir |
| --help | Yardım dökümanı verir. |
| --verison | Versiyonu verir. |
