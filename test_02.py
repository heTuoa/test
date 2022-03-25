import random

while 1:
    print("开始")
    gusss = random.randint(1, 10)
    print(gusss)
    while 1:
        num = int(input("请输入1-10的数字："))
        if num < 1:
            print("数字太小")
        elif num > 10:
            print("数字太大")
        if num == gusss:
            print("恭喜猜对")
            print("结束")
            break
        elif num != gusss:
            print("错了，重来")
            continue