def main():
    try:
        f()
        print("After the function call")
    except IndexError:
        print("Index out of bound")
    except:
        print("Exception in main")

def f():
    try:
        s = "abc"
        print(s[5])
    except ZeroDivisionError:
        print("Dicided by zero")
    except IndexError:
        print("Index out of bound")

# 執行程式
main()


# 輸出結果:Index out of bound
#         After the function call

#說明執行結果的原因:
#def main()這段使用 try-except 結構包住了對 f() 的呼叫，以及一個在函式呼叫後的 print()。
#def f(): 1.s = "abc" 是個字串，長度為 3，索引為 0, 1, 2.print(s[5]) 嘗試存取第 6 個字元（index 為 5），這會觸發 IndexError。 3.該錯誤在 f() 函式內的 except IndexError: 中被捕捉，並印出："Index out of bound"
#因為 f() 自己已經 妥善處理了這個錯誤，所以這個例外 不會再傳回到 main() 的 except 區塊中。程式繼續執行 f() 呼叫之後的 print("After the function call")，所以會接著印出："After the function call"