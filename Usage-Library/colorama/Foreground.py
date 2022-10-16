#!/usr/bin/env python

from colorama import *

class Base:
#{
    def __init__(self):
    #{
        init()
        
        print(Fore.RED + "This is colored text!")
        print(Fore.GREEN + "This is colored text!")
        print(Fore.BLUE + "This is colored text!")
        print(Fore.MAGENTA + "This is colored text!")
        print(Fore.CYAN + "This is colored text!")
        print(Fore.WHITE + "This is colored text!")
        print(Fore.RESET + "This is colored text!")
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}