# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕

try:
    print('try: ')
    # a = 1 # 正常
    a = 10/0 # 错误
    print(a) # 错误时不执行后面语句
    print('haha')
except ZeroDivisionError as e: # 只有错误时执行，正确不执行
    print('error: %s'%e)
else: # 只有正确时执行
    print('no Error')
finally:
    print('finally : ')