import time
import os
command = input("Enter Command:")
os.system(command)
while command != "exit":
    command = input("Enter Command:")
    os.system(command)