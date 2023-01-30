#!/usr/bin/env python

from urllib import *;

def main():
#{
    page = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html");
    
    contents = page.read();
    
    page.close();
    
    mess = contents.split("-->")[1].split("<!--\n")[1];
    
    items = {};
    for item in mess:
    #{
        if item in items:
        #{
            items[item] = items[item] + 1;
        #}
        else:
        #{
            items[item] = 1;
        #}
    #}
    
    print("Items: " + str(items))
    
    found = [];
    for key in items.iterkeys():
    #{
        if(items[key] > 1):
        #{
            found += [key];
        #}
    #}
    
    for item in found:
    #{
        mess = mess.replace(item, "");
    #}
    
    print("Mess: " + str(mess))
    
    for item in items:
    #{
        if items[item] == 1:
        #{
            print(item);
        #}
    #}
#}

if(__name__ == "__main__"):
#{
    main();
#}