# 列表：长度可变
a = [1,"2",True,(2,3,4),[1,2,3,4],{"usrname":"tanyijun"}]
print(a)
# print(a[0])
# print(len(a)) # list列表的长度
# print(a[-1])

# 1、增加元素：
a.append("顾祯蓉") # 只能够用在列表上面
print(a)

# 增加元素的练习题：
# b = [1,2,3,4,5,6]
# print(b[0])
# b.append("谭奕骏")
# print(b)

# 2、删除全部元素
# a.clear()
# print(a)

# 3、从列表中取出元素并且删除取出的元素
# c = a.pop(1)
# print(c)
# print(a)

# 4、统计某个值的个数
d = a.count(1)
print(d) # 打印出来两个“1”，因为计算机中0假1真，默认true为1；
