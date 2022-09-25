#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a joke!";
        print("'" + self.string.rjust(30) + "'");
        print("'" + self.string.rjust(30, '-') + "'");
        print("'" + self.right_justify(self.string, 30) + "'");
        print("'" + self.right_justify(self.string, 30, '-') + "'");
    #}
    
    def right_justify(self, string_to_justify, width, filchar = " "):
    #{
        if(len(filchar) > 1):
        #{
            filchar = filchar[0];
        #}
        
        difference = width - len(string_to_justify);
        
        return filchar * difference + string_to_justify;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}