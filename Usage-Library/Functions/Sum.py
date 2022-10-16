#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        print(self.get_sum(["3", 4, 3, "10", 20, 10]));
        print(sum([3, 4, 3, 10, 20, 10]));
    #}
        
    def get_sum(self, array):
    #{
        sum_number = 0;
        for item in array:
        #{
            if(type(item) is str):
            #{
                item = int(item);
            #}
            sum_number += item;
        #}
        return sum_number;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}