#!/usr/bin/env python2

import hashlib;

class Base:
#{
    def __init__(self):
    #{
        md5 = hashlib.md5();
        
        md5.update("hash this");

        print("Type: " + str(type(md5.digest()))); 
        print("Digest: " + md5.digest());

        print("Type: " + str(type(md5.hexdigest()))); 
        print("Hex Digest: " + md5.hexdigest());
        
        md5.update(" and this, too!");

        md5_clone = md5.copy();
        print("Clone: " + md5_clone.hexdigest());
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}
