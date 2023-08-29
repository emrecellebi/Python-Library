#!/usr/bin/env python2

import morsecode;

def main():
#{
    data = '&& &&& !&! !!! ! !&& !& !!! &!&! &&& &&& !&!!';
    print(data.replace("!", ".").replace("&", "-"));
    data = data.replace("!", ".").replace("&", "-");
    
    print(morsecode.decodeMorse(data));
#}

if(__name__ == "__main__"):
#{
    main();
#}