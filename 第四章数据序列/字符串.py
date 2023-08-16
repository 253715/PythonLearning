
# 字符串
# 字符串是 Python 中最常用的数据类型。
# 我们一般使用引号来创建字符串。创建字符串很简单，只要为变量分配一个值即可。
a = 'hello world'
b = "abcdefg"
print(type(a))
print(type(b))

name3 = ''' Tom '''
name4 = """ Rose """
# 注意：三引号形式的字符串支持换行
a = '''I am Tom, 
        nice to meet you! '''

b = """ I am Rose, 
        nice to meet you! """
print(a,b)

# 字符串的输入
# 在Python中，使用input()接收用户输入。
# username = input('请输入您的名字：')
# 字符串的输出
# print(f'您输入的名字是{username}')
# print(type(username))
#
# password = input('请输入您的密码：')
# print(f'您输入的密码是{password}')
# print(type(password))
# 字符串底层逻辑 索引下标从0开始
# 由于一个个字符组成

# 1.字符串切片
# 切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
# 序列[开始位置下标:结束位置下标:步长]
# ① 不包含结束位置下标对应的数据， 正负整数均可；
# ② 步长是选取间隔，正负整数均可，默认步长为1。
# 2.切片的使用
# 只顾头来尾不管，步长为正正向移，步长为负则逆向移
print("=================================")
name='abcdefg'
print(name[2:5:1])
print(name[2:5])
print(name[:5])
print(name[1:])
print(name[:])
print(name[::2])
# -1表示从最后一个数开始
print(name[:-1])
# -1表示从最后一个数开始
print(name[:-4:-1])
print("============================================")
# 3.常用方法
# 3.1 查找
# 所谓字符串查找方法即是查找子串在字符串中的位置或出现的次数。
# find()：检测某个子串是否包含在这个字符串中，
# 如果在返回这个子串开始的位置下标，否则则返回-1。
# 字符串序列.find(子串, 开始位置下标, 结束位置下标)
# 开始和结束位置下标可以省略，表示在整个字符串序列中查找。
mystr = "hello world and hello python"
print(mystr.find('hello'))
print(mystr.find('hello', 10, 27))
# # 如果在返回这个子串开始的位置下标，否则则返回-1。
print(mystr.find('heima'))  # -1

# index()：检测某个子串是否包含在这个字符串中，
# 如果在返回这个子串开始的位置下标，否则则报异常。
mystr = "hello world and hello python"
print(mystr.index('hello'))
print(mystr.index('hello', 10, 27))
# 如果在返回这个子串开始的位置下标，否则则报异常
# print(mystr.index('heima'))  # 报错
print("=====================================")
# rfind()： 和find()功能相同，但查找方向为右侧开始。
# rindex()：和index()功能相同，但查找方向为右侧开始
# count()：返回某个子串在字符串中出现的次数
# 3.2 字符串修改
# 所谓修改字符串，指的就是通过函数的形式修改字符串中的数据。
# 3.2.1 replace()：返回替换后的字符串
# 字符串序列.replace(旧子串, 新子串, 替换次数)
# 注意：替换次数如果查出子串出现次数，则替换次数为该子串出现次数。
mystr = "hello world and hello python"
# 结果：hello world & hello python
print(mystr.replace('and', '&'))
# 结果：hi world and hi python  2表示替换2次
print(mystr.replace('hello', 'hi', 2))
# 结果：hello world and hello python
# 数据按照是否能直接修改分为可变类型和不可变类型两种。
# 由于字符串属于不可变类型，所以修改的时候不能改变原有字符串
# 打印还是原来的结果就说明，字符串就是不可变类型
print(mystr)
print("=======================================")
# 3.2.2 split()：按照指定字符分割字符串
# 字符串序列.split(分割字符, num)
# 注意：num表示的是分割字符出现的次数，
# 即将来返回数据个数为num+1个。
mystr = 'apple,orange,banana'
# 结果：['apple', 'orange', 'banana']
print(mystr.split(','))
# 结果：['apple', 'orange,banana']  1表示分割一次  也就是最后返回两个
print(mystr.split(',', 1))
# 结果：['apple,orange,banana']
print(mystr.split('*'))
print("=====================================")
# 3.2.3 join()：合并字符串
# 用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串。
list1 = ['it', 'heima']
tuple1 = ('hello', 'python')
# 结果：itheima  中间使用空格
print(''.join(list1))
# 结果：hello-python
print('-'.join(tuple1))
print('==========================')
# capitalize()：将字符串第一个字符转换成大写
# 注意：capitalize()函数转换后，
# 只字符串第一个字符大写，其他的字符全都小写。
mystr = 'student'
# 结果：Studentprint(mystr.capitalize())
print('==========================')
# title()：将字符串每个单词首字母转换成大写
# upper()：将字符串中小写转大写
# lower()：将字符串中大写转小写
print('==========================')
# lstrip()：删除字符串左侧空白字符
# rstrip()：删除字符串右侧空白字符
# strip()：删除字符串两侧空白字符。
print('==========================')
# ljust()：返回一个原字符串左对齐,
# 并使用指定字符(默认空格)填充至对应长度 的新字符串。
# rjust()：返回一个原字符串右对齐,
# 并使用指定字符(默认空格)填充至对应长度 的新字符串，语法和ljust()相同。
# center()：返回一个原字符串居中对齐,
# 并使用指定字符(默认空格)填充至对应长度的新字符串，语法和ljust()相同
mystr = "python"
print(mystr.ljust(10, '.'))
print('-' * 10)
print(mystr.rjust(10, '.'))
print('-' * 10)
print(mystr.center(10, '.'))
# 字符串判断
# 所谓判断即是判断真假，返回的结果是布尔型数据类型：True 或 False。
# startswith()：检查字符串是否是以指定子串开头，
# 是则返回 True，否则返回 False。如果设置开始和结束位置下标，
# 则在指定范围内检查。
# endswith()：检查字符串是否是以指定子串结尾，是则返回 True，
# 否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
mystr1 = 'python program'
# 表示是不是以某个字符串开头
print(mystr1.startswith('python'))
print('-' * 10)
mystr2 = 'avater.png'
# 表示是不是以某个字符串结尾
print(mystr2.endswith('.png'))
print("========================================")
# isalpha()：
# 测字符串是否只由字母组成，
# 如果字符串所有字符（至少有一个字符）都是字母则返回 True, 否则返回 False。
mystr1 = 'hello'
mystr2 = 'hello12345'
# 结果：True
print(mystr1.isalpha())
# 结果：False
print(mystr2.isalpha())
print("========================================")
# isdigit()：如果字符串只包含数字则返回 True 否则返回 False。
mystr1 = 'aaa12345'
mystr2 = '12345'
# 结果： False
print(mystr1.isdigit())
# 结果：False
print(mystr2.isdigit())

# isalnum()：检测字符串是否由字母和数字组成，
# 如果字符串所有字符都是字母或数字（至少有一个字符）
# 则返 回 True,否则返回 False。

# isspace()：如果字符串中只包含空白，则返回 True，否则返回 False。
