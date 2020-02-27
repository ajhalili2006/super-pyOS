import os
import io
import platform    # modules to use
import subprocess
import sys
import glob
from time import *

#---------------------------------------------------
licence_status = "valid, available for up to 3 devices"
#---------------------------------------------------

os.system("clear")

print("configuration")
print("---------------")
print("")
print("1. see licence status")
print("2. exit configuration")


config = input("choose an option: ")

if config == "1":
  print(licence_status)
  os.system("python3 main.py")

if config == "2":
  os.system("clear && python3 main.py")
  
else:
  sys.exit("invalid command, system aborted action")