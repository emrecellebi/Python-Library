#!/usr/bin/env python

import threading;

def do_this():
#{
    print("This is our thread!");
#}

def main():
#{
    out_thread = threading.Thread(target=do_this);
    out_thread.start();

    print(threading.active_count());
    print(threading.enumerate());
    print(threading.current_thread());
#}

if(__name__ == "__main__"):
#{
    main();
#}