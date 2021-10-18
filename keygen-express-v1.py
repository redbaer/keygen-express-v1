import os
import random
import string
import hashlib

clear = "\n" * 100

method = ""
maxchars = 0

def gen(length):
    global generated
    generated = ""
    if(method == "1"):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    elif(method == "2"):
        result_str = ''.join(random.choice(string.digits) for i in range(length))
    elif(method == "3"):
        result_str = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    print("Key (Method: #" + str(method) + ", Max: " + str(maxchars) + "):", result_str)
    generated = result_str


def hash():
    hashed = hashlib.md5(generated.encode())
    print("Hash (MD5): ", hashed.hexdigest())

def prompthash():
    print("\n")
    i3 = input("Would you like to hash this result? (Y/n): ")
    if(i3 == "Y"):
        print(clear)
        print("Hashing in MD5...")
        print(clear)
        print("Key (Method: #" + str(method) + ", Max: " + str(maxchars) + "):", generated)
        hash()
        print("\n")
    elif(i3 == "n"):
        print(clear)
        print("Key (Method: #" + str(method) + ", Max: " + str(maxchars) + "):", generated)
        print("\n")

print("Keygen Express 1.0")
i = input("Type 'start' to enter the program: ")

if(i == "start"):
    print(clear)
    i1 = input("\n1) Strictly Alphabetical\n2) Strictly Numeric \n3) Alphanumeric (Both Alphabetical and Numeric) \nType your choice: ")
    method = i1
    if(i1 == "1"):
        print(clear)
        print("Using strict method #1 (Alphabetical)")
        print("\n")
        i2 = input("Enter a char limit: ")
        maxchars = int(i2)
        print(clear)
        print("Using method #1 (Alphabetical) with limit " + str(maxchars))
        print("\n")
        print("Generating key...")
        print(clear)
        gen(maxchars)
        prompthash()
    elif(i1 == "2"):
        print(clear)
        print("Using strict method #2 (Numeric)")
        print("\n")
        i2 = input("Enter a char limit: ")
        maxchars = int(i2)
        print(clear)
        print("Using method #2 (Numeric) with limit " + str(maxchars))
        print("\n")
        print("Generating key...")
        print(clear)
        gen(maxchars)
        prompthash()
    elif (i1 == "3"):
        print(clear)
        print("Using method #3 (Alphanumeric)")
        print("\n")
        i2 = input("Enter a char limit: ")
        maxchars = int(i2)
        print(clear)
        print("Using method #3 (Alphanumeric) with limit " + str(maxchars))
        print("\n")
        print("Generating key...")
        print(clear)
        gen(maxchars)
        prompthash()

