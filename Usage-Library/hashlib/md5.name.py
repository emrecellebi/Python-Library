#!/usr/bin/env python2

import hashlib;

class Base:
#{
    def __init__(self):
    #{
        md5 = hashlib.md5();

        print("Type: " + str(type(md5.name)));
        print("Name: " + md5.name);
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}
