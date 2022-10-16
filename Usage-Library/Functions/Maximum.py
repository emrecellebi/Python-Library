#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.numbers = [2, 100, -3, 429, 0];
        self.list_of_numbers = [200, 3000, 76373, 9, 543];
        print(max(self.numbers));
        print(self.get_maximum(self.list_of_numbers));
    #}
    
    def get_maximum(self, array):
    #{
        for item in array:
        #{
            if(item == array[0]):
            #{
                maximum = item;
            #}
            else:
            #{
                if(item > maximum):
                #{
                    maximum = item;
                #}
            #}
        #}
        return maximum;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}