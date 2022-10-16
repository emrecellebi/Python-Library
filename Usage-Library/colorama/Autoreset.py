#!/usr/bin/env python

from colorama import *

class Base:
#{
    def __init__(self):
    #{
        init(autoreset=True);
        
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "This is red text!");
        print("Don't tou think that's cool?");
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}