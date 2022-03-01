import sys
import os
import hashlib

def getsha256(file):
    try:
        hashsha = hashlib.sha256()
        with open(file, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                hashsha.update(block)
        return hashsha.hexdigest()
    except Exception as e:
        print(f"Error: {e}")
        return ""
    except:
        print("Error desconocido")
        return ""

pathfile = os.getcwd() + "/" + sys.argv[1]
print('BASH: ' + getsha256(pathfile))