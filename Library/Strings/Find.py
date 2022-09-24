#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a string! It is, right?";
        print(self.string.find("is"));
        print(self.string.find("is", 4, len(self.string)));
        print(self.find(self.string, "is"));
        print(self.find(self.string, "is", 4, len(self.string)));
    #}
    
    def find(self, string, look_for, start = 0, end = None):
    #{
        if(end == None):
        #{
            end = len(string);
        #}
        
        look_for_lenght = len(look_for);
        for i in range(start, end):
        #{
            if(string[i] == look_for[0]):
            #{
                if(string[i:i + look_for_lenght] == look_for):
                #{
                    return i;
                #}
            #}
        #}
        return -1;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}