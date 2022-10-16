#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "this is a string!";
        print(self.string.islower());
        print(self.is_lower(self.string));
    #}
    
    def is_lower(self, string_to_look_in):
    #{
        for character in string_to_look_in:
        #{
            if(character in string.ascii_letters):
            #{
                if(character not in string.ascii_lowercase):
                #{
                    return False;
                #}
            #}
        #}
        return True;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}