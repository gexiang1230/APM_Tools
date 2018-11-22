import re
from allpairspy import AllPairs
class  generationParams:
    def __init__(self,path):
        self.path=path
    def genPara(self):
        allkeys=[]     #表头
        allvalue=[]    #值的列表
        allpairs=[]
        with open(self.path,'r',encoding='utf8') as f:
            allParas=f.readlines()
        for all in allParas:
            r='[：，:,]'
            all=re.split(r,all.strip())#所有切割好的值,strip()去掉头和尾左右的空格
            allkeys.append(all[0])
            allvalue.append(all[1:])
        allpairs.append(allkeys)
        ##生成正交列表
        for pairs in AllPairs(allvalue):
            allpairs.append(pairs)
        return allpairs #返回表头和正交值


if __name__=='__main__':
    import sys
    print(sys.path)
    paras1 = r'C:\Users\502760349\Desktop\database\new.txt'
    g=generationParams(paras1)
    all1 = g.genPara()
    print('result--表头')
    print(all1[0])
    print('result--body')
    print(all1[1])

