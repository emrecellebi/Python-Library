#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.array = ["This", "is", "a", "list"];
        
        print(self.array.index("is"));
        print(self.index(self.array, "is", 2));
    #}
    
    def index(self, array, value, start = 0, end = None):
    #{
        if(end == None):
        #{
            end = len(array);
        #}
        
        for i in range(start, end):
        #{
            if(array[i] == value):
            #{
                return i;
            #}
        #}
        
        # Error çıkartmak için kullanılırnır.
        # raise ValueError("'" + value + "' is not in list");
        return -1;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}