#!/usr/bin/env python

import re;

from colorama import Fore as foreground
from colorama import Back as background

def main():
#{
    pattern = r".";
    string = "This is a joke, right?\n\nBackslash";
    flags_in_use = re.MULTILINE;
    
    found_matches = re.findall(pattern, string, flags_in_use);
    print("The Python re module Testing Environment found " + foreground.YELLOW + str(len(found_matches)) + foreground.RESET + " matches." + "\nThey are: " + foreground.MAGENTA)
    print(found_matches);
    print(foreground.RESET + "The match hilight looks like: ");
    
    regex = re.compile(pattern, flags_in_use);
    
    matched = regex.search(string);
    start = end = beginning = 0;
    
    hilight = "";
    
    while(matched):
    #{
        start = matched.start();
        end = matched.end();
        hilight += string[beginning:start] + background.BLUE + string[start:end] + background.RESET;
        matched = regex.search(string, end + 1);
        beginning = end;
        
        if not (matched):
        #{
            hilight += string[end:];
        #}
        
        if(end >= len(string)): break;
    #}
    if hilight == "": hilight = string;
    print(hilight);
#}

if(__name__ == "__main__"):
#{
    main();
#}