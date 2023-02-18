# !----------------> import threading <----------------!  # https://docs.python.org/2.7/library/threading.html
threading.active_count()                  # Canlı olan Thread sayısını döner.
threading.current_thread()                # Calışan Threadi döner.
threading.enumerate()                     # Calı olan tüm Tread nesnelerinin listesini döner.

threading.Tread()                         # Thread class
.ident                                    # Thread başlatıldığında her bir parça için bir kimlik üretilir.
.start()                                  # Threadi başlatır.
.is_alive()                               # Thread in ayakta olup olmadığını döner.
.join()                                   # Thread işlemi bitene kadar bekle
.isDaemon()                               # Bir arka plan programı olup olmadığını kontrol eder.
.setDaemon()                              # 

threading.Lock()                          # 
.acquire()                                # Kilit engellme 
.release()                                # Kilidi serbest bırak

