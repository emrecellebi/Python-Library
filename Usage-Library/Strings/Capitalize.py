#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "strigns are the coolest things ever.";
        print(self.string.capitalize());
        print(self.capitalize(self.string));
    #}
    
    def capitalize(self, string):
    #{
        lowercase = [];
        start_lowercase = 97;
        end_lowercase = 123;
        for i in range(start_lowercase, end_lowercase):
        #{
            lowercase += [chr(i)];
        #}
        
        uppercase = [];
        start_uppercase = 65;
        end_uppercase = 91;
        for i in range(start_uppercase, end_uppercase):
        #{
            uppercase += [chr(i)];
        #}
        
        if(string[0] in lowercase):
        #{
            size_of_lowercase = len(lowercase);
            for i in range(size_of_lowercase):
            #{
                if(lowercase[i] == string[0]):
                #{
                    string = uppercase[i] + string[1:];
                #}
            #}
        #}
        return string;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}