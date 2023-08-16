# 思考：有一个人的姓名(TOM)怎么书写存储程序？
# 答：变量。
# 如果一个班级100位学生，每个人的姓名都要存储，应该如何书写程序？声明100个变量吗？
# 答：No，我们使用列表就可以了， 列表一次可以存储多个数据。
#  列表是可变类型
name_list =['Tom','Lily','Rose']
# 注意：列表可以一次存储多个数据且可以为不同的数据类型
print(name_list)
# 打印类型
print(type(name_list))
print('================================')
# 列表的常用操作
# 列表的作用是一次性存储多个数据，
# 程序员可以对这些数据进行的操作有：增、删、改、查
# 1. 查询
name_list = ['Tom', 'Lily', 'Rose']
# 使用下标查询
print(name_list[0])  # Tom
print(name_list[1])  # Lily
print(name_list[2])  # Rose

# index()方法：指定数据所在位置的下标
# 列表序列.index(数据, 开始位置下标, 结束位置下标)
name_list = ['Tom', 'Lily', 'Rose']
# 指定的是数据所在位置的下标
print(name_list.index('Lily', 0, 2))  # 1
print('=======================================')
# count()方法：统计指定数据在当前列表中出现的次数
name_list = ['Tom', 'Lily', 'Rose']
# 指定的是数据所在位置的下标
print(name_list.count('Lily'))  # 1
print('=======================================')
# in：判断指定数据在某个列表序列，如果在返回True，否则返回False
# not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False

# 2.增加
# append()方法：增加指定数据到列表中
name_list = ['Tom', 'Lily', 'Rose']
name_list.append('Jennifer')
# ['Tom', 'Lily', 'Rose', 'Jennifer']
# 直接作为一个整体添加
# 列表是可变类型
print(name_list)
# extend()方法：
# 列表结尾追加数据，
# 如果数据是一个序列，则将这个序列的数据逐一添加到列表
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend('Smith')
# 结果：['Tom', 'Lily', 'Rose', 'S', 'm', 'i', 't', 'h']
# 一个一个字符进行添加
print(name_list)

# insert()方法：指定位置新增数据
name_list = ['Tom', 'Lily', 'Rose']
# 这里表示在下标为1的地方添加数据
name_list.insert(1, 'Smith')
# 结果：['Tom', 'Smith', 'Lily', 'Rose']
print(name_list)

# 删除
# del：删除列表中的某个元素
name_list = ['Tom', 'Lily', 'Rose']
del name_list[0]
print(name_list)

# pop()方法：删除指定下标的数据(默认为最后一个)，并返回该数据。
name_list = ['Tom', 'Lily', 'Rose']
# 可以返回删除的数据
del_name = name_list.pop(1)
# 结果：Lily
print(del_name)
# 结果：['Tom', 'Rose']
print(name_list)

# remove()方法：移除列表中某个数据的第一个匹配项。
name_list = ['Tom', 'Lily', 'Rose']
name_list.remove('Rose')
# 结果：['Tom', 'Lily']
print(name_list)
print('===========================')
name_list1 = ['Tom', 'Lily', 'Rose','Rose','Rose']
name_list1.remove('Rose')
# ['Tom', 'Lily', 'Rose', 'Rose']
# 只是删掉第一个
print(name_list1)
# clear()方法：清空列表，删除列表中的所有元素，返回空列表。
print('===========================')

# 修改
# reverse()：将数据序列进行倒叙排列
num_list = [1, 5, 2, 3, 6, 8]
num_list.reverse()
# 结果：[8, 6, 3, 2, 5, 1]
print(num_list)
# sort()方法：对列表序列进行排序
# 列表序列.sort( key=None, reverse=False)
# 注意：reverse表示排序规则，reverse = True降序，
# reverse = False升序（默认）
num_list = [1, 5, 2, 3, 6, 8]

num_list.sort()
print(num_list)

# copy()方法：对列表序列进行拷贝
# name_list = ['Tom', 'Lily', 'Rose']
# name_li2 = name_list.copy()
# 结果：['Tom', 'Lily', 'Rose']
# print(name_li2)
print('===========================')

# 循环遍历
# while
name_list = ['Tom', 'Lily', 'Rose']
# 用于计数
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
print('===========================')
# for循环遍历
name_list = ['Tom', 'Lily', 'Rose']
for i in name_list:
    print(i)
print('===========================')
# 列表的嵌套
# 所谓列表嵌套指的就是一个列表里面包含了其他的子列表。
# 应用场景：要存储班级一、二、三三个班级学生姓名，
# 且每个班级的学生姓名在一个列表。
# name_list =
# [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'],
# ['张三', '李四', '王五']]
# 第一步：按下标查找到李四所在的列表
print(name_list[2])
# 第二步：从李四所在的列表里面，再按下标找到数据李四
print(name_list[2][1])
