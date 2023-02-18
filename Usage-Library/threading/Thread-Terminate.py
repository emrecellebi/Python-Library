#!/usr/bin/env python

import threading;

def do_this():
#{
    global dead;
    x = 0;
    print("This is our thread!\n");
    while(not dead):
    #{
        x += 1
        pass;
    #}
    print("Total Count: " + str(x));
#}

def main():
#{
    global dead
    dead = False;
    
    out_thread = threading.Thread(target=do_this);
    out_thread.start();

    print(threading.active_count());
    print(threading.enumerate());
    print(threading.current_thread());

    input("Hit enter to die.");
    dead = True;
    
#}

if(__name__ == "__main__"):
#{
    main();
#}


