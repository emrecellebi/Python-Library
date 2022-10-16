#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a joke!";
        print(self.string.zfill(20));
        print(self.zfill(self.string, 20));
    #}
    
    def zfill(self, string, width):
    #{
        return "0" * (width - len(string)) + string;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}