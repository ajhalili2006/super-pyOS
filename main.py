import os
import platform    # modules to use
import subprocess
import sys
from time import *

# machine settings / enviroment paths
DEBUG_MODE = "false" # debug mode shuts down the script on execution to prevent damage
currentpth = os.getcwd()

#----------------------------------------------------------------------------------------#

if DEBUG_MODE == "true":
  sys.exit('debug mode has been enabled- please disable to continue')

if DEBUG_MODE == "false":
  print("beginning boot process...")
  sleep(3)
  # command prompt starts here
  print("pyOS- version 1.0_BETA")
  print("© 2019, protech IT solutions")
  
  command = input 