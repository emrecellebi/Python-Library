#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        print(self.get_lenght(3, "This", "is", "a", "Cars"));
    #}
    
    def get_lenght(self, *items):
    #{
        all_lenghts = [];
        for item in items:
        #{
            if(type(item) is int):
            #{
                item = str(item);
            #}
            
            lenght = 0;
            for character in item:
            #{
                lenght += 1;
            #}
            
            all_lenghts += [lenght];
        #}    
        return all_lenghts;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}