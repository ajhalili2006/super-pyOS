import os
import platform    # modules to use
import subprocess
import sys
import glob
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
  print("WARNING- SYSTEM WILL RESET AFTER COMMANDS ARE EXECUTED")
  
  command = input(currentpth + "> ")
  # command prompt ends here, my part is done
  
  # todo= put all commands into a seperate file  
  
  if command == "cmds":
    print("cmds: shows all available commands")
    print("ls: shows all files in the directory")
    
  if command == "ls":
    print(glob.glob(currentpth))

# script closes at this point, so we run this command to loop it
os.system('python3 main.py')