#!/usr/bin/env python

from colorama import *

class Base:
#{
    def __init__(self):
    #{
        init()
        
        print(Back.RED + "This is colored text!")
        print(Back.GREEN + "This is colored text!")
        print(Back.BLUE + "This is colored text!")
        print(Back.MAGENTA + "This is colored text!")
        print(Back.CYAN + "This is colored text!")
        print(Back.WHITE + "This is colored text!")
        print(Back.RESET + "This is colored text!")
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}