#!/usr/bin/env python2

import hashlib;

class Base:
#{
    def __init__(self):
    #{
        md5 = hashlib.md5();

        print("Block Size: " + str(md5.block_size));
        print("Type: " + str(type(md5.block_size)));
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}
