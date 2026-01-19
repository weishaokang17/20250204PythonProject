t=(i for i in range(1,4))
print(t) # 这一行，输出可迭代对象

s=tuple(t) # 这一行，把t这个可迭代对象，转换为元组
print(s)
# 遍历1
for item in s:
    print(item)

for index,j in enumerate(s):
    print(index,j)

print('-' * 90)


t2=(i for i in range(1,9))

# s2 = tuple(t2)  一旦把t2这个可迭代对象，转换成了元组，t2这个可迭代对象就
# 已经被使用了，后面的__next__()方法会报错

print(t2.__next__())
print(t2.__next__())
print(t2.__next__())

t=tuple(t2)
print(t)