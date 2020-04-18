"""Integration Project of the game Duck Hunt where you shoot birds to gain
points """
__author__ = "Andrew Wilhelm"

import random


def introduction():
    """
    This Function, introduction, introduces the game and what its all
    """
    intro_answer = input("Would you like to play a game? \nType yes or no? \n")
    if intro_answer == "yes":
        print("Welcome to Duck Hunt Where you hunt ducks")
    elif intro_answer == "no":
        print("Welcome to Duck Hunt Any Way!")
    else:
        print("Incorrect input. Please answer by typing yes or no")
        introduction()


def chance_hit():
    """
    This function adds the chance that you can hit or miss the duck
    :return: It returns the value hit that has 1 has a hit and 0 as a miss
    """
    rand_num = random.randint(1, 14)
    if rand_num >= random.randint(1, 5):
        hit = 1
    else:
        hit = 0
    return hit


def dogs():
    """
    The function dogs is used to find out what kind of dog names do people
    like to go hunting with
    """
    print("Please give 3 dogs you want to going hunting with names")
    for x in range(3):
        d = str(input())
        x += 1
        print("dog name:" + d)
    print("What wonderful choices of dogs")


def play_again(s):
    """
    play_again gives the option to play the game again or not and gives you
    your final score :param s:
    """
    again = input("Do you want to play again? \ntype yes or no \n")
    if again == 'yes':
        duck_shooting1()
    elif again == 'no':
        print("Your final score was:", s, " \nGoodbye, have a nice life")
    else:
        print("Incorrect input. Please start from the beginning")
        introduction()


def start():
    """
    #start function runs all other function in order for the program to run
    properly
    """
    introduction()
    score = duck_shooting1()
    dogs()
    play_again(score)


def duck_shooting1():
    """
    This function, duck_shooting1, prompts the user to pick a duck to shoot 3
    times and uses the function chance_hit to determine it they were
    successful in shooting the duck.
    :return: It returns the score so that it may be used later to see the
    final score
    """
    score = 0
    duck = input("Do you want to shoot duck 1 2 3 or 4 \n")
    if duck == '1':
        if chance_hit() == 1:
            print("good job you got 500 points")
            score += 500
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '2':
        if chance_hit() == 1:
            print("good job you got 1000 points")
            score += 1000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '3':
        if chance_hit() == 1:
            print("good job you got 5000 points")
            score += 5000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '4':
        if chance_hit() == 1:
            print("good job you got 3000 points")
            score += 3000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    else:
        print(
            "That is not a duck you silly Goose. Now you have to start over!")
        start()
    duck = input("Do you want to shoot duck 1 2 3 or 4 \n")
    if duck == '1':
        if chance_hit() == 1:
            print("good job you got 500 points")
            score += 500
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '2':
        if chance_hit() == 1:
            print("good job you got 1000 points")
            score += 1000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '3':
        if chance_hit() == 1:
            print("good job you got 5000 points")
            score += 5000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '4':
        if chance_hit() == 1:
            print("good job you got 3000 points")
            score += 3000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    else:
        print(
            "That is not a duck you silly Goose. Now you have to start over!")
        start()
    duck = input("Do you want to shoot duck 1 2 3 or 4 \n")
    if duck == '1':
        if chance_hit() == 1:
            print("good job you got 500 points")
            score += 500
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '2':
        if chance_hit() == 1:
            print("good job you got 1000 points")
            score += 1000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '3':
        if chance_hit() == 1:
            print("good job you got 5000 points")
            score += 5000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    elif duck == '4':
        if chance_hit() == 1:
            print("good job you got 3000 points")
            score += 3000
            print("Score:" + ("{:08d}".format(score)))
        else:
            print("Dang, you missed")
            print("Score:" + ("{:08d}".format(score)))
    else:
        print(
            "That is not a duck you silly Goose. Now you have to start over!")
        start()
    return score


start()
