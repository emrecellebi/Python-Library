# !----------------> import subprocess <----------------!   # https://docs.python.org/2.7/library/subprocess.html
subprocess.call(args)                  # Array olarak verilen bir komutları çalıştırır dönüş olarak int değeri döner.
subprocess.check_output(args)          # Array olarak verilen bir komutları çalıştırır dönüş olarak string değeri döner.

# !----------------> subprocess.Popen <----------------!
subprocess.Popen(args)                 # Bir Alt proses oluşutur ve yürütülür.
Popen.poll()                           # Alt sürecin sonlandırılıp sonlandırılmadığını kontrol edin.
Popen.kill()                           # Öldür.
Popen.terminate()                      # Stop.
Popen.wait()                           # Beklet
Popen.pid                              # İşlem Idsi
Popen.returncode                       # Dönüş kodunu verir