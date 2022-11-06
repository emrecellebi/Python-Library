#!/usr/bin/env python

import glob;

class Base:
#{
    def __init__(self):
    #{
        # filename = "*";           # Hepsini listeler.
        # filename = "s*";          # s ile başlayanları listeler.
        # filename = "[1-9].jpg";   # 1 ile 9 arasınfakileri listeler
        filename = "[a-z]*.py";     # a ile z arasınfakileri listeler * tümünü getir.
        files = glob.glob(filename);
        for afile in files:
        #{
            print(afile);
        #}
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}