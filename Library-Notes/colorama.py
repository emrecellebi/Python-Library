# !----------------> import colorama <----------------! https://pypi.org/project/colorama/
colorama.init()                  # System yapılandırılır.
colorama.init(autoreset)         # System yapılandırılır. autoreset True yada False ise otomatik resetlenir.
colorama.init(convert)           # System yapılandırılır. convert True yada False ANSI kolarının Win32 cağrılarını geçersiz kılar.
colorama.init(wrap)              # System yapılandırılır. wrap True yada False

colorama.Fore.BLACK              # Foregorund Siyah
colorama.Fore.RED                # Foregorund Kırmızı
colorama.Fore.GREEN              # Foregorund Yeşil
colorama.Fore.BLUE               # Foregorund Mavi
colorama.Fore.MAGENTA            # Foregorund Magenta
colorama.Fore.CYAN               # Foregorund Cyan
colorama.Fore.WHITE              # Foregorund Beyaz
colorama.Fore.RESET              # Foregorund Reset

colorama.Back.BLACK              # Backgorund Siyah
colorama.Back.RED                # Backgorund Kırmızı
colorama.Back.GREEN              # Backgorund Yeşil
colorama.Back.BLUE               # Backgorund Mavi
colorama.Back.MAGENTA            # Backgorund Magenta
colorama.Back.CYAN               # Backgorund Cyan
colorama.Back.WHITE              # Backgorund Beyaz
colorama.Back.RESET              # Backgorund Reset

colorama.Style.NORMAL            # 
colorama.Style.DIM               # 
colorama.Style.BRIGHT            # 
colorama.Style.RESET_ALL         # 