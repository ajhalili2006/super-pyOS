import os
import platform    # modules to use
import subprocess
import sys
from time import *

# machine settings
DEBUG_MODE = "false" # debug mode shuts down the script on execution to prevent damage

#----------------------------------------------------------------------------------------#

if DEBUG_MODE == "true":
  sys.exit('debug mode has been enabled- please disable to continue')

if DEBUG_MODE == "false":
  print("beginning boot process...")
  
  