#!/usr/bin/env python2

import zipfile;

def main():
#{
    the_zip = zipfile.ZipFile("channel.zip");
    comments = [];

    def next_nothing(filename):
    #{
        text = the_zip.read(filename);
        _next = text.split()[-1];
        
        if(_next != "comments."):
        #{
            next_nothing(_next + ".txt");
            comments.append(the_zip.getinfo(_next + ".txt").comment);
        #}
    #}

    next_nothing("90052.txt");
    
    for comment in reversed(comments):
    #{
        print comment,;
    #}
#}

if(__name__ == "__main__"):
#{
    main();
#}

