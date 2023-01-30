#!/usr/bin/env python

from PIL import Image;

def main():
#{
    filename = "img/5.jpg";
    image = Image.open(filename);
    size = width, height = image.size;
    
    image.thumbnail((128, 128));
    image.show();
    
    del image;
#}

if(__name__ == "__main__"):
#{
    main();
#}