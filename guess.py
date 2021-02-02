import random

r = random.randint(1,100)
count = 0
while True:
    count += 1
    guess = int(input("請猜一個數字:"))
    if guess == r:
        print("你猜對了。")
        print(f"總共猜了{count}次")
        break
    elif guess > r :
        print("再小一點")
        print(f"總共猜了{count}次")
    elif guess < r :
        print("再大一點")
        print(f"總共猜了{count}次")