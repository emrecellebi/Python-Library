#!/usr/bin/env python

import urllib;

class Base:
#{
    def __init__(self):
    #{
        proxy = {'http', 'http://107.1.39.55:3128'};
        urllib.urlopen('http://whatismyip.com', proxies=proxy);
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}