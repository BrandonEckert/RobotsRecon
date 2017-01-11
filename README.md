# RobotsRecon

This simple scripts simply reads the contents of a supplied websites robots.txt file, and checks each directory marked disallow to see if the directory actually exists.

## Arguments:
The only argument is to supply the URL of the website after calling robotsrecon.py (i.e. python ./robotsrecon.py http://<IP Address or Domain Name>


## Installation:
<pre>git clone https://github.com/BrandonEckert/RobotsRecon.git && cd RobotsRecon/ && pip install -r requirements.txt</pre>
## Usage:

With a domain target:
<pre>python3 ./robotsrecon.py http://domain.com</pre>
With an IP target:
<pre>python3 ./robotsrecon.py http://127.0.0.1</pre>
