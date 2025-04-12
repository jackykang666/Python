s = input("請輸入溫度: ").strip()
#加入 strip() 移除使用者輸入的前後空白。

if s.count('.') > 1:
    print('只能有一個小數點')
elif s.lstrip('-').replace('.', '').isdigit():
    temp = float(s)
    print(f'攝氏 {temp} 度等於華氏 {(temp * 9 / 5) + 32:+5.1f} 度')
    print(f'華氏 {temp} 度等於攝氏 {(temp - 32) * 5 / 9:+5.1f} 度')
else:
    print("輸入的溫度無法轉換！")


#原程式中 s[1:].replace('.', '').isdigit() 會錯誤地跳過單位數整數。
#現在改為 s.lstrip('-').replace('.', '').isdigit()，正確處理負數和整數。