# !----------------> import re <----------------!  # https://docs.python.org/2.7/library/re.html
re.S                                               # Özel karakter, yeni satır da dahil olmak üzere herhangi bir karakterle eşleşir
re.DOTALL                                          # Özel karakter, yeni satır da dahil olmak üzere herhangi bir karakterle eşleşir
re.M                                               # Belirtildiğinde, kalıp karakteri '^' dizenin başında ve her satırın başında (her yeni satırın hemen ardından) eşleşir; ve kalıp karakteri '$' dizenin sonunda ve her satırın sonunda (her yeni satırın hemen öncesinde) eşleşir.
re.MULTILINE                                       # Belirtildiğinde, kalıp karakteri '^' dizenin başında ve her satırın başında (her yeni satırın hemen ardından) eşleşir; ve kalıp karakteri '$' dizenin sonunda ve her satırın sonunda (her yeni satırın hemen öncesinde) eşleşir.

re.search(pattern, string): MatchObject            # Verilen Pattern ve String ile bir arama yapar karşılık Match değerini döner. Aksi halde None olarak döner.
re.search(pattern, string, flags): MatchObject     # Verilen Pattern ve String ile bir arama yapar karşılık Match değerini döner. Aksi halde None olarak döner. Flags kullanılır.

re.MatchObject()                                   # 
.start()                                           # Başlangıç indexi
.end()                                             # Bitiş indexi



# !------> Characters <------!
'.'         # Yeni satır dışında her hangi bir karakter ile eşleşir. DOTALL flag belirtilmişse, bu, yeni satır dahil herhangi bir karakterle eşleşir.
'*'         # Tekrarla
'^'         # Dizenin başlangıcıyla eşleşir ve MULTILINE modunda ayrıca her yeni satırdan hemen sonra eşleşir.
'$'         # Dizenin sonuyla veya dizenin sonundaki yeni satırdan hemen önce eşleşir ve MULTILINE modunda ayrıca yeni satırdan önce de eşleşir

