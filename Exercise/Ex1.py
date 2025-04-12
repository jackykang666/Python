import random

def guessAnInt(from_=1, to=100):
    num = random.randint(from_, to)
    count = 0

    while True:
        s = input('猜出正确数字：')
        count += 1

        if int(s) > num:
            print('太大了')

        if int(s) < num:
            print('太小了')

        if int(s) == num:
            print(f'恭喜，猜對了！答案是 {num}')
            break

    print(f'結束，一共猜了 {count} 次')

# 測試函式
guessAnInt(1, 100)