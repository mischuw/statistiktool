import os
import time
import re


datei = open("/Users/mischu/Desktop/Intern/Statistiktool/ia.log", "r")

print "Am 26. Januar passierte folgendes:"
for zeile in datei:
    m = re.match(r"May 07 (.*)", zeile)
    if m != None:
        print m.group(1)

       
        
        
    
