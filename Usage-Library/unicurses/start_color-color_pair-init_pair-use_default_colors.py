#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    start_color();
    # use_default_colors();
    init_pair(1, COLOR_RED, COLOR_WHITE);
    
    addstr("Hello World!", color_pair(1) + A_BLINK);
    getch();
    
    endwin();
    
    return 0;
#}

if(__name__ == "__main__"):
#{
    main();
#}