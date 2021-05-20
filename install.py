#!/usr/bin/env python3

#Build the package and install (Installation is the same as if installed from pypi -> that means it also does not update with code changes!)
import os
os.system("python3 build.py")
files = os.listdir("dist")
install_command = "pip3 install " + os.path.join("dist", files[0])
print("Executing: " + install_command)
os.system(install_command)

