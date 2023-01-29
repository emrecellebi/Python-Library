# from unicurses import *;
from curses import *;
from curses.panel import *;
from functions import *;

class Player:
#{
    def __init__(self, stdscr, body, foreground = None, background = None, attribute = 0):
    #{
        self.max_x = stdscr.getmaxyx()[1] - 1;
        self.max_y = stdscr.getmaxyx()[0] - 1;
        
        self.x = int(self.max_x / 2);
        self.y = int(self.max_y / 2);
        self.body = body;
        
        del stdscr;
        
        self.window = newwin(1, 1, self.y, self.x);
        # waddstr(self.window, self.body); # unicurses
        self.window.bkgd(self.body);
        self.panel = new_panel(self.window);
        
        self.foreground = foreground;
        self.background = background;
        self.color = 0;
        self.attribute = attribute;
        
        if(foreground != None and background != None):
        #{
            self.set_colors(foreground, background);
        #}
        
        self.show_changes();
        
    #}
    
    def set_colors(self, foreground, background):
    #{
        self.color = make_color(foreground, background);
        
        self.foreground = foreground;
        self.background = background;
        
        # waddstr(self.window, self.body, color_pair(self.color) + self.attribute); # unicurses
        self.window.bkgd(self.body, color_pair(self.color) + self.attribute);
        self.show_changes();
    #}
    
    def move(self, key, motion = 1):
    #{
        moved = False;
        
        if(key == KEY_UP):
        #{
            if not (self.y - motion < 0):
            #{
                moved = True;
                self.y -= motion;
            #}
        #}
        
        if(key == KEY_DOWN):
        #{
            if not (self.y + motion > self.max_y):
            #{
                moved = True;
                self.y += motion;
            #}
        #}
        
        if(key == KEY_LEFT):
        #{
            if not (self.x - motion < 0):
            #{
                moved = True;
                self.x -= motion;
            #}
        #}
        
        if(key == KEY_RIGHT):
        #{
            if not (self.x + motion > self.max_x):
            #{
                moved = True;
                self.x += motion;
            #}
        #}
        
        if(moved):
        #{
            # move_panel(self.panel, self.y, self.x); # unicurses
            self.panel.move(self.y, self.x);
            self.correct_background();
            self.show_changes();
        #}
    #}
    
    def correct_background(self):
    #{
        changing = place_meeting(self);
        if(changing):
        #{
            self.set_colors(self.foreground, changing[1]);
        #}
    #}
    
    def show_changes(self):
    #{
        update_panels();
        doupdate();
    #}
#}