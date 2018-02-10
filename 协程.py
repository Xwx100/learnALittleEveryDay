# 多线程共用同一变量，导致有GIL锁，麻烦
# 协程:由程序控制，单线程

# 有默认参数,则顾客有默认需求
def consumer(r='可乐'):

    while True:
        # 第一次为None，为空对象，直接返回，n1=‘可乐’=r1
        # 后面不为空对象，后面执行，打印，r=‘200 OK’
        n1 = yield r
        # 如果对象为空，返回退出
        if not n1:
            return
        # 如果对象不为空，打印顾客需求
        print('[读取顾客需求]：%s' % n1)
        r = '200 OK'

# 开发商
def produce(c):
    # send  发送yield的返回值
    r1=c.send(None)
    print('[默认顾客需求]：%s' %(r1))

    need = '汉堡'
    print('-'*30)
    print('[写入顾客需求]：%s'% need)
    r1 = c.send(need)
    print('[顾客需求回应]：%s'% r1)
#return
    n = 0
    while n < 5:
        n = n + 1
        print('-'*30)
        print('[PRODUCER] Producing %s...' % n)
        # 发送0-4的数字
        r1 = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r1)

    c.close()

c = consumer()
produce(c)