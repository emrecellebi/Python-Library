#!/usr/bin/env python

from subprocess import *;

class Base:
#{
    def __init__(self):
    #{
        print(call("ls"));
        print(call(["ls", "-l"]));
        print(call("exit 2", shell=True));
        print(call(["ls", "-l"], stdout=open("thing.txt", "w")));
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}