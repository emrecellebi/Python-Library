#!/usr/bin/env python

class Base:
#{
    def __init__(self, name, *numbers):
    #{
        self.numbers = numbers;
    #}
       
    def print_out(self):
    #{
        print(str(self.numbers) + "\n");
        for everything in self.numbers:
        #{
            print(everything);
        #}
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base("Tuple", 1, 2, 3, 4, 5);
    root.print_out();
#}