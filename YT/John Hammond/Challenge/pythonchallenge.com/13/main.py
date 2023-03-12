#!/usr/bin/env python2

import xmlrpclib;

def main():
#{
    servername = "http://www.pythonchallenge.com/pc/phonebook.php";
    client = xmlrpclib.ServerProxy(servername);
    print client.phone('Bert');
#}

if(__name__ == "__main__"):
#{
    main();
#}

