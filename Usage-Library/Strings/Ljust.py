#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a joke!";
        print("'" + self.string.ljust(30) + "'");
        print("'" + self.string.ljust(30, '-') + "'");
        print("'" + self.left_justify(self.string, 30) + "'");
        print("'" + self.left_justify(self.string, 30, '-') + "'");
    #}
    
    def left_justify(self, string_to_justify, width, filchar = " "):
    #{
        if(len(filchar) > 1):
        #{
            filchar = filchar[0];
        #}
        
        difference = width - len(string_to_justify);
        
        return string_to_justify + filchar * difference;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}