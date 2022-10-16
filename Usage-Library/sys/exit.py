#!/usr/bin/env python

import sys
import string

class Base:
#{
    def __init__(self):
    #{
        print("Hello there!");
        name = input("what is your name?\n");
        
        for digit in string.digits: 
        #{
            if(digit in name): 
            #{
                sys.exit(2);
            #}
        #}
        print("Oh, it's good to meet you, " + name + "!");
        sys.exit(0);
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}