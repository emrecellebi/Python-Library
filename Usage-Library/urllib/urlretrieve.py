#!/usr/bin/env python

from urllib import *;

class Base:
#{
    def __init__(self):
    #{
        print(urlretrieve("https://docs.python.org/2.7/library/urllib.html", "01.html"));
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}