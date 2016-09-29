# coding: utf-8
import os
import urllib
from lxml.html import fromstring

if os.path.exists('out'):
    os.remove('out')

def write_out(line):
    out=open('out','a')
    out.write(line+'\n')
    out.close()

input_list=[line.strip() for line in open('input','r')]
xpath_list=input_list[1:]
html = urllib.urlopen(input_list[0]).read();
tree = fromstring(html) 
for xpath_line in xpath_list:
    xpath_line=xpath_line.split('\t\t')
    if len(xpath_line)==2:
        title,xpath=xpath_line
        xpath_val=''.join(map(lambda x:x.strip(),tree.xpath(xpath)))
        out_line='%s\t\t%s'%(title,xpath_val)
        print out_line
        write_out(out_line)
    else:
        title=xpath_line[0]
        out_line='the title %s is not associated with any xpath expression' % title
        print out_line
        write_out(out_line)
print 'done!'