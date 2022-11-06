#!/usr/bin/env python2

import hashlib;

class Base:
#{
    def __init__(self):
    #{
        print("Type: " + str(type(hashlib.algorithms)));
        print("Algorithms: " + str(hashlib.algorithms));
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}
