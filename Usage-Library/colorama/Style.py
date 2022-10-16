#!/usr/bin/env python

from colorama import *

class Base:
#{
    def __init__(self):
    #{
        init()
        
        print(Style.NORMAL + Back.WHITE + Fore.RED + "This is colored text!")
        print(Style.DIM + Back.WHITE + Fore.RED + "This is colored text!")
        print(Style.BRIGHT + Back.WHITE + Fore.RED + "This is colored text!")
        print(Style.RESET_ALL + Back.RESET + Fore.RESET + "This is colored text!")
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}