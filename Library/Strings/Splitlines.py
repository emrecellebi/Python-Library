#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This string\nhas newline\ncharacters\nin it!";
        print(self.string.splitlines(True));
        print(self.split_lines(self.string, True));
    #}
    
    def split_lines(self, string, keeping_characters = False):
    #{
        string_length = len(string);
        newline_denoter = "\n";
        newline_length = len(newline_denoter);
        
        new_string = "";
        array = [];
        
        for i in range(string_length):
        #{
            if(string[i:i + newline_length] == newline_denoter):
            #{
                if(keeping_characters):
                #{
                    new_string += newline_denoter;
                #}
                array += [new_string];
                new_string = "";
            #}
            else:
            #{
                new_string += string[i];
            #}
        #}
        
        array += [new_string];
        return array;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}