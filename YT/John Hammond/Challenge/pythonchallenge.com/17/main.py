#!/usr/bin/env python2

import requests;
import urllib;
import bz2;

def main():
#{
    array = [];
    data = '';
    next_nothing = '12345';
    while True:
    #{
        try:
        #{
            url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + str(next_nothing);
            response = requests.get(url);
            next_nothing = response.text.split()[-1];
            info = response.cookies["info"];
            print('next_nothing', next_nothing, 'info', info);
            array.append(info);
        #}
        except:
        #{
            data = ''.join(array)
            print(data + '\n');
            break;
        #}
    #}
    
    data = urllib.unquote_plus(data);
    print(repr(data + '\n'));
    
    decompressor = bz2.BZ2Decompressor();
    data = decompressor.decompress(data);
    print(data);
    
    cookies = {'info', 'the flowers are on their way'};
    url = 'http://www.pythonchallenge.com/pc/stuff/violin.php';
    response = requests.get(url, cookies=cookies);
    
    print(response.text)
#}

if(__name__ == "__main__"):
#{
    main();
#}