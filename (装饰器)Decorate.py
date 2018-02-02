# 装饰器：不动原代码的情况下，增加新功能

# 使用装饰器 实现 <br><i>xu</i></br>
def wrapper2(fn):
    def inside(name1):
        return '<br>' + fn(name1) + '</br>'
    return inside

def wrapper1(fn):
    def inside(name2):
        return '<i>' + fn(name2) +'</i>'
    return inside

@wrapper2
@wrapper1
def character(name0):
    return '%s'%name0

print(character('xu'))

# 在privary函数上增加密码权限


def pWrapper(fn):
    def inside():
        judge_var = input('请输入密码，以确认你的身份: ')
        if judge_var == 'xu':
            return fn()
        else:
            return '输入密码错误'
    return inside

@pWrapper
def privary():
    return '私有东西'

print(privary())