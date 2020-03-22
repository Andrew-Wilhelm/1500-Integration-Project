#Andrew Wilhelm
#My Intergration Project
#duck hunt THE GAME
#dammage counter
#combo counter

import math
import random

def introduction():
    intro_answer = input("Would you like to play a game? \nType yes or no? ")
    if intro_answer == "yes":
        print("Welcome to Duck Hunt")
    else:
        print("Welcome to Duck Hunt Any Way!")

def duck_shooting():
    duck = input("Do you want to shoot duck 1 2 3 or 4?")
    score = 0
    if duck == 1:
        if chance_hit() == 1:
            print("good job you got 500 points")
            score += (500)
        else:
            print("Dang, you missed")
    elif duck == 2:
        if chance_hit() == 1:
            print("good job you got 1000 points")
            score += (1000)
        else:
            print("Dang, you missed")
    elif duck == 3:
        
        if chance_hit() == 1:
            print("good job you got 1000 points")
            score += (5000)
        else:
            print("Dang, you missed")
    elif duck == 4:
        if chance_hit() == 1:
            print("good job you got 1000 points")
            score += (3000)
        else:
            print("Dang, you missed")
    else:
        print("That is not a duck you silly Goose")
    print("Score:"+("{:08d}".format(score)))

#Chance of hitting the duck
#level_difficulty will lower as it gets harder
def chance_hit():
    rand_num = random.randint(1,14)
    if rand_num >= level_difficulty():
        hit = 1
    else:
        hit = 0
    return hit

#sets the number of ducks to apear in a round and how strong they will be
def number_of_ducks():
    num_ducks = random.randint(1,30)
def duck_power():
    number_of_ducks() 
    for index in range (1,num_ducks):
        level_difficulty()
        power_lvl = lvl_diff

        
def level_difficulty():
    lvl_diff = random.randint(1,5)
    return lvl_diff

def shop():
    if score < item:
        purchased = 0
    else:
        purchased = 1
    
def start():
    introduction()
    
    duck_shooting()
    
    
start()

#use of required numerical operators
num = int(input("pick a number that you want to be put to the power of 7, divided by 6 and added to 750"))
num = num ** 7 / 6 + 750
print("result:",num)
sqr_num = int(input("If you want just the whole number type 1 \nIf you want just the remainder then type 2"))
if(sqr_num == 1):
    print("Heres the Whole side:" ,num // 1)
else:
    print("Heres the remainder:", num % 1)

#more needed things
def get_quadratic(a,b):
    s = a**2 + b**2
    return s

# needed while function?
s = 0
q = int(input("try and find a number that when squared and addde to 6 squared will return 40: "))
while s != 40:
    get_quadratic(q,6)

#duck Points
#duck1 = 500
#duck2 = 1000
#duck3 = 5000
#duck4 = -3000

#some kind of feature that if you hit ducks without missing you get a bonus
#combo1 = score//50
#combo = score + combo1
#print(combo)

#maybe a upgrade shop
#print("Upgrade Shop")
#item1 = 100
#item2 = 500
#item3 = 1000
#item4 = 5000
#item5 = 10000
#if(score >= input)
  #  print("Purchased"), score = (score - input))
#print(item1 <= score)
#print(item2 <= score)
#print(item3 <= score)
#print(item4 <= score)
#print(item5 <= score)

#print("Score:"+("{:08d}".format(score))) #so the score ends in the proper format

