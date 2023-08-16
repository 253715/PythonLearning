# 1、为什么需要字典
# 思考1： 如果有多个数据，例如：'Tom', '男', 20，如何快速存储？
# 答：列表
list1 = ['Tom', '男', 20]
# 可以通过下标来访问到数据
# 思考3：如果将来数据顺序发生变化，如下所示，还能用`list1[0]`访问到数据'Tom'吗？
# 不能
# 思考4：数据顺序发生变化，每个数据的下标也会随之变化，
# 如何保证数据顺序变化前后能使用同一的标准查找数据呢？
# 答：字典，字典里面的数据是以键值对形式出现，字典数据和数据顺序没有关系，即字典不支持下标
# ，后期无论数据如何变化，只需要按照对应的键的名字查找数据即可。
# 定义
# 字典特点：
# 符号为大括号（花括号）
# 数据为键值对形式出现
# 各个键值对之间用逗号隔开
# 字典是可变类型
# 基本语法：
# 有数据字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 空字典
dict2 = {}
dict3 = dict()
# {'name': 'Tom', 'age': 20, 'gender': 'male'}
print(dict1)
print(type(dict2))
print(type(dict3))
print('=================================')
# 增加
# 字典序列[key] = value
# 注：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
dict1['name'] = 'Rose'
# 结果：{'name': 'Rose', 'age': 20, 'gender': 'male'}
print(dict1)
dict1['id'] = 110
# {'name': 'Rose', 'age': 20, 'gender': 'male', 'id': 110}
print(dict1)
print('=================================')

# 字典的"删"操作
# del() / del：删除字典或删除字典中指定键值对
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 根据key来进行删除
del dict1['gender']
# {'name': 'Tom', 'age': 20}
print(dict1)
print('=================================')
# clear() 表示清空字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
dict1.clear()
print(dict1)  # {}

# 字典的"改"操作
# 字典序列[key] = value

# 字典的"查"操作
# 1.key值查找
# dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 如果当前查找的key存在，则返回对应的值；否则则报错
# print(dict1['id'])         # 报错
# 根据key查询
# print(dict1['name'])  # Tom
# 1	get(key, 默认值)	根据字典的key获取对应的value值，
# 如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回None
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}

print(dict1.get('name'))    # Tom
# id没有 于是就返回110
print(dict1.get('id', 110))  # 110
# id没有 也没有第二个参数
print(dict1.get('id'))  # None

# 2	keys()	以列表返回一个字典所有的键

dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 结果：dict_keys(['name', 'age', 'gender'])
print(dict1.keys())

# 3	values()	以列表返回字典中的所有值
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 结果：dict_keys(['Tom', 20, 'male'])
print(dict1.values())

# 4	items()	以列表返回可遍历的(键, 值) 元组数组
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 结果：dict_items([('name', 'Tom'), ('age', 20), ('gender', 'male')])
print(dict1.items())
print("==========================")
# {'name': 'Tom', 'age': 20, 'gender': 'male'}
print(dict1)



