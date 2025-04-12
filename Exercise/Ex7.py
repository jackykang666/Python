def temperature():
    s = input("請輸入溫度: ").strip()

    try:
        if s.count('.') > 1:
            raise ValueError("只能有一個小數點")

        if not s.lstrip('-').replace('.', '').isdigit():
            raise ValueError("輸入的溫度無法轉換！")
        
        temp = float(s)
        print(f'攝氏 {temp} 度等於華氏 {(temp * 9 / 5) + 32:+5.1f} 度')
        print(f'華氏 {temp} 度等於攝氏 {(temp - 32) * 5 / 9:+5.1f} 度')
    
    except ValueError as e:
        print(e)

# 測試函式
temperature()


#封裝函數：將轉換邏輯放入 convert_temperature()，方便重用。
#使用 try-except：捕獲輸入錯誤，避免非數字或錯誤格式導致程式崩潰。
#                自訂錯誤訊息，提升可讀性。
#raise ValueError()：當輸入格式錯誤時，主動拋出異常，讓 except 處理。