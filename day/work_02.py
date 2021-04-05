# 根据自己手机号为基数；生成1000个不同的手机号并打印出来。

phone_str = '1551771'
a = 0
for x in range(1000, 2000):
    # print(x)
    phone = phone_str+str(x)
    print(phone)
    a += 1
    print(a)
