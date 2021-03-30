# 循环 for
list1 = [1, 2, 3, 4]

for mylist in list1:
    print(mylist)


# 生成序列数
list2 = list(range(10))
print(list2)

list3 = range(10)
print(list3)

a = 10
while True:
    a = a-1
    if not a:
        break
    else:
        print(a)

    if a > 5:
        print(1)
