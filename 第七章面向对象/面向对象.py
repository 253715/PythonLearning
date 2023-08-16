# 什么是编程思想

# 所谓的编程思想，就是人们利用计算机来解决实际问题的一种思维方式，
# 常见的编程思想有面向过程和面向对象，很多计算机语言的语法各不相同，
# 但是它们基本的编程思想却是差不多的，
# 而Python是同时支持面向对象和面向过程的编程语言！

# 面向过程
# 传统的面向过程的编程思想总结起来就八个字——自顶向下，逐步细化！
# → 将要实现的功能描述为一个从开始到结束按部就班的连续的“步骤”
# → 依次逐步完成这些步骤，如果某一个步骤的难度较大，
# 又可以将该步骤再次细化为若干个子步骤，以此类推，一直到结尾并得到我们想要的结果
# 程序的主体是函数，一个函数就是一个封装起来的模块，可以实现特定的功能，
# 程序的各个子步骤也往往就是通过相关的函数来完成的！从而实现代码的重用与模块化编程
# 举个栗子：大家以来传智教育报名学习这件事情，
# 可以分成哪些步骤？开始 → 学员提出报名，提供相关材料  →
# 学生缴纳学费，获得缴费凭证  →  教师凭借学生缴费凭证进行分配班级 →
# 班级增加学生信息  → 结束,所谓的面向过程，就是将上面分析好了的步骤，
# 依次执行就行了！


# 面向对象的思想
# 所谓的面向对象，就是在编程的时候尽可能的去模拟现实世界！
# 在现实世界中，任何一个操作或者业务逻辑的实现都需要一个实体来完成！
# 实体就是动作的支配者，没有实体，也就没有动作发生！
# 思考：上面的整个报名过程，都有哪些动词？
# 提出、提供、缴纳、获得、分配、增加
# 有动词就一定有实现这个动作的实体！
# 所谓的模拟现实世界，
# 就是使计算机的编程语言在解决相关业务逻辑的时候，
# 与真实的业务逻辑的发生保持一致，
# 需要使任何一个动作的发生都存在一个支配给该动作的一个实体（主体），
# 因为在现实世界中，任何一个功能的实现都可以看做是一个一个的实体在发挥其各自的“功能”
# （能力）并在内部进行协调有序的调用过程！

# 类的概念
# 对象如何产生？又是如何规定对象的属性和方法呢？
# 答：在Python中，采用类（class）来生产对象，用类来规定对象的属性和方法！也就是说，
# 在Python中，要想得到对象，必须先有类！
# 为什么要引入类的概念？ 类本来就是对现实世界的一种模拟，
# 在现实生活中，任何一个实体都有一个类别，
# 类就是具有相同或相似属性和动作的一组实体的集合！
# 所以，在Python中，对象是指现实中的一个具体的实体，
# 而既然现实中的实体都有一个类别，所以，OOP中的对象也都应该有一个类！
# 一个对象的所有应该具有特征特性信息，都是由其所属的类来决定的，
# 但是每个对象又可以具有不同的特征特性信息，比如，我自己（人类）这个对象，
# 名字叫老王，性别男，会写代码，会教书；另一个对象（人类）
# 可能叫赵薇，性别女，会演戏，会唱歌！

# 类的定义
# Python3中类分为：经典类 和 新式类
# 经典类：不由任意内置类型派生出的类，称之为经典类
# class 类名:
#     代码
#     ......
# 新式类：
# class 类名():
#     代码
#     ......
# 这就是一个类，只不过里面什么都没有！其中，
# 类名不区分大小写，遵守一般的标识符的命名规则（以字母、数字和下划线构成，
# 并且不能以数字开头），一般为了和方法名相区分，
# 类名的首字母一般大写！（大驼峰法）

class Person():
    def eat(self):
        print('我喜欢吃零食')
    def drink(self):
        print('我喜欢喝果汁')
# 类的实例化 创建对象
# 创建对象
p1 = Person()
# <__main__.Person object at 0x1013ecf50>
print(p1)
# p1对象调用实例方法
p1.eat()
p1.drink()

# self 重点
# 在类中，有一个特殊关键字self，其指向类实例化对象本身。
# 注意：打印对象和self得到的结果是一致的，都是当前对象的内存中存储地址。
# 1. 定义类
class Person():
    def eat(self):
        print('我喜欢吃零食')
        # <__main__.Person object at 0x1058bced0>
        print(self)
# 2. 创建对象
p1 = Person()
# <__main__.Person object at 0x1058bced0>
print(p1)
p1.eat()
p2 = Person()
# <__main__.Person object at 0x1058bcf50>
print(p2)
# 添加获取对象属性
# 属性即是特征，比如：人的姓名、年龄、身高、体重…都是对象的属性。
# 对象属性既可以在类外面添加和获取，也能在类里面添加和获取。
# 在外面添加
# 对象名.属性名 = 值
p1.name = '老王'
p1.age = 18
p1.address = '北京'
# 在外面获取
# 对象名.属性名
print(f'姓名：{p1.name}')
print(f'年龄：{p1.age}')
print(f'地址：{p1.address}')

# 类里面获取对象属性
# self.属性名
# 1. 定义类
class Person():
    def print_info(self):
        # 类里面获取实例属性
        print(f'姓名：{self.name}')
        print(f'年龄：{self.age}')
        print(f'地址：{self.address}')
# 2. 创建对象
p1 = Person()
# 3. 添加属性
p1.name = '老王'
p1.age = 18
p1.address = '北京'
p1.print_info()

# 魔术方法 重要
# 在Python中，__xxx__()的函数叫做魔法方法，指的是具有特殊功能的函数。
# __init__()方法  有点类似构造方法
# 思考：人的姓名、年龄等信息都是与生俱来的属性，可不可以在生产过程中就赋予这些属性呢？
# 答：可以，使用__init__() 方法，其作用：实例化对象时，连带其中的参数，
# 会一并传给__init__函数自动并执行它。__init__()函数的参数列表会在开头多出一项，
# 它永远指代新建的那个实例对象，Python语法要求这个参数必须要有，名称为self。
class Person():
    # 定义初始化功能的函数
    def __init__(self):
        # 添加实例属性
        self.name = '老王'
        self.age = 18
        self.address = '北京'
    def print_info(self):
        # 类里面调用实例属性
        print(f'姓名：{self.name}, 年龄：{self.age}，地址：{self.address}')
p1 = Person()
p1.print_info()
# 注意事项
# ① __init__()方法，在创建一个对象时默认被调用，不需要手动调用
# ② __init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象
# 引用传递过去。

# 带参数的__init__()方法  类似于Java中的有参数构造方法
# 虽然我们已经可以通过__init__实现类属性的初始化操作，
# 但是以上案例还存在一个问题，所有实例属性都拥有相同的
# name、age以及address，这显然是不对的。
# 应该如何解决呢？答：使用带参数的__init__()
class Person():
    # 定义初始化功能的函数
    def __init__(self, name, age, address):
        # 添加实例属性
        self.name = name
        self.age = age
        self.address = address
    def print_info(self):
        # 类里面调用实例属性
        print(f'姓名：{self.name}, 年龄：{self.age}，地址：{self.address}')
p1 = Person('老王', 18, '北京')
p1.print_info()
p2 = Person('老李', 20, '深圳')
p2.print_info()

# __str__()方法
# 当使用print输出对象的时候，默认打印对象的内存地址。
# 如果类定义了`__str__`方法，那么就会打印从在这个方法中 return 的数据。
class Person():

    # 定义初始化功能的函数
    def __init__(self, name, age, address):
        # 添加实例属性
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        """ 返回一个对象的描述信息 """
        return f'姓名：{self.name}，年龄：{self.age}，地址：{self.address}'

p1 = Person('老王', 18, '北京')
print(p1)

# __del__()方法
# 当删除对象时，python解释器也会默认调用__del__()方法。
class Person():
    # 定义初始化功能的函数
    def __init__(self, name, age, address):
        # 添加实例属性
        self.name = name
        self.age = age
        self.address = address
    def __del__(self):
        print(f'{self}对象已经被删除')

p1 = Person('老王', 18, '北京')
# <__main__.Person object at 0x101af8f90>对象已经被删除
del p1

# 面向对象三大特性
# 封装、继承、多态
# ① 封装
# 将属性和方法书写到类的里面的操作即为封装，封装可以为属性和方法添加私有权限。
# ② 继承
# 子类默认继承父类的所有属性和方法，与此同时子类也可以重写父类属性和方法。
# ③ 多态
# 多态是同一类事物具有的多种形态。不同的对象调用同一个接口（方法），表现出不同的状态，称为多态。

# 封装
# 私有属性和私有方法
# 在Python中，可以为实例属性和方法设置私有权限，
# 即设置某个实例属性或实例方法不继承给子类。
# 设置私有属性和私有方法的方式非常简单：
# 在属性名和方法名 前面 加上两个下划线 "__" 即可。
class Girl():
    def __init__(self):
        self.name = '小美'
        # 私有属性
        self.__age = 18
    # 私有方法
    def __showinfo(self):
        print('姓名：%s，年龄：%d' % (self.name, self.__age))
girl = Girl()
print(girl.name)
# 外界不能直接访问私有属性和私有方法
print(girl.__age)
girl.__showinfo()

# 获取与设置私有属性值
# 在Python中，一般定义函数名'
# get_xx '用来获取私有属性，
# 定义' set_xx '用来修改私有属性值。
class Girl():
    def __init__(self):
        self.name = '小美'
        self.__age = 18
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

girl = Girl()
girl.set_age(19)
print(girl.get_age())
# 封装的意义在哪里？
# ① 封装数据属性：明确的区分内外，控制外部对对隐藏的属性的操作行为
class People(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print('Name:<%s> Age:<%s>' % (self.__name, self.__age))

    def set_info(self, name, age):
        if not isinstance(name, str):
            print('名字必须是字符串类型')
            return
        if not isinstance(age, int):
            print('年龄必须是数字类型')
            return
        self.__name = name
        self.__age = age
# 封装方法：隔离复杂度
class ATM:
    def  __card(self):
         print('插卡')
    def  __auth(self):
         print('用户认证')
    def __input(self):
          print('输入取款金额')
    def __print_bill(self):
          print('打印账单')
    def __take_money(self):
          print('取款')

    def withdraw(self):
          self.__card()
          self.__auth()
          self.__input()
          self.__print_bill()
          self.__take_money()
atm = ATM()
atm.withdraw()

# 继承
# 我们接下来来聊聊Python代码中的“继承”：类是用来描述现实世界中同一组事务的共有特性的抽象模型，
# 但是类也有上下级和范围之分，比如：生物 => 动物 =>
# 哺乳动物 => 灵长型动物 => 人类 => 黄种人
# 从哲学上说，就是共性与个性之间的关系，
# 比如：白马和马！所以，我们在OOP代码中，
# 也一样要体现出类与类之间的共性与个性关系，
# 这里就需要通过类的继承来体现。简单来说，
# 如果一个类A使用了另一个类B的成员（属性和方法），
# 我们就可以说A类继承了B类，同时这也体现了OOP中代码重用的特性！
# 在Python中，所有类默认继承object类，
# object类是顶级类或基类；其他子类叫做派生类。
# # 父类B
# class B(object):
# 	pass
#
# # 子类A
# class A(B):
#     pass
# 继承：一个类从另一个已有的类获得其成员的相关特性，就叫作继承！
# 派生：从一个已有的类产生一个新的类，称为派生！
# 很显然，继承和派生其实就是从不同的方向来描述的相同的概念而已，本质上是一样的！
#
# 父类：也叫作基类，就是指已有被继承的类！
# 子类：也叫作派生类或扩展类
#
# 扩展：在子类中增加一些自己特有的特性，就叫作扩展，没有扩展，继承也就没有意义了！
# 单继承：一个类只能继承自一个其他的类，不能继承多个类，单继承也是大多数面向对象语言的特性！
# 多继承：一个类同时继承了多个父类， （C++、Python等语言都支持多继承）

# 单继承
# # 父类B
# class B(object):
# 	pass
#
# # 子类A
# class A(B):
#     pass
class Animal(object):
    def eat(self):
        print('吃...')

    def sleep(self):
        print('睡...')

    def call(self):
        print('叫...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass

# 重写父类属性和方法
# 重写也叫作覆盖，就是当子类成员与父类成员名字相同的时候，
# 从父类继承下来的成员会重新定义！
# 此时，通过子类实例化出来的对象访问相关成员的时候，
# 真正其作用的是子类中定义的成员！
# 上面单继承例子中 Animal 的子类 Cat和Dog 继承了父类的属性和方法，
# 但是我们狗类Dog 有自己的叫声'汪汪叫'，猫类 Cat 有自己的叫声 '喵喵叫' ，
# 这时我们需要对父类的 call() 方法进行重构。如下：
# 思考一个问题：此时父类中的call方法还在不在？
# 答：还在，只不过是在其子类中找不到了。类方法的调用顺序，
# 当我们在子类中重构父类的方法后，Cat子类的实例先会在自己的类 Cat 中查找该方法，
# 当找不到该方法时才会去父类 Animal 中查找对应的方法。

# 调用父类属性和方法
# super()：调用父类属性或方法，完整写法：super(当前类名, self).属性或方法()
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('吃...')

    def sleep(self):
        print('睡...')

    def call(self):
        print('叫...')
class Dog(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def __str__(self):
        return f'{self.name}，今年{self.age}岁了，我会汪汪叫...'

class Cat(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def __str__(self):
        return f'{self.name}，今年{self.age}岁了，我会喵喵叫...'

# Python中的多继承实现
# 多继承：一个类同时继承了多个父类，
# 并且同时具有所有父类的属性和方法例如：
# 孩子会继承父亲 和 母亲的方法。
class Father(object):
    pass


class Mother(object):
    pass


class Child(Father, Mother):
    pass
# 注：MRO(Method Resolution Order)：方法解析顺序，我们可以通过
# 类名.__mro__或类名.mro()获得“类的层次结构”，
# 方法解析顺序也是按照这个“类的层次结构”寻找到。

# 多态
# 多态指的是一类事物有多种形态。
# 定义：多态是一种使用对象的方式，子类重写父类方法，
# 调用不同子类对象的相同父类方法，可以产生不同的执行结果
# ① 多态依赖继承
# ② 子类方法必须要重写父类方法
# 好处：调用灵活，有了多态，更容易编写出通用的代码，
# 做出通用的编程，以适应需求的不断变化！

# 多态实现步骤
# 定义父类，并提供公共方法
# 定义子类，并重写父类方法
# 传递子类对象给调用者，可以看到不同子类执行效果不同
# 类具有继承关系，并且子类类型可以向上转型看做父类类型，
# 如果我们从 Animal 派生出 Cat和 Dog，并都写了一个 call() 方法，如下示例：
class Cat(Animal):
   def __init__(self, name, age, sex):
       super(Cat, self).__init__(name, age)
       self.sex = sex

   def call(self):
       print(self.name, '会“喵喵”叫')

class Dog(Animal):
   def __init__(self, name, age, sex):
       super(Dog, self).__init__(name, age)
       self.sex = sex
   def call(self):
       print(self.name, '会“汪汪”叫')
class Animal(object):
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def call(self):
       print(self.name, '会叫')

# 其他特性
# 类方法 属性
# 静态方法
# 在开发时，如果需要在类中封装一个方法，这个方法：
# ① 既 不需要访问实例属性或者调用实例方法
# ② 也 不需要访问类属性或者调用类方法
# 这个时候，可以把这个方法封装成一个静态方法
@staticmethod
def 静态方法名(): 
    pass
