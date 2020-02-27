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

print("\033[1;31mConfiguration\033[1;m")
print("---------------")
print("")
print("1. see licence status")
print("2. exit configuration")
print("3. force install all packages")
print("4. edit .bashrc file")
print("5. edit .env")

config = input("choose an option: ")

if config == "1":
  print(licence_status)
  os.system("python3 main.py")

if config == "2":
  os.system("clear && python3 main.py")
  
if config == "3":
  os.system("pip install -r requirements.txt")
  
if config == "4":
  os.system("vim .bashrc")

if config == "5":
  os.system("vim .env")
  
else:
  sys.exit("invalid command, system aborted action")