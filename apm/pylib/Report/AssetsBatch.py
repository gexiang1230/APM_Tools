import xlwings as xw
class AssetsBatch():
    def __init__(self,deviceID,devicename,deviceAssort,ownerApart,deviceSystemId):
        self.deviceID=deviceID
        self.devicename=devicename
        self.deviceAssort=deviceAssort
        self.ownerApart=ownerApart
        self.deviceSystemId=deviceSystemId

    def AssetsReport(self):
        '''生成资产'''
        app = xw.App(visible=True, add_book=False)
        wb = app.books.open(r'C:\Users\502760349\Desktop\database\APM_Asset_Template2.xlsx')
        sht = wb.sheets['Asset List']
        sht.range('A7').options(transpose=True).value = self.deviceID  # 设备编号
        sht.range('B7').options(transpose=True).value = self.devicename # 设备名称
        sht.range('Q7').options(transpose=True).value=self.deviceAssort #设备分类
        sht.range('H7').options(transpose=True).value = self.ownerApart #所属科室
        sht.range('X7').options(transpose=True).value = self.deviceSystemId
        wb.save() #保存表
        wb.close() #关闭表
        app.quit()

class Org():
    '''组织机构'''
    def __init__(self,group,hostipital,hospital_district,department):
        self.group=group
        self.hostipital=hostipital
        self.hostipital_district=hospital_district
        self.department=department
    def OrgReport(self):
        app=xw.App(visible=True,add_book=False)
        wb=app.books.open(r'C:\Users\502760349\Desktop\database\APM_Org_Template.xlsx')
        sht=wb.sheets['datalist']
        sht.range('A2').options(transpose=True).value = self.group        #  集团
        sht.range('B2').options(transpose=True).value = self.hostipital     #  医院
        sht.range('C2').options(transpose=True).value = self.hostipital_district #院区
        sht.range('D2').options(transpose=True).value = self.department     #科室

