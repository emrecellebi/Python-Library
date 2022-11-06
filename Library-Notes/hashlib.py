# !----------------> import hashlib <----------------! https://docs.python.org/2.7/library/hashlib.html
hashlib.algorithms                              # Bu modül içindeki algoritmaların listesini verir. (Return Type Tuple)
hashlib.md5()                                   # MD5 Algoritması modülü (Return Type Object)

# !----------------> hashlib.md5() sha1() sha255() <----------------!
md5.block_size                                  # MD5 Algoritmasının byte cinsinden dahili block boyutu (Return Type long)
md5.digets_size                                 # Elde edilen MD5 Algoritmasının byte cinsinden boyutu (Return Type long)
md5.name                                        # Algoritmanın adını döner (Return Type str)
md5.update(args)                                # Verilen değeri MD5 algoritmasına günceller. Ardı ardına çağrılır ise ekleme yaparak günceller
md5.digest()                                    # Update ile güncellenen veriyi ASCII olmayan karakterler ile geri döner (Return Type str)
md5.hexdigest()                                 # Update ile güncellenen veriyi Hexadecimal olarak geri döner (Return Type str)
md5.copy()                                      # Hash nesnesinin bir kopyasını döner (Return Type object)

