# 变量定义

# 字符串
str1 = 'sss\' sdsd\" sdsd'
print(str1)

str2 = '\\n\\t\\b  \\\\'
print(str2)

str3 = r'\\n\\t\\b '

str4 = '''sdfsd
sdsds
sdsd
sdsd'''
print(str4)

# boolean
str5 = True
str6 = False
str7 = None
print(str5, str6, str7)

# 运算符 and|or|not|!|==|!=|>=|<=

# 变量 变量名必须是大小写英文、数字和_的组合，且不能用数字开头

# 使用list
list1 = ['1', '2', '3', '3']
print(list1, len(list1), list1[0], list1[-1])

list1[0] = 5
list1.append(10)
list1.insert(4, 1)
list1.pop()
# list1[4] = 10
list1.insert(10, [1, 2, 3])

print(list1)

# 使用tuple
tuple1 = (1, 2)
print(tuple1)
print((1,))

#tuple 和list st和tuple是Python内置的有序集合，一个可变，一个不可变 (区别是指向不变)
