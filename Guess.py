import random

answer = random.randint(1, 10)

while True:
    guess = int(input("Take your guess: "))
    if guess < answer:
        print("wah! too low")
    elif guess > answer:
            print ("nah son too high")
    elif guess == answer:
            break
print("You got it correct!")