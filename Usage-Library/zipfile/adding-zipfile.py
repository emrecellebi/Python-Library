#!/usr/bin/env python

from zipfile import *;

def main():
#{
    file_name = "shopping.zip";
    
    items = ["eggs", "cats", "tonka_trucks", "people", "babies", "virgins", "pumpkins"];
    
    zip_archive = ZipFile(file_name, "w");
    
    for item in items:
    #{
        object_name = item + ".txt";
        object_handle = open(object_name, "w");
        object_handle.write("I need to buy some " + item.upper() + "!");
        object_handle.close();
        
        zip_archive.write(object_name);
    #}
    
    zip_archive.close();
#}

if(__name__ == "__main__"):
#{
    main();
#}