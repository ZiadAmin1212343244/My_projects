import random

print("heelo! what's your name?")
name = input()
secret_number = random.randint(1,20)
print('well', name ,'i am thinking of number between 1,20')

for guesstaken in range(1,7):
    print("take a guess")
    guess = int(input())
    if guess < secret_number :
        print("your guess is too low")
    elif guess > secret_number :
        print("your guess is too high ")
    else:
        break


if guess == secret_number:
    print("well that is the number i was thinking of! ")
else:
    print("wrong, the number, i was thinking is" + str(secret_number))
