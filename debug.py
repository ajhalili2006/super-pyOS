from os import getenv, putenv, system



if getenv("DEBUG_PYOS") == "true":
  print("you are booting in developer mode, be cautious")

  
system("python3 main.py")