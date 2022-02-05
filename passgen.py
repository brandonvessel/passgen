from os import remove
from hashlib import sha256
from time import sleep
import os
import subprocess

desiredLength = 20

# special characters
special_characters = list("!@#$%^&*()"*1000)

# numbers
numbers = list("1234567890"*1000)

# letters
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"*1000)

def copy2clip(txt):
    '''Copies txt (str) into the clipboard'''
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

# get master from user
master = str(input("Input Text:"))

# clear terminal if you want
#os.system('cls' if os.name == 'nt' else 'clear')

# particular password from user
#sub = str(input("Application:"))

#outputhash = sha256(master.encode() + sub.encode())
outputhash = sha256(master.encode())

output = outputhash.hexdigest()[0:20] + str(special_characters[ord(outputhash.hexdigest()[0])*2]) + str(numbers[ord(outputhash.hexdigest()[1])*3]) + str(letters[ord(outputhash.hexdigest()[2])*4])

# control length
output = "".join(list(output)[len(output)-desiredLength + 1:len(output)-1])

print(output)
print("Copied to clipboard")
try:copy2clip(output)
except:pass

with open("output.txt", "a") as f:
    f.write(output + "\n")