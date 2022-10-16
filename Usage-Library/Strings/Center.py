#!/usr/bin/env python

import math;

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a string!";
        print("'" + self.string.center(40) + "'");
        print("'" + self.string.center(40, '-') + "'");
        print("'" + self.center(self.string, 40) + "'");
    #}
    
    def center(self, string, width):
    #{
        string_lenght = len(string);
        ground__cover = width - string_lenght;
        sides = int(math.floor(ground__cover / 2));
        return sides * " " + string + " " * sides;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}