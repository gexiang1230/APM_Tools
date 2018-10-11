'''excel 表格生成'''
import xlwings as xw

class toBeOrth():
    def __init__(self,allkeys,allvalues,path):#参数需要表头和body,两个参数
        self.allkeys=allkeys
        self.allvalues=allvalues
        self.path=path
    def tobOrth(self):
        app=xw.App(visible=False,add_book=False)
        wb=app.books.open(self.path)
        sht=wb.sheet['Sheet1']


