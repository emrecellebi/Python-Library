#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    start_color();
    noecho();
    curs_set(False);
    keypad(stdscr, True);
    
    init_pair(1, COLOR_YELLOW, COLOR_GREEN);
    init_pair(2, COLOR_RED, COLOR_GREEN);
    
    dude = newwin(1, 1, 10, 30);
    waddstr(dude, "@", color_pair(2));
    dude_panel = new_panel(dude);
    
    grass = newwin(10, 50, 5, 5);
    
    wbkgd(grass, ".", color_pair(1));
    grass_panel = new_panel(grass);
    bottom_panel(grass_panel);
    
    
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