#!/usr/bin/env python

import re;

from colorama import Fore as foreground
from colorama import Back as background

def main():
#{
    pattern = r"^.";
    string = "This is a joke, right?\n\nBackslash";
    flags_in_use = re.MULTILINE;
    
    found_matches = re.findall(pattern, string, flags_in_use);
    print("The Python re module Testing Environment found " + foreground.YELLOW + str(len(found_matches)) + foreground.RESET + " matches." + "\nThey are: " + foreground.MAGENTA)
    print(found_matches);
    print(foreground.RESET + "The match hilight looks like: ");
    
    
    matched = re.search(pattern, string, flags_in_use);
    
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