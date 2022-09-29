#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.array = ["This", "joke!"];
        
        print(str(self.array));
        
        self.array.insert(1, "is");
        print(str(self.array));
        
        print(self.insert(self.array, 1, "is"));
    #}
    
    def insert(self, array, position, value):
    #{
        array = array[:position] + [value] + array[position:];
        return array;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}