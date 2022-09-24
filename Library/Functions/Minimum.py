#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.numbers = [2, 100, -3, 429, 0];
        self.list_of_numbers = [200, 3000, 76373, 9, 543];
        print(min(self.numbers));
        print(self.get_minimum(self.list_of_numbers));
    #}
    
    def get_minimum(self, array):
    #{
        for element in array:
        #{
            if(element == array[0]):
            #{
                minimum = element;
            #}
            else:
            #{
                if(element < minimum):
                #{
                    minimum = element;
                #}
            #}
        #}
        return minimum;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}