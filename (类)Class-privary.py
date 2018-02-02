class Myclass(object):
    a = '公有'
    _b = '类私有'
    __c = '私有'

# a 任何都可访问，权限级别低
# _b 类对象和实例对象都可访问，权限级别中等
print(Myclass.a,Myclass._b)
# __c 任何外部都不可访问，权限级别高
print(Myclass.__c)