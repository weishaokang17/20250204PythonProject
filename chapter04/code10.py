import random

lst=[item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)

# 上面的，因为前面要用到item，下面的，因为for循环里面的每个元素，都用不到，仅需要用到循环此时，就用了 _
lst=[random.randint(1,100) for _ in range(10)]
print(lst)

# 从列表中选择符合条件的元素组成新的列表
lst=[i for i in range(10) if i%2==0]
print(lst)