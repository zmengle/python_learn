# 两个字典：a={'a':1,'b':2,'c':3} b= {'aa':11,'bb':22,'cc':33}合并为一个list--实现方式有多种，考察dict和list的基本知识
a = {'a': 1, 'b': 2, 'c': 3}
b = {'aa': 11, 'bb': 22, 'cc': 33}

merge_list = []
for x in a:
    merge_list.append(a[x])

for x in b:
    merge_list.append(b[x])

print(merge_list)
