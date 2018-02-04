# 位置参数，默认参数，可变参数，命名关键字参数，关键字参数
def test(first, second, third, four = 4, five = 5, *args, **kwargs):
    print('first args: %s'%first)
    print('second args: %s'%second)
    print('third args: %s'%third)
    print('four args: %s'%four)
    print('five args: %s'%five)
    for num in args:
        print('other args :%s'%num)
    print('kwargs : %s'%kwargs)

test(1,2,3)
print()
test(1,2,3, four=5, five=4)
print()
test(1,2,3,4,5,6,7)
print()
test(four=5, first=1, second=2, third=3, seven = 7)

# 函数定义时不加可变参数和关键字参数，然后直接在函数调用二者，
def test1(one,two):
    print('one : %s'%one)
    print('two : %s'%two)

args = [2,1]
kwargs = {'one':1,'two':2}

test1(*args)
test1(**kwargs)