#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is right!";
        print(self.string.endswith("right!"));
        print(self.string.endswith("!", 8, len(self.string)));
        print(self.ends_with(self.string, "right!"));
    #}
    
    def ends_with(self, string, end):
    #{
        endswith = False;
        
        if(string[-1] == end[-1]):
        #{
            end_lenght = len(end) + 1;
            
            for i in range(1, end_lenght):
            #{
                if(string[-(i)] == end[-(i)]):
                #{
                    endswith = True;
                #}
                else:
                #{
                    endswith = False;
                    break;
                #}
            #}
        #}
        return endswith;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}