#!/usr/bin/env python

from urllib import *;

class Base:
#{
    def __init__(self):
    #{
        page = urlopen("https://docs.python.org/2.7/library/urllib.html");
        print("Read: " + page.read());
        print("Get Code: " + str(page.getcode()));
        print("Get Url: " + page.geturl());
        print("Url: " + page.url);
        page.close();
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}