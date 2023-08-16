# 导包
from pyspark import SparkConf,SparkContext
# 创建sparkconf类对象
conf =SparkConf().setMaster("local[*]").setAppName("test_spark")
# 基于sparkconf类对象创建sparkcontext
sc=SparkContext(conf=conf)
# 将列表转换为rdd
rdd=sc.parallelize([1,2,3,4])
print(rdd.collect())
sc.stop()