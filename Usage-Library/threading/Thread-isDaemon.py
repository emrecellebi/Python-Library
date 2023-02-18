#!/usr/bin/env python

import threading;

def do_this():
#{
    global x;
    while(x < 300):
    #{
        x += 1
    #}
    if x == 300:
    #{
        print("Total Count: " + str(x));
    #}
#}

def main():
#{
    global x;
    
    x = 0;
    
    our_thread = threading.Thread(target=do_this);
    our_thread.start();
    our_thread.setDaemon(True);
    print(our_thread.isDaemon());
    
#}

if(__name__ == "__main__"):
#{
    main();
#}


