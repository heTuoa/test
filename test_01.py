while True:
    print("查询能量，退出0")
    print("能力来源如下")
    print("生活缴费、行走捐、共享单车、线下支付、网络购票")
    inp = str(input("请输入"))
    if inp == "0":
        print("退出成功")
        break
    if inp == "行走捐":
        print("200g")
    elif inp == "生活缴费":
        print("40g")
    elif inp == "共享单车":
        print("30g")
    elif inp == "线下支付":
        print("10g")
    elif inp == "网络购票":
        print("150g")

