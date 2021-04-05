# 以空格分隔单词，删除所有重复的单词并按首字母排序后打印这些单词。---考察去重和排序
# 例如：将  hello world  hello xiaoetontong hello python
# 输出为:hello python world xiaoetong

list1 = ['hello', 'world', 'hello', 'xiaoetontong', 'hello', 'python']

list2 = []

for x in list1:
    if x not in list2:
        list2.append(x)

list2.sort()
print(list2)