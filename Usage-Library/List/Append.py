#!/usr/bin/env python

import string;

class Base:
#{
    def __init__(self):
    #{
        self.array = ["This", "is", "a", "list"];
        print(str(self.array));
        
        self.array.append("right?");
        print(str(self.array));
        
        self.append(self.array, "right?");
        print(str(self.array));
    #}
    
    def append(self, array, append_this):
    #{
        array += [append_this];
        return array;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}