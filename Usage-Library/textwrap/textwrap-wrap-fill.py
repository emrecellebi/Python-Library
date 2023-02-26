#!/usr/bin/env python

import textwrap;

def main():
#{
    long_text = "This is a really really long string! T am happy to be making videos again -- I only have a short window of time to do it, but I will when I can. I can record in the library at school and only rerely in my room, but right now, I'm home for the holidays! Merry Christmas everybody, and have a happy New Year!";
    width = 20;
    
    wrapped_lines = textwrap.wrap(long_text, width);
    
    for line in wrapped_lines:
    #{
        print(len(line), line);
    #}
    
    print("\n------------------\n");
    
    print(textwrap.fill(long_text, width));
#}

if(__name__ == "__main__"):
#{
    main();
#}