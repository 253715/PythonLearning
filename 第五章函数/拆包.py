# 什么是拆包
# 拆包: 对于函数中的多个返回数据,
# 去掉元组, 列表 或者字典直接获取里面数据的过程。
# ☆ 拆包tuple元组：
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)  # 100
print(num2)  # 200

# ☆ 拆包dict字典
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1

# 对字典进行拆包，取出来的是字典的key
print(a)  # name
print(b)  # age

print(dict1[a])  # TOM
print(dict1[b])  # 18

# 案例：交换两个变量的值
# 方法一 引入中间变量
num1 = 10
num2 = 20

temp = num1
num1 = num2
num2 = temp

print(num1)
print(num2)

# 方法二 基于拆包
num1 = 10
num2 = 20

num1, num2 = num2, num1

print(num1)
print(num2)

# 引用变量与可变、非可变类型
# 值传递与引用传递
# 在python中，值是靠引用来传递来的。
# 我们可以用id() 来判断两个变量是否为同一个值的引用。
# 我们可以将id值理解为那块内存的地址标识。
a = 1
b = a

print(b)  # 1

print(id(a))  # 140708464157520
print(id(b))  # 140708464157520

a = 2
print(b)  # 1,说明int类型为不可变类型

print(id(a))  # 140708464157552，此时得到的是数据2的内存地址
print(id(b))  # 140708464157520

# 列表序列
aa = [10, 20]
bb = aa

print(id(aa))  # 2325297783432
print(id(bb))  # 2325297783432


aa.append(30)
# bb会随着aa的改变也改变
print(bb)  # [10, 20, 30], 列表为可变类型

print(id(aa))  # 2325297783432
print(id(bb))  # 2325297783432

# 可变与不可变类型的总结
# 所谓可变类型与不可变类型是指：
# 数据能够直接进行修改，如果能直接修改那么就是可变，否则是不可变。
# 可变类型
# 列表
# 字典
# 集合
# 不可变类型
# 整型
# 浮点型
# 字符串
# 元组
