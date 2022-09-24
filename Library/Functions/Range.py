#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        print(self.range_of(10, 20, 3));
        print(list(range(10, 20, 3)));
    #}
    
    def range_of(self, start, stop = 0, step = 1):
    #{
        returned_list = [];
        if(stop == 0):
        #{
            stop = start;
            start = 0;
        #}
        while(start < stop):
        #{
            returned_list += [start];
            start += step;
        #}
        return returned_list;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}