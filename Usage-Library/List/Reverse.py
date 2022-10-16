#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.array = [1, 2, 3, 4, 5];
        
        # self.array.reverse();
        # print(self.array);
        print(self.reverse(self.array));
    #}
    
    def reverse(self, array):
    #{
        array_length = len(array);
        
        new_array = [];
        for i in range(1, array_length):
        #{
            new_array += [array[-(i)]];
        #}
        
        new_array += [array[0]];
        
        return new_array;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}