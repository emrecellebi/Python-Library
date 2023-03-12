#!/usr/bin/env python2

import datetime, calendar;

def main():
#{
    for year in range(1006, 1996, 10):
    #{
        if datetime.datetime(year, 1, 27). weekday() == 1:
        #{
            if(calendar.isleap(year)):
            #{
                print "leap year", year;
            #}
        #}
    #}
#}

if(__name__ == "__main__"):
#{
    main();
#}

