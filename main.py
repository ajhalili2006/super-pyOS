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
import help


# machine settings / enviroment paths

#debug mode ( dev mode )
DEBUG_MODE = False
if os.getenv("DEBUG_PYOS") == None:
  DEBUG_MODE = False # debug mode shuts down the script on execution to prevent damage
elif os.getenv("DEBUG_PYOS") == "true":
  DEBUG_MODE = True
  
#------------------------- LOGGING FILE-------
logging.basicConfig(filename="pyos.log", level=logging.INFO) # log path
#---------------------------------------------

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

#---------------------------------------------
currentpath = os.getcwd() # get current path

#----------------------------------------------------------------------------------------#

#if DEBUG_MODE == "false":
  # print("beginning boot process...")
 
  # run licelock check 1
licelock.antipiracy()
  
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
  
  print("network: configure your network BETA")
  
  print("exit: exit pyOS")
  
  print("help <command/topic>")
  
  os.system("python3 main.py")
  
if command == "ls":
  os.listdir(currentpath)
  #xr = input("path>")
  #if xr == "":
  #  print(str.join("   ",os.listdir(currentpath)))
  #else:
  
   # print(str.join("   ",os.listdir(currentpath + "/" + xr)))
  
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
  os.system("python3 -m venv .virtual")
  
if command == "virtualenv run":
  print("preparing system for virtualisation...")# RUN VENV
  os.system("source .virtual/venv/bin/activate")

# end

if command == "config":
  os.system("python3 config.py")
  
if command == "network":
  print("entering network and DNS configuration...")
  sleep(2)
  os.system("python3 network.py")

if command == "exit":
  sys.exit("exited successfully")
  logging.info("[" + current_time + "]" + ": OS exited successfully")
  
else:
  logging.error("[" + current_time + "]" + ": command " + command + " could not be found")
  
# help topics

if command == "help general":
  help.general()
  
if command == "help virtualenv":
  help.virtualenv()
  
# -------------
os.system('python3 main.py')# this will go through the entire boot process again, the boot section should go into a seperate moduleb
