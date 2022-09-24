#!/usr/bin/env python

class Base:
#{
    def __init__(self):
    #{
        file_handle = open("file.txt", "w");
        file_handle.write("Hello World!");
        file_handle.close();
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}