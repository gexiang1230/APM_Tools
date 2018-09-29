class FOO:
    pass
# 方法1
f1=FOO()

print(type(f1))
print(type(FOO))
'''产生类的两种方法'''
# 方法2
FFO=type('FOO',(object,),{'x':1})
F2=FFO()
print(FFO)
print(F2)
#第一个参数：类名
#第二个参数：继承的父类，新式类集成object，使用元组的方式
#第三个参数：类的属性，使用字典的方式