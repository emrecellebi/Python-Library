#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    start_color();
    noecho();
    curs_set(False);
    keypad(stdscr, True);
    
    move(3, 3);
    vline("|", 10);
    
    running = True;
    while(running):
    #{
        key = getch();
        obj_player.move(key);
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