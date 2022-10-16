#!/usr/bin/env python

import sys

class Base:
#{
    def __init__(self):
    #{
        if(len(sys.argv) < 3):
        #{
            sys.stderr.write("E: usage: " + sys.argv[0] + " <filename> <word> ");
            sys.stderr.flush();
            
            exit(2);
        #}
        else:
        #{
            filename = sys.argv[1];
            needle = sys.argv[2];
        #}
        
        counter = 0
        file_handle = open(filename);
        
        for line in file_handle.readlines(): 
        #{
            words = line.split(" ");
            for word in words: 
            #{
                if(word == words[-1]):
                #{
                    word = word[:-1];
                #}
                
                if(word == needle):
                #{
                    counter += 1;
                #}
            #}
        #}
        print(counter);
        exit(0);
    #}
#}

if(__name__ == "__main__"):
#{
    root = Base();
#}