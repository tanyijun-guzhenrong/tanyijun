# a = (1,2,3,4)
# print(type(a))

# 元组内的元素可取值任意类型，但长度固定，一旦确定变量的值无法更改
b = (1,"2",True,(2,3,4),[1,2,3,4],{"usrname":"tanyijun"})
print(b)

# 下标：第一个元素的下标为0，-1就是倒数第一个值
# print(b[6]):IndexError: tuple index out of range # 专业术语：下标越界

# print(len(b)) # 打印元素的长度
print(b[-1]) # 倒数第几个值，按照下标来计算