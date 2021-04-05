#  创建一个空列表，命名为 names，往里面添加 zhangsan、lisi、Jack、Xiuxiu、Peiqi 和 Black 元素，
# 然后在 Black 前面插入一个 Blue，并且把names 列表中 Xiuxiu 的名字改成中文
names = ['zhangsan', 'lisi', 'Jack', 'Xiuxiu', 'Peiqi', 'Black']

names.insert(-1, 'Blue')
print(names)

search_name = 'Xiuxiu'

if search_name in names :
    index = names.index(search_name)
    names[index] = '秀秀'

print(names)