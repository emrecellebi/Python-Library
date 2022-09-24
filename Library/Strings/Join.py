#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "...";
        print(self.string.join("What are you doing?"));
        print(self.join("What are you doing?", self.string));
    #}
    
    def join(self, string_to_iterate_through, string_to_put_in):
    #{
        new_string = "";
        for charackter in string_to_iterate_through:
        #{
            if(charackter == string_to_iterate_through[-1]):
            #{
                new_string += charackter;
            #}
            else:
            #{
                new_string += charackter + string_to_put_in;
            #}
        #}
        return new_string;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}