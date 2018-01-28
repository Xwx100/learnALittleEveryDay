# 不适用type(元类)动态创建类对象
def chooseClass(class_name):
    if class_name == 'Demo1':
        class Demo1(object):
            pass
        return Demo1
    else:
        class Demo2(object):
            pass
        return Demo2
demo = chooseClass('Demo2')
print(demo)


# 使用type(元类)动态创建类对象
class MyClass(object):
     class_attr1 = 1

     def __init__(self):
         self.init1 = 2

def init2(self):
    return '拥有init2属性'

MyMetaClass = type('MyClass',(),{'class_attr2':2,
                                 'init2':init2
                                 })
# 元类 的 实例对象: 类对象
# 类对象 的 实例对象: 实例对象
MyClass1 = MyMetaClass()
# 打印元类
print(type(MyMetaClass))
# 元类、过渡类、类(元类所创建的子类)
print(MyMetaClass,MyClass,MyClass1)
print(MyMetaClass.__class__,MyClass.__class__,MyClass1.__class__)
print(MyClass.class_attr1,MyClass1.class_attr2,MyClass1.init2())

# ORM: 类的实例--具体数据
#      元类的实例--具体表

# 使用函数自定义元类
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    #通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)#返回一个类

# 使用类自定义元类
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

class Foo(object,metaclass=UpperAttrMetaclass):
    bar = 'bip'

print(Foo.__dict__)
print(hasattr(Foo,'BAR'))