#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    addstr("Hello World!");
    getch();
    
    endwin();
    
    return 0;
#}

if(__name__ == "__main__"):
#{
    main();
#}