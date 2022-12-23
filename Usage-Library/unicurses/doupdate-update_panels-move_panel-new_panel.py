#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    start_color();
    noecho();
    curs_set(False);
    keypad(stdscr, True);
    
    window = newwin(3, 20, 4, 4);
    box(window);
    wmove(window, 1, 1);
    waddstr(window, "Hey YouTube!");
    
    panel = new_panel(window);
    
    move_panel(panel, 10, 30);
    
    update_panels();
    doupdate();
    
    running = True;
    while(running):
    #{
        key = getch();
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