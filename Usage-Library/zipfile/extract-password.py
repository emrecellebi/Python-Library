#!/usr/bin/env python

from zipfile import *;

def main():
#{
    file_name = "shopping.zip";
    
    zip_archive = ZipFile(file_name);
    
    zip_archive.setpassword("123456");
    zip_archive.extract("virgins.txt");
    
    zip_archive.close();
#}

if(__name__ == "__main__"):
#{
    main();
#}