import random


random_num = random.randint(0, 100)

x = 0
while True:
    guess = int(input("guess a number "))

    if guess > random_num:
        print("guess lower")
        x += 1

    elif guess < random_num:
        print("guess higher")
        x += 1

    elif guess == random_num:
        print("correct")
        x += 1
        print("It took you", x, "tries!")
        break