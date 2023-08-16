# 安装
# 同其它的Python第三方库一样，PySpark同样可以使用pip程序进行安装。
# 在”CMD”命令提示符程序内，输入：
# pip install pyspark
# 或使用国内代理镜像网站（清华大学源）
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspark
# Installing collected packages: py4j, pyspark
# Successfully installed py4j-0.10.9.7 pyspark-3.4.1

# 构建PySpark执行环境入口对象
# 想要使用PySpark库完成数据处理，首先需要构建一个执行环境入口对象。
# PySpark的执行环境入口对象是：类 SparkContext 的类对象
# 导包
from pyspark import SparkConf,SparkContext
# 创建sparkconf类对象
conf =SparkConf().setMaster("local[*]").setAppName("test_spark")
# 基于sparkconf类对象创建sparkcontext
sc=SparkContext(conf=conf)
# 打印pyspark运行版本
print(sc.version)
sc.stop()
# 编程模型
# SparkContext类对象，是PySpark编程中一切功能的入口。
# PySpark的编程，主要分为如下三大步骤：
# 数据输入  数据计算  数据输出
