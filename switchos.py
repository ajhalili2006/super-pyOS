import os
import io
import platform    # modules to use
import subprocess
import sys
import glob
from time import *

os.system("clear")
print("\033[1;31mSwitch OS utility\033[1;m")
print("version 1.0")
print("")
print("switch your OS here")
print("")
print("")
print("1. switch execution path")

switcher = input("choose an option: ")
i
if switcher == "1":
  os.system("clear")
  switcherpath = input("") # need to code something that'll switch to the folder and run the files thereimport os
import io
import platform    # modules to use
import subprocess
import sys
import glob
from time import *

os.system("clear")
print("\033[1;31mSwitch OS utility\033[1;m")
print("version 1.1")
print("")
print("switch your OS here")
print("")
print("")
print("1. switch execution path")

switcher = input("choose an option: ")

if switcher == "1":
  os.system("clear")
  print("please set variable EXECUTION_PATH:")
  print("format: FOLDERNAME/")
  print("No need to put the script name- we handled that")
  path = input("EXECUTION_PATH = ")
  print("switching to OS...")
  sleep(2)
  os.system("python3 " + path + "/" + "boot.py")
