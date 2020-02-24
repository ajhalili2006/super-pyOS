import os
from time import sleep
print("***PYOS***")
sleep(3)
try:
  os.system("clear")
except:
  os.system("cls")
sleep(2)
os.system("python3 debug.py")