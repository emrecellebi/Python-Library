#!/usr/bin/env python

import threading;

def do_this():
#{
    global x, lock;
    
    lock.acquire()
    try:
    #{
        while(x < 300):
        #{
            x += 1
        #}
        if x == 300:
        #{
            print("Total Count: " + str(x));
        #}
    #}
    finally:
    #{
        lock.release();
    #}
#}

def do_after():
#{
    global x, lock;
    
    try:
    #{
        x = 450;
        while(x < 600):
        #{
            x += 1
        #}
        print("Total Count: " + str(x));
    #}
    finally:
    #{
        lock.release();
    #}
#}

def main():
#{
    global x, lock;
    
    x = 0;
    
    lock = threading.Lock();
    
    our_thread = threading.Thread(target=do_this);
    our_thread.start();
    our_thread.join();
    print("Ident Number: " + str(our_thread.ident));
    
    our_next_thread = threading.Thread(target=do_after);
    our_next_thread.start();
    print("Ident Number: " + str(our_next_thread.ident));
#}

if(__name__ == "__main__"):
#{
    main();
#}


