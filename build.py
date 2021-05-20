#!/usr/bin/env python3

#Build distribution packages using setuptools
import os

os.system("rm dist/*")
os.system("python3 setup.py sdist bdist_wheel")