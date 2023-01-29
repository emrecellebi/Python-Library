#!/usr/bin/env python

from zipfile import *;

def main():
#{
    file_name = "shopping.zip";
    
    zip_archive = ZipFile(file_name);
    
    zip_info = zip_archive.getinfo("virgins.txt");
    print("File Name: " + str(zip_info.filename));
    print("Date Time: " + str(zip_info.date_time));
    
    zip_archive.close();
#}

if(__name__ == "__main__"):
#{
    main();
#}