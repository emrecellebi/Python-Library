#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    max_y, max_x = getmaxyx(stdscr);
    move(int(max_y / 2), int(max_x / 2));
    
    addstr("@");
    getch();
    
    endwin();
    
    return 0;
#}

if(__name__ == "__main__"):
#{
    main();
#}