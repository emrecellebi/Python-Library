#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "rzsw\t\t  This is a new string!";
        print(self.string.lstrip("rzsw\t\t "));
        print(self.left_strip(self.string, "rzsw\t\t "));
    #}
    
    def left_strip(self, string_to_look_through, characters = None):
    #{
        if(characters == None):
        #{
            characters = string.whitespace;
        #}
        
        new_string = "";
        string_lenght = len(string_to_look_through);
        
        for i in range(string_lenght):
        #{
            if( string_to_look_through[i] in characters):
            #{
                new_string += "";
            #}
            else:
            #{
                break;
            #}
        #}
        
        for x in range(i, string_lenght):
        #{
            new_string += string_to_look_through[x];
        #}
        
        return new_string;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}