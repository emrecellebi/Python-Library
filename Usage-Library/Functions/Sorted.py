#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.structure = [-421, -3423, 2365, 0, 23, -4, 90]
        print(sorted(self.structure));
        print(self.sort(self.structure));
    #}
        
    def sort(self, array):
    #{
        array_length = len(array);
        for i in range(array_length):
        #{
            for j in range(i, array_length):
            #{
                if(array[i] > array[j]):
                #{
                    temporary = array[i];
                    array[i] = array[j];
                    array[j] = temporary;
                #}
            #}
        #}
        return array;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}