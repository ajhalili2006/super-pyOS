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
elif os.getenv("DEBUG_PYOS") == "true":
  DEBUG_MODE = True
  
  
#-------------------------  
currentpth = os.getcwd()

#----------------------------------------------------------------------------------------#

#if DEBUG_MODE == "false":
  # print("beginning boot process...")
 
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
    print ("test debug")
  exn = ""
  print(glob.glob(currentpth))
  
if command == "xen":

  os.system('python3 xencli.py')
    
    
    
  # setup debug
  
if command == "down-the-rabbit-hole":

  ans = input ("are you sure you want to enable debug(Y/N)> ")
  
  if ans == "Y":
    print("we are setting up developer mode! please wait")
    print("ok, we need a bit of help to activate the modules!\nrun the command specified for your os ( all linux os are listed under 'linux', and it must be placed in the .bashrc file at the ***BOTTOM***)")
    print("WINDOWS 10:  setx DEBUG_PYOS true")
    print("LINUX:       export DEBUG_PYOS=\"true\"")
    # script closes at this point, so we run this command to loop it
os.system('python3 main.py')#this will go through the entire boot process again, the boot section should go into a seperate module