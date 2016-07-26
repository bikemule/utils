#!/usr/bin/awk
# Taken from http://www.ibm.com/developerworks/library/l-awk1/index.html
BEGIN { x=0 } 
/^$/  { x=x+1 } 
END   { print "I found " x " blank lines. :)" }
