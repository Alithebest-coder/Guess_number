import random
number=random.randint(1,200)
play="yes"
while play=="yes":
    print("guess the number in this game to WIN!")
    if number%2==0: 
        print("it is even")
    else:
        print("or it is odd")
    guess=int(input("give a number from 1 to 200:       "))
    try:
        if guess >=1 and guess <=200:
            if guess<number:
                print("It is too low!")
            if guess>number: 
                print("It is too high!")
            if guess!=number:
                print("try again!")
            if guess==number:
                print("YOU WON!!!!")
                break
    except:
        print("enter the number to 1 and 200")