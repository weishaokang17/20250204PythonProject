#(1)创建字典的方法1，使用大括号直接创建
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) # key相同时，value值进行了覆盖

# (2)zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj) # <zip object at 0x000001ECD5A24F00>

print(list(zipobj)) # [(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]
# 上面这一步，是把zip对象转换成了list，list里面每个元素都是元组

d=dict(zipobj)
print(d) # {}

# 使用参数创建字典
d=dict(cat=10,dog=20) # 左侧cat是key ,右侧的是value
print(d) # {'cat': 10, 'dog': 20}


t=(10,20,30)
print({t:10}) # t是key,10是value ,元组是可以作为字典中的key，因为元组是不可变的

# lst=[10,20,30]
# print({lst:10}) # TypeError: unhashable type: 'list'，
# 列表是可变的，所以列表不能作为字典的key


print('max:',max(d))
print('min:',min(d))
# 上面的max和min，比的是key的大小，先比较两个key的首字母，相同就比较第二个字母......
print('len:',len(d))
# 字典的删除
del d
#print(d)