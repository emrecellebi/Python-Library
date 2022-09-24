#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        print(pow(2, 4));
        print(self.power(2, 4));
    #}
    
    def power(self, base, power):
    #{
        if(power == 0):
        #{
            return 1;
        #}
        product = base;
        for i in range(1, power):
        #{
            product *= base;
        #}
        return product;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}