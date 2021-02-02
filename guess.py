import random

r = random.randint(1,100)

while True:
    guess = int(input("請猜一個數字:"))
    if guess == r:
        print("你猜對了。")
        break
    elif guess > r :
        print("再小一點")
    elif guess < r :
        print("再大一點")