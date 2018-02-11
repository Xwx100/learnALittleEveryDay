import uuid
import base64
import time

while 1:
# MD5、sha1提供数据完整性的保护，保护数据不被人动过
    a = uuid.uuid4().bytes + uuid.uuid4().bytes
    print(a)
# Base64是网络上最常见的用于传输8Bit字节码的编码方式之一，
# Base64就是一种基于64个可打印字符来表示二进制数据的方法
# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，
# 因为二进制文件包含很多无法显示和打印的字符，
# 所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。
# Base64是一种最常见的二进制编码方法。
    print(base64.b64encode(a))
    time.sleep(1)