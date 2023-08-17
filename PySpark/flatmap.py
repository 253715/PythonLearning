from pyspark import SparkConf,SparkContext
if __name__ == '__main__':
    # 构建环境
    conf=SparkConf().setAppName("flat_map").setMaster("local[*]")
    sc=SparkContext(conf=conf)
    rdd=sc.parallelize(["a b c","a c e","e c e"])
    print(rdd.flatMap(lambda x: x.split(" ")).collect)
    sc.stop()