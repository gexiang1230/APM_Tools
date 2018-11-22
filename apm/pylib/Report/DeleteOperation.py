import xlwings as xw
class DeleterOpertion():
    def __init__(self,fn,delete_list):
        self.fn = fn
        self.delete_list=delete_list
    def rule(self):
        #自定义规则
        pass
    def Delete(self):
        #删除
        # visible 控制 Excel 打开是否显示界面
        # add_book 控制是否添加新的 workbook
        app = xw.App(visible=True, add_book=False)
        # app.display_alerts = False
        # 打开 data.xlsx 文件到 wookbook 中
        wb = app.books.open(self.fn)
        # 切换到当前活动的 sheet 中
        sheet= wb.sheets.active

        # 选择 A1 所在的一列
        # 当 Excel 格式复杂的时候,不建议使用 expand
        # 可以这样选择
        # Delete origin row
        temp_del = 0
        if len(self.delete_list) > 0:
            for delete_row in self.delete_list:
                # Delete one row
                sheet.range('A' + str(delete_row - temp_del)).api.EntireRow.Delete()
                temp_del = temp_del + 1
        wb.save()
        # sheet.range("A7:A100").api.EntireRow.Delete()
        # ARange = sheet.range("A1").expand("down")
        # for A in ARange:
        #     if str(A.value).strip() not in self.ExistSet:
        #         self.ExistSet.add(str(A.value).strip())
        #     else:
        #         # address = A.address
        #         # 获取 A 所在的位置坐标
        #         self.ToDelList.append(A.address)
        #         # print(A.value)
        #
        # while self.ToDelList:
        #     td = self.ToDelList.pop()
        #     # 删除 A 所在的一行
        # sheet.range(td).api.EntireRow.Delete()
        app.quit()
if __name__=='main':
    fn = r'C:\Users\502760349\Desktop\database\APM_Asset_Template.xlsx'
    delete_list=[7]
    d = DeleterOpertion(fn,delete_list)
    d.Delete()
