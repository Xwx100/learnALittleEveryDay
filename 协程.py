def consumer():
    r = 'a'
    while True:
        print('print:%s' %('haha'))
        n1 = yield r
        print(n1)
        if not n1:
            return
        print('[CONSUMER] Consuming %s...' % n1)
        r = '200 OK'
def produce(c):
    r1=c.send(None)
    print('print:%s' %(r1))

#return
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r1 = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r1)
    c.close()

c = consumer()
produce(c)