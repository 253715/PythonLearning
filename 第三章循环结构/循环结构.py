
# while
# 初始条件
i=0
# 循环条件
while i<5:
    # 循环体
    print("zrk")
    # 计数器
    i+=1
print("结束")

# 求累计和
i=1
result=0
while i<=100:
    result=result+i
    i+=1
print(result)
# 循环中的两个关键词  break continue
i = 1
while i <= 5:
    if i == 4:
        print(f'吃饱了不吃了')
        # 这里就停止了 下面的不执行了
        break
    print(f'吃了第{i}个苹果')
    i += 1
print("==============================")
i = 1
while i <= 5:
    if i == 3:
        print(f'大虫子，第{i}个不吃了')
        # 在continue之前一定要修改计数器，否则会陷入死循环
        i += 1
        # 这里只是推出3这一次  其他的还是执行
        continue
    print(f'吃了第{i}个苹果')
    i += 1

# 死循环
# while True:
#     print('你是风儿我是沙，缠缠绵绵到天涯…')

# while循环嵌套
j = 0
while j < 3:
    i = 0
    while i < 3:
        print('老婆大人，我错了')
        i += 1
    print('刷晚饭的碗')
    print('一套惩罚结束----------------')
    j += 1
# for循环结构
str1 = 'itheima'
# i 临时标量 str1 表示序列
for i in str1:
    print(i)
print("======================")
# range() 函数返回的是列表，而在Python3中
# range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型，
# 所以打印的时候不会打印列表。（由于我们还未学习面向对象，
# 为了方便大家理解，你可以简单的将其理解为一个序列结构
for i in range(5):
    print(i)
# 步长为5 [0, 5, 10, 15, 20, 25]  左闭右开
print(list(range(0,30,5)))
# [0, 2, 4, 6, 8]
print(list(range(0,10,2)))

# for循环两大关键词  break continue
# for 循环嵌套
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={j*i}', end='\t')
    print('')


# while else 结构
# 循环可以和else配合使用，
# else下方缩进的代码指的是当循环正常结束之后要执行的代码
print("=================================")
i = 0
while i < 5:
    print('老婆大人，我错了')
    i += 1
else:
    print('老婆大人原谅我了，真开心，哈哈...')

# for循环else结构
# 所谓else指的是循环正常结束之后要执行的代码，
# 即如果是break终止循环的情况，else下方缩进的代码将不执行。
print("===================================")
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束之后执行的代码')

print("===================================")
str1 = 'itheima'
for i in str1:
    print(i)
print('循环正常结束之后执行的代码')