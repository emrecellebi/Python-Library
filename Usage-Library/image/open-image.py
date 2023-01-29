#!/usr/bin/env python

from PIL import Image;

def main():
#{
    filename = "img/3.jpg"
    
    image = Image.open(filename);
    image.show();
    
    del image;
#}

if(__name__ == "__main__"):
#{
    main();
#}