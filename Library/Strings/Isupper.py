#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "THIS IS A STRING!";
        print(self.string.isupper());
        print(self.is_upper(self.string));
    #}
    
    def is_upper(self, string_to_look_in):
    #{
        for character in string_to_look_in:
        #{
            if(character in string.ascii_letters):
            #{
                if(character not in string.ascii_uppercase):
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