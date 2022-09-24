#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        file_handle = open("file.txt", "r");
        lines = file_handle.readlines();
        for line in lines:
        #{
            print(line);
        #}
        file_handle.close();
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}