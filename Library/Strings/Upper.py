#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a joke!";
        print(self.string.upper());
        print(self.to_upper(self.string));
    #}
    
    def to_upper(self, string_to_work_with):
    #{
        alphabet_length = len(string.ascii_lowercase);
        new_string = "";
        
        for character in string_to_work_with:
        #{
            if(character in string.ascii_lowercase):
            #{
                for i in range(alphabet_length):
                #{
                    if(string.ascii_lowercase[i] == character):
                    #{
                        new_string += string.ascii_uppercase[i];
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