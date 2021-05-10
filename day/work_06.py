'''
Descripttion: Created by VsCode.
User: lionzhang
Date: 2021-05-10 12:46:10
Time: Do not edit
'''
# 题目一：
# 输入某年某月某日，判断这一天是这一年的第几天？

month_arr = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
             7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

try:
    year = input("请输入年：")
    year = int(year)
    month = input("请输入月：")
    month = int(month)
    day = input("请输入天：")
    day = int(day)
except ValueError as e:
    exit("时间格式错误，请检查！")
    # exit(e)

if month not in month_arr:
    exit("输入月份错误")
else:
    day_max = month_arr[month]

if day > day_max:
    print("输入天错误")
else:
    pass

# 计算第几天
day_count = 0
for item in month_arr:
    if item != month:
        day_count += month_arr[item]
    else:
        day_count += day
        break

print("日期：%d年%d月%d日 是第%d天" % (year, month, day, day_count))
