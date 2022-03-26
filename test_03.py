import random

one = True
two = True
while one:
    print("开始")
    while two:
        num = str(input("请输入中心、音乐块、微信支付块："))
        if num == "中心":
            print("30分")
            continue
        elif num == "音乐块":
            print("20分")
            continue
        if num == "微信支付块":
            print("50分")
            continue
        elif num == "0":
            one = False
            break