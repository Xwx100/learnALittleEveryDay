# 赋值：N个对象引用 指向 同一个对象

# 下面两个拷贝：外部对象引用 和 对象 一一对应
# 浅拷贝：内部对象引用 没有拷贝
# 深拷贝：内外部对象引用 都拷贝

import copy

a = [1,2,3,4,[6,7]]
b = a # 引用
c = copy.copy(a) # 浅拷贝
d = copy.deepcopy(a) # 深拷贝
a.append(5)
a[4].append(8)

print(id(a), id(b), id(c), id(d))
print(a, b, c, d)