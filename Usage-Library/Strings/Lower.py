#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a joke!";
        print(self.string.lower());
        print(self.to_lower(self.string));
    #}
    
    def to_lower(self, string_to_change):
    #{
        uppercase_lenght = len(string.ascii_uppercase);
        new_string = "";
        
        for character in string_to_change:
        #{
            if(character in string.ascii_uppercase):
            #{
                for i in range(uppercase_lenght):
                #{
                    if(character == string.ascii_uppercase[i]):
                    #{
                        new_string += string.ascii_lowercase[i];
                    #}
                #}
            #}
            else:
            #{
                new_string += character;
            #}
        #}
        return new_string;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}