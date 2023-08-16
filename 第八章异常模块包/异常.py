# 什么是异常
# 当检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的"异常"。
# 例如：以`r`方式打开一个不存在的文件。
# f = open('linux.txt', 'r')
# 就会出现异常
# Traceback (most recent call last):
#   File "C:\Users\Administrator\PycharmProjects\pythonProject2\第八章异常模块包\异常.py",
#   line 4, in <module>
#     f = open('linux.txt', 'r')
#         ^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'linux.txt'

# 异常的捕获方法
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码
try:
    # 尝试使用只读的方式打开文件
    f = open('linux.txt', 'r')
except:
    # 如果出现异常 使用可以写的方式打开异常
    f = open('linux.txt', 'w')
#     捕获指定异常
try:
    print(name)
except NameError:
    # name变量名称未定义错误
    print('name变量名称未定义错误')
# ① 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
# ② 一般try下方只放一行尝试执行的代码。
# 捕获多个异常
# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except 后，并使用元组的方式进行书写。
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('ZeroDivision错误...')
# 捕获异常并输出描述信息
try:
    print(num)
except (NameError, ZeroDivisionError) as e:
    # name 'num' is not defined  e就是表示异常的描述信息
    print(e)
#     捕获所有异常
try:
    print(name)
#     exception 直接捕获所有异常
except Exception as e:
    print(e)
# 异常else
# else表示的是如果没有异常要执行的代码。
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常的时候执行的代码')
# 异常的finally
# finally表示的是无论是否异常都要执行的代码，例如关闭文件。
try:
    # 尝试执行
    f = open('test.txt', 'r')
except Exception as e:
    # 返回异常信息
    f = open('test.txt', 'w')
else:
    # 没有异常要执行的
    print('没有异常，真开心')
finally:
    # 无论无何都要执行的代码
    f.close()
