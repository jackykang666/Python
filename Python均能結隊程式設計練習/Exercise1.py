import random

def playgame():
    choices = ["剪刀", "石頭", "布"]

    computer = random.randint(0, 2)

    try:
        user = int(input("請輸入 0（剪刀）、1（石頭）、2（布）："))

        if user not in [0, 1, 2]:
            print("請輸入有效的數字（0、1 或 2）")
            return

        print(f"你出了：{choices[user]}")
        print(f"電腦出了：{choices[computer]}")

        if user == computer:
            print("平手！")
        elif (user == 0 and computer == 2) or \
             (user == 1 and computer == 0) or \
             (user == 2 and computer == 1):
            print("你贏了！🎉")
        else:
            print("你輸了！😢")

    except ValueError:
        print("請輸入數字 0、1 或 2！")

# 執行程式
playgame()
