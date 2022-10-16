#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.string = "This is a string? Isn't it? It is, right?";
        print(self.string.count("is"));
        print(self.string.count("is", 10, len(self.string)));
        print(self.count(self.string, "is"));
    #}
    
    def count(self, haystack, needle):
    #{
        haystack_lenght = len(haystack);
        needle_lenght = len(needle);
        
        total = 0;
        for i in range(haystack_lenght):
        #{
            if(haystack[i] == needle[0]):
            #{
                end = i + needle_lenght;
                if(haystack[i:end] == needle):
                #{
                    total += 1;
                #}
            #}
        #}
        return total;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}