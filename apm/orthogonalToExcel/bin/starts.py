from pylib.dbOpera import generationParams
from toBeExcel.toBeOrth import toBeOrth
path = r"C:\Users\502760349\Desktop\new.csv" #生成csv文件地址

paras1 = r'C:\Users\502760349\Desktop\database\new.txt'###参数地址

db=generationParams(paras1) #生成参数实例
datas=db.genPara()          #调用生成正交数据的方法
tb = toBeOrth(datas, path)  #输出实例
tb.tobOrth()                #调用生成csv方法