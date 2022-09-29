#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "ThIS sTRinG haS RAndOM caSES!";
        print(self.string.swapcase());
        print(self.swap_case(self.string));
    #}
    
    def swap_case(self, string_to_swap):
    #{
        new_string = "";
        alphabet_length = len(string.ascii_lowercase);
        
        for character in string_to_swap:
        #{
            if(character in string.ascii_lowercase):
            #{
                for i in range(alphabet_length):
                #{
                    if(string.ascii_lowercase[i] == character):
                    #{
                        new_string += string.ascii_uppercase[i];
                        break;
                    #}
                #}
            #}
            else:
            #{
                if(character in string.ascii_uppercase):
                #{
                    for i in range(alphabet_length):
                    #{
                        if(string.ascii_uppercase[i] == character):
                        #{
                            new_string += string.ascii_lowercase[i];
                            break;
                        #}
                    #}
                #}
                else:
                #{
                    new_string += character;
                #}
            #}
        #}
        return new_string;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}