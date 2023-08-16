# 什么是python模块
# Python 模块(Module)，是一个 Python文件，以 .py 结尾，
# 包含了 Python 对象定义和Python语句。
# 模块能定义函数，类和变量，模块里也能包含可执行的代码。

# 模块的导入方式
# import 模块名
# from 模块名 import 功能名
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名

# import模块名
# import 模块名
# import 模块名1，模块名2
#
# 模块名.功能名()
import math
print(math.sqrt(9))  # 3.0

# from 模块名 import 功能名
from os import mkdir
mkdir('images')

# as定义别名
# 模块别名
import time as tt

tt.sleep(2)
print('hello')

# 功能别名
from time import sleep as sl
sl(2)
print('hello')

# 制作自定义模块
# 在Python中，每个Python文件都可以作为一个模块，
# 模块的名字就是文件的名字。也就是说自定义模块名必须要符合标识符命名规则。

# 模块的定位顺序
# 当导入一个模块，Python解析器对模块位置的搜索顺序是：
# 当前目录
# 如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
# 如果都找不到，Python会查看默认路径。UNIX下，
# 默认路径一般为/usr/local/lib/python/
# 模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，
# PYTHONPATH和由安装过程决定的默认目录。
# 注意：
# 自己的文件名不要和已有模块名重复，否则导致模块功能无法使用
# "使用from 模块名 import 功能"的时候，如果功能名字重复，调用到的是最后定义或导入的功能。