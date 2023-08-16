
# 赋值运算符
# 单个运算符
a=10
# 多个运算符
a=b=11
# 打印
print(a,b)
# 复合运算符
# =+  -+ *+
# 比较运算符
# == ！= > < >= <=
# 逻辑运算符  and or not
# 短路运算
a=1
b=2
c=3
# true  这里是同时成立  直接true
print((a<b)and(b<c))
# a>b  a>b就是错误的  后面的就不运算了  直接false
print((a>b)and(b<c))
# true
print((a>b)or (b<c))
print(not(a>b))
# if语句