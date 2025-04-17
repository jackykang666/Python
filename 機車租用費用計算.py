class Transport:
    def compute_time(self, time):
        return max(0, time - 6)

    def compute_price(self):
        pass


class Wemo(Transport):
    def compute_price(self, time, age):
        extra_time = self.compute_time(time)
        if age <= 24:
            price = 9 + extra_time * 1.5
        else:
            price = 15 + extra_time * 2.5
        return price


class Goshare(Transport):
    def compute_price(self, time, motorcycle_type):
        extra_time = self.compute_time(time)
        if motorcycle_type.lower() == "viva":
            price = 15 + extra_time * 2.5
        elif motorcycle_type.lower() == "gogoro2":
            price = 25 + extra_time * 2.5
        else:
            raise ValueError("未知的車型")
        return price


while True:
    try:
        time = int(input("\n請輸入預計使用時間(分鐘)："))
        vehicle = input("您想使用哪款機車? 'Wemo' 或 'Goshare'：").strip().lower()

        if vehicle == "wemo":
            age = int(input("你現在幾歲?："))
            wemo = Wemo()
            price = wemo.compute_price(time, age)
        elif vehicle == "goshare":
            moto_type = input("你想騎那款 Gogoro? 'Viva' 或 'Gogoro2'：").strip()
            goshare = Goshare()
            price = goshare.compute_price(time, moto_type)
        else:
            print("輸入錯誤，請輸入 'Wemo' 或 'Goshare'")
            continue

        print(f"所需費用：{price:.1f}")

        cont = input("繼續玩嗎？若想繼續玩，請按 'y' 或 'Y'：").strip().lower()
        if cont != 'y':
            print("程式結束，感謝使用！")
            break
    except Exception as e:
        print("發生錯誤：", e)
        continue
