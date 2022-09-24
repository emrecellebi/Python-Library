#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "12235488991";
        print(self.string.isdigit());
        print(self.is_full_of_digits(self.string));
    #}
    
    def is_full_of_digits(self, string_to_look_through):
    #{
        for character in string_to_look_through:
        #{
            if not(character in string.digits):
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