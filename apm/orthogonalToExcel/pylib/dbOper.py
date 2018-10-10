import re
class  generationParams:
    def __init__(self,path):
        self.path=path
    def genPara(self):
        allkeys=[]     #表头
        allvalue=[]    #值的列表
        with open(self.path,'r') as f:
            allParas=f.readlines()
        for all in allParas:
            minivalue = []
            all=re.split(':/|：/|,/|，',all)#所有切割好的值
            allkeys.append(all[0])
            minivalue.append(all[1:])    #剩下的value先放进一个小列表中
            allvalue.append(minivalue)
        return allkeys,allvalue





if __name__=='main':
    paras1 = r'C:\Users\502760349\Desktop\database\new.txt'
    g=generationParams(paras1)
    all1 = g.genPara()
    print('result')
    print(all1[0],all1[1])

