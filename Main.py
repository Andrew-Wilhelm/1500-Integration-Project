#Andrew Wilhelm
#My Intergration Project
#duck hunt THE GAME
#dammage counter
#combo counter

print("Would you like to play a game? \nType yes or no")
intro_answer = input()
if intro_answer == "yes":
    print("Welcome to Duck Hunt")
else:
    print("Welcome to Duck Hunt Any Way!"*10)

print("Do you want to shoot duck 1 2 3 or 4?")
duck = int(input())
score = 0
if duck == 1:
    print("good job you got 500 points")
    score += (500)
elif duck == 2:
    print("good job you got 1000 points")
    score += (1000)
elif duck == 3:
    print("good job you got 1000 points")
    score += (5000)
elif duck == 4:
    print("good job you got 1000 points")
    score -= (3000)
else:
    print("That is not a duck you silly Goose")


print("Score:"+("{:08d}".format(score)))

#use of required numerical operators
print("pick a number that you want to be put to the power of 7, divided by 6 and added to 750")
num = int(input())
num = num ** 7 / 6 + 750
print("result:",num)
print("If you want just the whole number type 1 \nIf you want just the remainder then type 2")
sqr_num = int(input())
if(sqr_num == 1):
    print("Heres the Whole side:" ,num // 1)
else:
    print("Heres the remainder:", num % 1)
    
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

print("Thats all there is, no more to do")
