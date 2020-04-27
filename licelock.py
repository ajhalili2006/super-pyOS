import os
import sys
import logging
from datetime import datetime
from time import *

logging.basicConfig(filename="pyos.log", level=logging.INFO)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

def antipiracy():
  logging.warn("[" + current_time + "]" + ": this software utilises the EN_LICE_ULOCK mechanism")
  sleep(2)
  f = open("LICENSE.txt", "r")
  sleep(2)
  logging.info("[" + current_time + "]" + ": anti-piracy test complete, execution starting...")
  sleep(2)
  logging.error("[" + current_time + "]" + ": if script has not run, then we have detected a bad apple")
  logging.critical("[" + current_time + "]" + ": required file has not been found, please get a copy for the script to run")
# the python module initialising security mechansim EN_LICE_ULOCK (ENCRYPTED_LICENCE_UNLOCK)
#-------------------------------------------------------------------------------------------
# COPYRIGHT 2020- 17lwinn & jonyk5

import os
import sys
import logging
from datetime import datetime
from time import *

logging.basicConfig(filename="pyos.log", level=logging.INFO)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

#-------------------------------------------------------------------

def antipiracy():
  logging.warn("[" + current_time + "]" + ": this software utilises the EN_LICE_ULOCK mechanism, which is in all its glory useless")
  sleep(2)
  f = open("LICENSE.txt", "r")
  sleep(2)
  logging.info("[" + current_time + "]" + ": anti-piracy test complete, execution starting...")
  sleep(2)
  logging.error("[" + current_time + "]" + ": if script has not run, then we have detected a bad apple")
  logging.critical("[" + current_time + "]" + ": required file has not been found, please get a copy for the script to run")
  
#-------------------------------------------------------------------
  
def keylock():
    from base64 import (
        b64encode,
        b64decode,
    )

    from Crypto.Hash import SHA256
    from Crypto.Signature import PKCS1_v1_5
    from Crypto.PublicKey import RSA


    message = "Validated"
    digest = SHA256.new()
    digest.update(message)

    # Read shared key from file
    private_key = False
    with open ("superpy.pem", "r") as myfile:
        private_key = RSA.importKey(myfile.read())

    # Load private key and sign message
    signer = PKCS1_v1_5.new(private_key)
    sig = signer.sign(digest)

    # Load public key and verify message
    verifier = PKCS1_v1_5.new(private_key.publickey())
    verified = verifier.verify(digest, sig)
    assert verified, ("Signature verification failed")
    print("Successfully verified signature, booting...")
    os.system("python3 boot.py")
