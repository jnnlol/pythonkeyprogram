import pyfiglet
import time

print(pyfiglet.figlet_format("JNN"))

keycheck = input("What is your key: ")
key = "YOURKEY"

if keycheck == key:
    print("Valid key! Welcome to the program.")
else:
    print("Invalid key, quitting program in 3 seconds.")
    time.sleep(3)
    quit()