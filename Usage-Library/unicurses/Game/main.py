#!/usr/bin/env python

# from unicurses import *;
from curses import *;
from functions import *;
from player import *;
from room import *;

def main():
#{
    global instances;

    stdscr = initscr();
    
    start_color();
    noecho();
    curs_set(False);
    # keypad(stdscr, True); # unicurses
    stdscr.keypad(True);
    
    stdscr_h, stdscr_w = stdscr.getmaxyx();
    world = Room(0, 0, stdscr_w, stdscr_h, " ", COLOR_BLACK, COLOR_BLACK);
    obj_room = Room(2, 3, 30, 10, "~", COLOR_BLACK, COLOR_BLUE, A_BOLD);
    obj_room_two = Room(8, 10, 50, 10, "~", COLOR_YELLOW, COLOR_MAGENTA, A_BOLD);
    obj_player = Player(stdscr, "@", COLOR_RED, COLOR_YELLOW, A_BOLD);
    obj_player.correct_background();
    
    instances += [obj_player, world, obj_room, obj_room_two];
    
    running = True;
    while(running):
    #{
        # key = getch(); # unicurses
        key = stdscr.getch();
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