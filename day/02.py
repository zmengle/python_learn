# -*- coding: utf-8 -*-
# 字符和编码
a = 66
print(a, chr(a))

b = '中'
print(b, ord(b))

c = '中文'
print(c.encode('utf-8'))

d = b'\xe4\xb8\xad\xe6\x96\x87'
print(d.decode('utf-8', errors='ignore'))

# 注意中英文编码
# 英文可以使用 ASCII
# 中文使用 utf-8 忽略错误编码  errors='ignore'

# 长度计算
print(len(d), len(d.decode('utf-8', errors='ignore')))

# 数据格式方式和C一样
print('%2d %02d' % (1, 1))
print('%.4f' %  1)
print('%x' %  16)
print('%s %s' %  (16, 'name'))
print('%s %%' %  'ssds')

str2 = '{0} xxxx {1:.1f}%'
str2.format('vvv', 16)
print(str2)

r = 1
s = 2.3
str1 = f'sss{r} xxxx{s:.2f}'
print(str1)
