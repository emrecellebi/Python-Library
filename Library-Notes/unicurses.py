# !----------------> import urllib <----------------!
initscr()                       # Ekranı başlat
endwin()                        # Ekranı bitir.
getch()                         # Kullanıcıdan input alır.
addstr(string)                  # Console yazı yazar.
move(y, x)                      # Yazıyı konumlandırmayı sağlar.
mvaddstr(y, x, string)          # Yazıyı konumlandırmayı sağlar.
getmaxyx(stdscr)                # Console peceresinib boyutlarını döner.
attron(object)                  # Yazı sttilini aktif et
attroff(object)                 # Yazı sttilini pasif et
start_color()                   # Renk sistemini başlatır.
init_pair(int, object, object)  # Özel renk tenımlama yapar.
color_pair(int)                 # Tanımlan id ile tanımlı olan rengi kullanır.
use_default_colors()            # Tanımlınan rengi default olarak kullnıcak ise bu çağrılır.


