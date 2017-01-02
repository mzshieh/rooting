# 讀入一個整數
# 不是整數的，就反覆到是整數為止
# 顯示 msg 作為提示
def input_int(msg):
    # 把要傳回的資料存在 ret
    ret = input(msg)
    while type(ret) != type(0):
        try: # try to convert ret into int
            ret = int(ret)
        except: # conversion failed: ask user again
            ret = input(msg)
    return ret

a = input_int('請輸入一個正整數')
while a <= 0:
    a = input_int('請輸入一個正整數')
