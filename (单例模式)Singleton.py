
# 使用__new__方法实现单例
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

# 用is判断两个对象引用是否指向同一对象
# 而==是判断两个对象是否相等
print(Singleton.__dict__)
print(Singleton.mro())
print(s1 is s2)

class Singleton_not_new(type):
    def __init__(self, *args, **kwargs):
        print("__init__")
        self.__instance = None
        super(Singleton_not_new,self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__")
        if self.__instance is None:
            self.__instance = super(Singleton_not_new,self).__call__(*args, **kwargs)
        return self.__instance


class Foo(object,metaclass=Singleton_not_new):
    pass #在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在Foo实例化的时候执行。且仅会执行一次。


foo1 = Foo()
foo2 = Foo()
print(foo1)
print(Foo.__dict__)  #_Singleton__instance': <__main__.Foo object at 0x100c52f10> 存在一个私有属性来保存属性，而不会污染Foo类（其实还是会污染，只是无法直接通过__instance属性访问）

print(foo1 is foo2)  # T