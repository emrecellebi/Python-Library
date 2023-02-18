#!/usr/bin/env python

import re;

from colorama import Fore as foreground
from colorama import Back as background

def main():
#{
    pattern = r"this";
    string = "This is a joke, right?";
    
    matched = re.search(pattern, string);
    
    if(matched):
    #{
        start = matched.start();
        end = matched.end();
        print(string[:start] + background.BLUE + string[start:end] + background.RESET + string[end:]);
    #}
    else:
    #{
        print(foreground.RED + "There was no match found!" + foreground.RESET);
    #}
#}

if(__name__ == "__main__"):
#{
    main();
#}