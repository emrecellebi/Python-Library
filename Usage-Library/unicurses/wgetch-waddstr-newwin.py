#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    start_color();
    noecho();
    curs_set(False);
    keypad(stdscr, True);
    
    window = newwin(10, 25, 3, 0);
    waddstr(window, "Hello World!");
    
    running = True;
    while(running):
    #{
        key = wgetch(window);
        if(key == 27):
        #{
            running = False;
            break;
        #}
    #}
    
    endwin();
    
    return 0;
#}

if(__name__ == "__main__"):
#{
    main();
#}