#!/usr/bin/env python2

import urllib2;

def main():
#{
    address = 'http://web.lasactf.com:45025';
    
    opener = urllib2.build_opener();
    opener.addheaders = [
        ('User-Agent', 'Google Ultron'),
        ('SpecialAuth', 'Kyle'),
        ('Referer', 'kyleisacoolguy.org')
    ];
    
    response = opener.open(address);
    
    print(response.read().split(':')[-1].replace('</h1>', ''));
#}

if(__name__ == "__main__"):
#{
    main();
#}