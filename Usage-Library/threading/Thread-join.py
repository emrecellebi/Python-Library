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

def do_after():
#{
    global x;
    
    x = 450;
    while(x < 600):
    #{
        x += 1
    #}
    print("Total Count: " + str(x));
#}

def main():
#{
    global x;
    
    x = 0;
    
    our_thread = threading.Thread(target=do_this);
    our_thread.start();
    our_thread.join();
    
    our_next_thread = threading.Thread(target=do_after);
    our_next_thread.start();
    
#}

if(__name__ == "__main__"):
#{
    main();
#}


