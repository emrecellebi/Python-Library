#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.array = ["This", "is", "a", "list"];
        print(self.array.count("is"));
        print(self.count(self.array, "is"));
    #}
    
    def count(self, array, value):
    #{
        counter = 0;
        for item in array:
        #{
            if(item == value):
            #{
                counter += 1;
            #}
        #}
        return counter;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}