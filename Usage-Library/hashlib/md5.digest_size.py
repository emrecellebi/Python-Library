#!/usr/bin/env python2

import hashlib;

class Base:
#{
    def __init__(self):
    #{
        md5 = hashlib.md5();

        print("Type: " + str(type(md5.digest_size)));
        print("Digest Size: " + str(md5.digest_size));
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}
