#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = " \t  \n ";
        print(self.string.isspace());
        print(self.is_space(self.string));
    #}
    
    def is_space(self, string_to_look_through):
    #{
        for character in string_to_look_through:
        #{
            if(character not in string.whitespace):
            #{
                return False;
            #}
        #}
        return True;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}