#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    attron(A_REVERSE);
    addstr("Hello World!\n", A_BLINK);
    addstr("Hello World!\n");
    attroff(A_REVERSE);
    addstr("Hello World!");
    getch();
    
    endwin();
    
    return 0;
#}

if(__name__ == "__main__"):
#{
    main();
#}