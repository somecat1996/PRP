from my_scanner_openvas.task import *
import re


f = open('fhuisfh.txt','r')
r = f.read()
f.close()

rr = re.findall('(<task.*?</task>)', r)
a = task()
a.load(rr[0])
a.display()