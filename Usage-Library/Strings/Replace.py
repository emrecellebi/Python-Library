#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a string!";
        print(self.string.replace("is", "at", 1));
        print(self.replace(self.string, "is", "at", 1));
    #}
    
    def replace(self, working_string, replace, replace_with, count = None):
    #{
        working_string_lenght = len(working_string);
        replace_lenght = len(replace);
        
        new_string = "";
        i = 0;
        
        if(count == None):
        #{
            while(i < working_string_lenght):
            #{
                if(working_string[i:i + replace_lenght] == replace):
                #{
                    new_string += replace_with;
                    i += replace_lenght;
                #}
                else:
                #{
                    new_string += working_string[i];
                    i += 1;
                #}
            #}
        #}
        else:
        #{
            if(type(count) is not int):
            #{
                count = int(count);
            #}
            counter = 0;
            while(i < working_string_lenght):
            #{
                if(counter < count):
                #{
                    if(working_string[i:i + replace_lenght] == replace):
                    #{
                        new_string += replace_with;
                        i += replace_lenght;
                        counter += i;
                    #}
                    else:
                    #{
                        new_string += working_string[i];
                        i += 1;
                    #}
                #}
                else:
                #{
                    new_string += working_string[i];
                    i += 1;
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