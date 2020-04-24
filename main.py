import os
import io
import platform    # modules to use
import subprocess
import sys
import glob
from time import *
import logging
from datetime import datetime


# machine settings / enviroment paths

#debug mode ( dev mode )
DEBUG_MODE = False
if os.getenv("DEBUG_PYOS") == None:
  DEBUG_MODE = False # debug mode shuts down the script on execution to prevent damage
elif os.getenv("DEBUG_PYOS") == "true":
  DEBUG_MODE = True
  
#------------------------- LOGGING FILE-------
logging.basicConfig(filename="pyos.log", level=logging.INFO)
#---------------------------------------------

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

#---------------------------------------------
currentpath = os.getcwd()

#----------------------------------------------------------------------------------------#

#if DEBUG_MODE == "false":
  # print("beginning boot process...")
 
  # command prompt starts here
  
logging.info("[" + current_time + "]" + ": OS started successfully")
command = input(currentpath + "> ")
  # command prompt ends here
  
  # todo= put all commands into a seperate file  
  

if command == "cmds":
  print("cmds: shows all available commands")
  
  print("ls:   shows all files in the directory")
  
  print("xen:  xent cli")
  
  print("vim: open vim")
  
  print("virtualenv: shows virtualenv")
    
  print("config: opens superPy Configurator")  
    
  print("clear: clears screen")
  
  print("network: configure your network")
  os.system("python3 main.py")
  
if command == "ls":
  xr = input("path>")
  if xr == "":
    print(str.join("   ",os.listdir(currentpath)))
  else:
  
    print(str.join("   ",os.listdir(currentpath + "/" + xr)))
  
if command == "xen":
  os.system('python3 xencli.py')   
    
    
  # setup debug
  
if command == "down-the-rabbit-hole":
  ans = input ("are you sure you want to enable debug(Y/N)> ")
  
if command == "vim":
  os.system("pyvim")
 

if command == "cd":
    np = input(currentpath + "/")

    try:
      os.chdir(currentpath + "/" + np)
    except:
      print("unable to open directory!")
      
if command == "clear":
  #there is a safeguard to this, good!
  try:
    os.system("clear && python3 main.py")
  except:
    # for developer mode:
    if DEBUG_MODE == True:
      print("EXCEPT: attempted 'clear' falling back to 'cls'")
      os.system("cls && python3 main.py")
    # script closes at this point, so we run this command to loop it

# VIRTUALISATION
if command == "virtualenv":
    try:
      os.system("virtualenv")  # SHOW VIRTUALENV CLI COMMANDS
    except:
    # for developer mode:
      if DEBUG_MODE == True:
        print("EXCEPT: attempted 'virtualenv, task terminated in dev mode")
      print("")
if command == "virtualenv venv":
  print("generating virtual environment VENV")  # GENERATE VENV
  os.system("virtualenv venv")
  
if command == "virtualenv run":
  print("preparing system for virtualisation...")# RUN VENV
  os.system("source venv/bin/activate")

# end

if command == "config":
  os.system("python3 config.py")
  
if command == "network":
  print("entering network and DNS configuration...")
  sleep(2)
  os.system("python3 network.py")

    
os.system('python3 main.py')#this will go through the entire boot process again, the boot section should go into a seperate moduleb