#!/usr/bin/env python2

def main():
#{
    file_handle = open("evil2.gfx", "rb");
    gfx = file_handle.read();
    
    images = {};
    number = 5;
    
    for i in range(number):
    #{
        images[i] = open("image" + str(i) + ".jpg", "wb");
    #}
    
    for b in range(0, len(gfx), number):
    #{
        # print ord(gfx[b]);
        for i in range(number):
        #{
            images[i].write(gfx[b + i]);
        #}
    #}
    file_handle.close();
    
    for i in range(number):
    #{
        images[i].close();
    #}
#}

if(__name__ == "__main__"):
#{
    main();
#}

