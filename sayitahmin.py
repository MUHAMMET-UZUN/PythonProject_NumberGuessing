import matplotlib as plt
import random

num = random.randint(1,10)
count = 0
user_value = 0

while (True):
    user_value = input("Guess number: ")
    count += 1

    if(user_value == "exit"):
        print("Left game")
        break
    user_value = int(user_value)
    if(user_value > num):
        print("You can guess a smaller number")

    elif(user_value < num):
        print("You can guess a bigger number")

    else:
        print("\nFOUND! Well Done...")
        print(str(count)+" guesses")
        break
