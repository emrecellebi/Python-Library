#!/usr/bin/env python

from unicurses import *;

def main():
#{
    stdscr = initscr();
    
    running = True;
    while(running):
    #{
        key = getch();
        if(key == 27):
        #{
            running = False;
            break;
        #}
        elif(key == ord('a')):
        #{
            move(2, 0);
            addstr("You pressed the A key!");
            continue;
        #}
        move(10, 0);
        addstr("Keycode was " + str(key) + " and the key was " + chr(key) + "  ");
        move(0, 0);
    #}
    
    endwin();
    
    return 0;
#}

if(__name__ == "__main__"):
#{
    main();
#}