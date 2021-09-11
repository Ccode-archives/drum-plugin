#!/usr/bin/env python3
# imports
import os
import sys
# import the drum api
home = os.path.expanduser('~')
mymodule_dir = os.path.join( home, 'drumbash', 'api')
sys.path.append( mymodule_dir )
import api

# replace the code below with your own code
print(api.drumver())
