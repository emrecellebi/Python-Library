#!/usr/bin/env python2

import pickle;
from urllib import *;
from string import *;

def main():
#{
    pick = pickle.load(open("banner.p"));
    
    for item in pick:
    #{
        for thing in item:
        #{
            print thing[0] * thing[1],
        #}
        print ""
    #}
#}

if(__name__ == "__main__"):
#{
    main();
#}