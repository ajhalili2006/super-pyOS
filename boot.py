import os
from time import sleep
print("\033[3;37;40m **PYOS** \033[0;37;40m \n")
print("a collab between ProtechCEO and J-tech-foundation \033[0m")

sleep(3)
#no, this is pauser so people can read above :)
#bios is on everything, no matter what ;)
# ok, but we still gotta install it using boot :)
# i know, graphical or command-line. well virtualenv is readyz
#gtg for now, be back in a little bit ;)
# ive gtg anyway,cya
try:
  os.system("clear")
except:
  os.system("cls")
print("install dependencies?(\033[38;5;28mY\033[0m/\033[38;5;124mN\033[0m)")

installdep = input("> ")

if installdep == "Y":
  os.system("pip3 install -r requirements.txt")
  os.system("python3 debug.py")
  
if installdep == "N":
  os.system("python3 debug.py")