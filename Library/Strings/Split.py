#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a joke!";
        
        print(self.string.split(" ", 2));
        print(self.split(self.string, " ", 2));
        
    #}
    
    def split(self, string_to_split, splitter = None, count = None):
    #{
        if(splitter == None):
        #{
            splitter = string.whitespace;
        #}
        
        new_string = string_to_split;
        array = [];
        
        if(count == None):
        #{
            new_string = "";
            if(splitter == string.whitespace):
            #{
                for character in string_to_split:
                #{
                    if(character in splitter):
                    #{
                        array += [new_string];
                        new_string = "";
                    #}
                    else:
                    #{
                        new_string += character;
                    #}
                #}
            #}
            else:
            #{
                string_length = len(string_to_split);
                splitter_length = len(splitter);
                
                i = 0;
                while(i < string_length):
                #{
                    if(string_to_split[i:i + splitter_length] == splitter):
                    #{
                        array += [new_string];
                        new_string = "";
                        i += splitter_length;
                    #}
                    else:
                    #{
                        new_string += string_to_split[i];
                        i += 1;
                    #}
                #}
            #}
        #}
        else:
        #{
            counter = 0;
            while(counter < count):
            #{
                new_string = "";
                
                string_length = len(string_to_split);
                splitter_length = len(splitter);
                
                i = 0;
                while(i < string_length):
                #{
                    if(string_to_split[i:i + splitter_length] == splitter):
                    #{
                        if(counter < count):
                        #{
                            array += [new_string];
                            new_string = "";
                            i += splitter_length;
                            counter += 1;
                        #}
                        else:
                        #{
                            break;
                        #}
                    #}
                    else:
                    #{
                        new_string += string_to_split[i];
                        i += 1;
                    #}
                #}
                for k in range(i, string_length):
                #{
                    new_string += string_to_split[k];
                #}
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