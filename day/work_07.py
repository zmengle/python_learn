'''
Descripttion: Created by VsCode.
User: lionzhang
Date: 2021-05-10 12:46:10
Time: Do not edit
'''
# 打印出1000以内所有的“水仙花数”，
# 所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

#水仙花数计算 最多支持三位数
def myCount(n):
    tmp, tmp1, tmp2, tmp3 = 0, 0, 0, 0
    if n > 99:
        tmp1 = n // 100
    if n > 9:
        tmp2 = n % 100 // 10
    if n > 0:
        tmp3 = n % 10
    tmp = tmp1 ** 3 + tmp2 ** 3 + tmp3 ** 3
    # print(tmp, tmp1, tmp2, tmp3)
    if tmp == n:
        return n
    else:
        return False
#初始化列表
myList = []
#遍历
for n in range(100, 999):
    if not n:
        break
    tmp = myCount(n)
    if tmp:
        myList.append(tmp)
    n -= 1
#输出
print(myList)