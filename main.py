import os
import io
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
  sys.exit('debug mode has been enabled- all system processes have been halted')

if DEBUG_MODE == "false":
  print("beginning boot process...")
  sleep(3)
  # command prompt starts here
  
  command = input(currentpth + "> ")
  # command prompt ends here
  
  # todo= put all commands into a seperate file  
  
  if command == "cmds":
    print("cmds: shows all available commands")
    print("ls: shows all files in the directory")
    
  if command == "ls":
    print(glob.glob(currentpth))
    
  if command == "xen":
    os.system('python3 xencli.py')

# script closes at this point, so we run this command to loop it
os.system('python3 main.py')#this will go through the entire boot process again, the boot section should go into a seperate module