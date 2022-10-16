#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "string";
        print(self.string.isalpha());
        print(self.is_alphabetical(self.string));
    #}
    
    def is_alphabetical(self, string_to_look_through):
    #{
        for character in string_to_look_through:
        #{
            if not(character in string.ascii_letters):
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