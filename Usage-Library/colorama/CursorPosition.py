#!/usr/bin/env python

from colorama import *

class Base:
#{
    def __init__(self):
    #{
        init(autoreset=True);
        
        print(Fore.RED + self.pos(30, 10) + "This is red text!");
    #}
    
    def pos(self, x, y):
    #{
        return '\x1b[' + str(y) + ';' + str(x) + 'H';
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}