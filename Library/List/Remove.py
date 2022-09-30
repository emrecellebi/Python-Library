#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        self.array = ["This", "is", "a", "list", "is", "that", "right?"];
        
        self.array.remove("is");
        print(self.array);
        print(self.remove(self.array, "is"))
    #}
    
    def remove(self, array, value):
    #{
        new_array = [];
        
        still_removing = True;
        
        for item in array:
        #{
            if not(item == value):
            #{
                new_array += [item];
            #}
            else:
            #{
                if(still_removing):
                #{
                    still_removing = False;
                #}
                else:
                #{
                    new_array += [item];
                #}
            #}
        #}
        return new_array;
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}