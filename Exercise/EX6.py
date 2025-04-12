import random

num = random.randint(1, 100)
count = 0

while True:
    s = input('猜出正确数字：') 
    count += 1

    if int(s) > num:
        print('太大了')

    if int(s) < num:
        print('太小了')

    if int(s) == num:
        print('恭喜，猜对了')
        break

print(f'结束，一共猜了{count}次')



