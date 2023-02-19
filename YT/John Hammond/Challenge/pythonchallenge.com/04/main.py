#!/usr/bin/env python

from urllib import *;
from string import *;

def main():
#{
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php";
    
    page = urlopen(url);
    
    contents = page.read();
    page.close();
    
    link_start = 'a href="'
    link_end = '"'
    
    _next = contents.split(link_start)[1].split(link_end)[0][23:];
    
    def go_to_new_nothing(nothing):
    #{
        new_url = url + "?nothing=" + nothing;
        page = urlopen(new_url);
        contents = page.read();
        page.close();
        return contents.split()[-1];
    #}
    
    # _next = 16044
    # _next /= 2
    # _next = str(_next)
    
    while(_next == str(int(_next))):
    #{
        _next = go_to_new_nothing(_next);
        print(_next);
        go_to_new_nothing(_next);
    #}
    
#}

if(__name__ == "__main__"):
#{
    main();
#}

