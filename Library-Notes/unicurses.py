# !----------------> import urllib <----------------!
initscr()                       # Ekranı başlat
endwin()                        # Ekranı bitir.
getch()                         # Kullanıcıdan input alır.
addstr(str)                     # Console yazı yazar.
move(y, x)                      # Yazıyı konumlandırmayı sağlar.
mvaddstr(y, x, str)             # Yazıyı konumlandırmayı sağlar.
getmaxyx(stdscr)                # Console peceresinib boyutlarını döner.
attron(object)                  # Yazı sttilini aktif et
attroff(object)                 # Yazı sttilini pasif et
start_color()                   # Renk sistemini başlatır.
init_pair(int, object, object)  # Özel renk tenımlama yapar.
color_pair(int)                 # Tanımlan id ile tanımlı olan rengi kullanır.
use_default_colors()            # Tanımlınan rengi default olarak kullnıcak ise bu çağrılır.
noecho()                        # Program çalışırken yazmayı kapatır.
curs_set(bool)                  # Cursor kapatıp açar.
keypad(stdscr, bool)            # 
newwin(int, int, int, int)      # Yeni bir ekran oluşturur.
waddstr(scr, str)               # Yeni oluşan ekranda yazılıcak yazı
wgetch(scr)                     # Yeni oluşan ekran için Kullanıcıdan input alır.
wmove(scr)                      # Yeni oluşan pencere için taşıma sağlar.
box(scr)                        # Pencerini etrafını belirtir.
new_panel(scr)                  # Panel oluşturur
move_panel(panel, int, int)     # Paneli taşır.
update_panels()                 # Tüm panelleri Günceller
doupdate()                      # 
bottom_panel(panel)             # Paneli aşağıya hizalar.
wbkgd(scr, str)                 # Verilen pencere içerisini doldurur.
has_colors()                    # 

