import os
import io
import platform    # modules to use
import subprocess
import sys
import glob
from time import *

# machine settings / enviroment paths

#debug mode ( dev mode )
DEBUG_MODE = False
if os.getenv("DEBUG_PYOS") == None:
  DEBUG_MODE = False # debug mode shuts down the script on execution to prevent damage
elif os.getenv("DEBUG_PYOS") == True:
  DEBUG_MODE = True
  
  
  
#-------------------------  
currentpth = os.getcwd()

#----------------------------------------------------------------------------------------#

#if DEBUG_MODE == "false":
  # print("beginning boot process...")
 
sleep(3)
  # command prompt starts here
  

command = input(currentpth + "> ")
  # command prompt ends here
  
  # todo= put all commands into a seperate file  
  

if command == "cmds":
  print("cmds: shows all available commands")
  
  print("ls:   shows all files in the directory")
  
  print("xen:  xent cli")
    
    
if command == "ls":

  if DEBUG_MODE == True:
    0
  
  print(glob.glob(currentpth))
    
  
if command == "xen":

  os.system('python3 xencli.py')
    
    
    
  # setup debug
  
if command == "down-the-rabbit-hole":

  ans = input ("are you sure you want to enable debug(Y/N)> ")
  
  if ans == "Y":
    print("we are setting up developer mode! please wait")
    DEBUG_MODE = True
    os.putenv("DEBUG_PYOS", True)

# script closes at this point, so we run this command to loop it
os.system('python3 main.py')#this will go through the entire boot process again, the boot section should go into a seperate module