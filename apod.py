#!/usr/local/bin/python
##############################
#Creates: apod.jpg
#Written by Ben Rose
#brose3@nd.edu
#On 2013-06-24 
#Notes: 
##############################
import urllib2
from HTMLParser import *
import os

# Grab html file from apod website
response = urllib2.urlopen('http://apod.nasa.gov/apod/astropix.html')
html = response.read() 

# make class to find line with image
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        ## Only parse the 'anchor' tags.
        if tag == "a":
           ### Check the list of defined attributes.
           for name, value in attrs:
               # image has name ==ref, stars with 'i' and ends with 'jpeg' -> worked on 2013-06-25 and 2013-06-24
               if name == "href" and value.startswith("i") and value.endswith("jpg"):
                    self.output = value #return the path+file name of the image
                    break

# get image's url
parser = MyHTMLParser()
parser.feed(html)
imgurl='http://apod.nasa.gov/apod/'+ parser.output
print imgurl

# download and rename to apod.jpg, could use '-O ' instead of '--output-document=' 
# os.system('wget --output-document=apod.jpg ' + imgurl)
os.system('wget  ' + imgurl) #without renaming, use with [hazel](http://www.noodlesoft.com/hazel.php)
