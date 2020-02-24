from os import getenv, putenv, system,environ



if getenv("DEBUG_PYOS") == "true":
  print("you are booting in developer mode, be cautious")
print(environ)

  
system("python3 main.py")