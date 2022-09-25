#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a new string! \t\t  \n";
        print(self.string.rstrip("\t\t \n"));
        print(self.right_strip(self.string, "\t\t \n"));
    #}
    
    def right_strip(self, string_to_look_through, characters = None):
    #{
        if(characters == None):
        #{
            characters = string.whitespace;
        #}
        
        new_string = "";
        string_lenght = len(string_to_look_through);
        
        for i in range(1, string_lenght):
        #{
            if not(string_to_look_through[-i] in characters):
            #{
                break;
            #}
        #}
        
        for x in range(i, string_lenght):
        #{
            new_string = string_to_look_through[-x] + new_string;
        #}
        
        new_string = string_to_look_through[0] + new_string;
        return new_string;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}