#!/usr/bin/env python3
# imports
import os
import sys
# import the drum api
home = os.path.expanduser('~')
mymodule_dir = os.path.join( home, 'drumbash', 'api')
sys.path.append( mymodule_dir )
import api
from sys import exit

args = sys.argv
try:
    if args[1] == "-h":
        print("indev")
    elif args[1] == "-v":
        print(api.drumver())
    else:
        print("try using -h")
except:
    print("error")
