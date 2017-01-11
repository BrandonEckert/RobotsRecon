#!/usr/bin/python
# Copyright (c) 2017, Brandon Eckert
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

import urllib.request, urllib.error, urllib.parse
import os
import sys
import requests

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
    print((r"""
         (\____/)
          (_""" + bcolors.RED + r"""oo""" + bcolors.ENDC + r""" _)
            (O)
          __||__    \)
       []/""" + bcolors.BLUE + r"""______""" + bcolors.ENDC + r"""\[] /
       / \______/ \/
      /    /__\
     (\   /____\

     """ + bcolors.BOLD + """RobotsRecon""" + bcolors.ENDC + """
        """))

os.system('clear')
gen_banner()
print("RobotsRecon - Reads robots.txt from website,")
print("and checks disallow if directories exist.")
print("Written by: Brandon Eckert")
print("")
print("Website: http://www.brandoneckert.com")
print("")
print("Usage: python3 ./robotsrecon.py http://<ip address or domain name>")
print("")

# get url from parameter
try:
    urlstring = (sys.argv[1])
except Exception:
    print ((bcolors.RED + "Exception: Did you forget IP/URL?" + bcolors.ENDC))
    exit()
# Attempt to find robots.txt
try:
    print ((bcolors.BLUE + "Attempting to download robots.txt..." + bcolors.ENDC))
    urllib.request.urlretrieve(urlstring + '/robots.txt', 'robots.txt')
    print ((bcolors.GREEN + "Download complete..." + bcolors.ENDC))
except Exception:
    print ((bcolors.RED + "Exception: Unable to find robots.txt. Does it exist? or is the site up?" + bcolors.ENDC))
    exit()
# Attempt to read robots.txt line by line
print ((bcolors.BLUE + "Checking status of disallowed directories..." + bcolors.ENDC))
robotsfile = tuple(open('robots.txt', 'r'))
try:
    for line in robotsfile:
            if line[0] != '#' and line[0].strip() != '':
                    lineSplit = line.split(': ')
                    if lineSplit[0].lower() == 'disallow':
                            targetUrl = urlstring +'%s' % lineSplit[1].strip()
                            response = requests.get(targetUrl)
                            if response.status_code != 404:
                                    print ((bcolors.GREEN + "FOUND:" + targetUrl + bcolors.ENDC))
                            else:
                                    print ((bcolors.RED + "NOT FOUND:" + targetUrl + bcolors.ENDC))
except Exception:
    print ((bcolors.RED + "EXCEPTION: Something has occured while parsing robots.txt..." + bcolors.ENDC))
    exit()

# Cleanup
try:
    print ((bcolors.BLUE + "Cleaning up..." + bcolors.ENDC))
    os.remove('robots.txt')
except Exception:
    pass

