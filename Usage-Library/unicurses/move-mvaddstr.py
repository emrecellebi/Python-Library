#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    # move(5, 30);
    mvaddstr(5, 30, "Hello World!");
    getch();
    
    endwin();
    
    return 0;
#}

if(__name__ == "__main__"):
#{
    main();
#}