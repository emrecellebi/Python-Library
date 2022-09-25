#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a string! It is, isn't it?";
        
        print(self.string.rfind("is", 2, 20));
        print(self.right_find(self.string, "is", 2, 20));
    #}
    
    def right_find(self, string, substring, start = 0, end = None):
    #{
        if(end == None):
        #{
            end = len(string);
        #}
        
        substring_lenght = len(substring);
        positon = -1;
        
        for i in range(start, end):
        #{
            if(string[i:i + substring_lenght] == substring):
            #{
                positon = i;
            #}
        #}
        return positon;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}