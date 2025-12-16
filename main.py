score = 100

import os
from random import randint
import time



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("divorsed? she took the kids? depressed? WELCOME TO GAMBLING!")
input("press enter to start...")

while score > 0:   
    for i in range(10):
        left = randint(0,9)
        center = randint(0,9)
        right = randint(0,9)
        clear()
        print(f"|{left}|{center}|{right}|")
        time.sleep(1/60)
    score -=5
    if left == center and left == right:
        score += 100
    elif left == center or center == right:
        score += 50
    print (score)

    if "y" in input("Do you want to quit? y to quit:   ").lower():
        break
        print (score)