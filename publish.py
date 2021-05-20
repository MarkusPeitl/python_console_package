#!/usr/bin/env python3

#Build package and publish to pypi using twine
import os
os.system("python3 build.py")
#Requires twine to be installed `pip3 install twine`
os.system("twine check dist/*")
os.system("twine upload dist/*")