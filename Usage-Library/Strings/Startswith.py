#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is right!";
        print(self.string.startswith("This"));
        print(self.string.startswith("is", 5, len(self.string)));
        print(self.starts_with(self.string, "This"));
    #}
    
    def starts_with(self, string, start):
    #{
        startswith = False;
        
        if(string[0] == start[0]):
        #{
            start_lenght = len(start);
            
            for i in range(start_lenght):
            #{
                if(string[i] == start[i]):
                #{
                    startswith = True;
                #}
                else:
                #{
                    startswith = False;
                    break;
                #}
            #}
        #}
        return startswith;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}