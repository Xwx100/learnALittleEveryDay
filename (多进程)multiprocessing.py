from multiprocessing import Pool,Process,Queue
import os
import time,random

## 多进程
# def run_proc(name):
#     print('(child process)子进程-%s-%s'%(name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Run time: %s'%(end-start))
#
# def main():
#     print('(Parent process)父进程-父-%s'%(os.getpid()))
#     print('Child process will start.')
#     p = Pool(2)
#     for num in range(6):
#         p.apply_async(run_proc,args=(num,))
#     p.close()
#     p.join()
#     print('Child process end.')
#
# if __name__ == '__main__':
#     main()

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()