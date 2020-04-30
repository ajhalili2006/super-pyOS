import os
import io
import platform    # modules to use
import subprocess
import sys
import glob
from time import *
import logging
from datetime import datetime
import licelock

def general():
  os.system("clear")
  print("--------------------------------------------------")
  print("PYOS general info")
  print("")
  print("pyOS is a small operating system built with the python language, it uses several")
  print("libraries to simulate general commands and applications. While about 25% relies ")
  print("on normal linux commands.")
  print("")
  print("it was built to show people what a bit of code can turn into, the software is free")
  print("of any hidden charges under the MIT license")
  print("")
  print("big thanks to Jonyk5 for always being there. :D")
  print("--------------------------------------------------")
  
def virtualenv():
  os.system("clear")
  print("Virtualisation is hard, heavy duty work.")
  print("")
  print("we can't rewrite Qemu, that's diabolical! instead we use virtualenv that is integrated into python")
  print("you can run the command virtualenv to see how to create a venv. We only get so much space in one")
  print("terminal session")
