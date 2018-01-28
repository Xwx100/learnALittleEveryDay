# 类：
# 继承(使用其他类的属性或方法)、
# 封装(简单调用类的内部属性或方法，使使用者不需明白原理即可调用)、
# 多态(多种姿态，实现代码重用或重写)


# 动物属性为总属性
# 实例属性为分属性
# 分属性没有找总属性，二者都有的话，各找各的，不会替代，不像继承，会替代
# 为啥继承要替代，实现代码重写
class Animal(object):
    name = 'Dog'
    weight = 200

    def __init__(self,name):
        self.name = name
        # 实例没有的属性找类属性
        # 如果同时存在，取决于你是对类对象还是对实例对象，
        # self.weight = weight

    def eat(self):
        print('%s can eat!!!'%self.name)

animal = Animal('cat')
print(animal.name,animal.weight)
print(Animal.name,Animal.weight)

# 对实例修改，若name不存在，则添加，存在，则修改-------这就是动态语言的美或坑
# 实例对象增加属性名Pig，二者同时存在，取决于你对谁取值
animal.weight = 100
print(animal.weight,Animal.weight)

Animal.weight = 300
print(animal.weight,Animal.weight)


# 类也是对象，类对象 相当于造物工厂
# 实例对象则为具体物品
class FactoryCar(object):
    """造车工厂"""
    hasWheel = 4

    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def has_func(self):
        print('%s 拥有很多功能'%self.name)
        # Python解释器没有执行到明确的return语句，自动返回None
        # return '%s 拥有很多功能'%self.name

# 类对象(造物工厂)：FactoryCar
# 实例对象(具体的物品): 宝马车，法拉利
BMW = FactoryCar('宝马', 400, 700)
Ferrari = FactoryCar('法拉利', 500, 800)
print(BMW.hasWheel)
print(Ferrari.has_func())

# 当python解释器执行到关键字Class指令时，会在内部创建一个名为FactoryCar类，这个类也是对象，称之为类对象
# 它一样有 标识、值、类型
print(id(FactoryCar))
print(FactoryCar)
print(type(FactoryCar))# 类型为type(元类)
print(FactoryCar.__class__)
