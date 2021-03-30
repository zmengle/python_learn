# 使用dict
dict1 = {'a': 100, 'b': 10}

dict1['c'] = 1000
dict1['c'] = 10000
print(dict1)

print('f' in dict1, 'a' in dict1)

print(dict1.get('c', 0), dict1.get('g', 0))

dict1.pop('c')

print(dict1)

# dict查询快 但是耗内存
# list查询慢 不耗内存

# 使用set(list)  key唯一，set和dict的唯一区别仅在于没有存储对应的value
set1 = ([1, 2, 4])
print(set1)

set1.__add__(12)
