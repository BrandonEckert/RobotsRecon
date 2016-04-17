#!/usr/bin/python
# Copyright (c) 2016, Brandon Eckert
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# RobotsRecon - Reads website robots.txt from website and checks disallow if directories exist.
#
# Written by: Brandon Eckert
# Website: http://www.brandoneckert.com
#
# Usage: python ./robotsrecon.py http://<ip address or domain name>

import requests
import urllib2
import os
import sys

# set text color class


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# generate banner, clear screen, print banner
def gen_banner():
    print(r"""
         (\____/)
          (_""" + bcolors.RED + r"""oo""" + bcolors.ENDC + r""" _)
            (O)
          __||__    \)
       []/______\[] /
       / \______/ \/
      /    /__\
     (\   /____\

     """ + bcolors.BOLD + """RobotsRecon""" + bcolors.ENDC + """
        """)

os.system('clear')
gen_banner()
print "RobotsRecon - Reads website robots.txt from website,"
print "and checks disallow if directories exist"
print "Written by: Brandon Eckert"
print ""
print "Website: http://www.brandoneckert.com"
print ""
print "Usage: python ./robotsrecon.py http://<ip address or domain name>"
print "Parsing robots.txt..."
print ""

# get url from parameter and get robots.txt
try:
    urlstring = (sys.argv[1])
    lines = urllib2.urlopen(urlstring + '/robots.txt')
    # read robots.txt check each directory for non 404
    for line in lines:
        if line[0] != '#' and line[0].strip() != '':
            lineSplit = line.split(': ')
            if lineSplit[0].lower() == 'allow' or lineSplit[0].lower() == 'disallow':
                targetUrl = urlstring + '%s' % lineSplit[1].strip()
                r = requests.get(targetUrl)
                if r.status_code != 404:
                    print bcolors.GREEN + "FOUND: " + targetUrl + bcolors.ENDC

except Exception:
    print bcolors.RED + "Exception: Did you forget parameter? Or is website live?" + bcolors.ENDC