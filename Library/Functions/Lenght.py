#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "Melek Şentürk";
        print(len(self.string));
        print(self.get_lenght(self.string));
    #}
    
    def get_lenght(self, data):
    #{
        if(type(data) is int):
        #{
            data = str(data);
        #}
        
        lenght = 0;
        for i in data:
        #{
            lenght += 1;
        #}
        
        return lenght;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}