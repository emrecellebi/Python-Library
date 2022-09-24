#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        print(abs(-25));
        print(self.absolute(-25));
    #}
        
    def absolute(self, number):
    #{
        if(type(number) == str):
        #{
            number = int(number);
        #}
          
        if(number < 0):
        #{
            number *= -1;
        #}
        return number;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}