import xlwings as xw
# C:\Users\502760349\Desktop\database\2000.xlsx
app = xw.App(visible=True, add_book=False)
wb=app.books.open(r'C:\Users\502760349\Desktop\database\AssetImport.xlsx')
sht=wb.sheets['Asset List']
# sht.range('A7').value = "fc02"

'''产生数据'''
deviceId=[i for i in range(10)] #设备编号
deviceName=[]                   #设备名称
for dec in deviceId:
    devn ='设备'+str(dec)
    deviceName.append(devn)
'''存放数据'''
sht.range('A7').options(transpose=True).value=deviceId   #设备编号
sht.range('B7').options(transpose=True).value=deviceName #设备名称
sht.range('P7:P17').value='放射科'     #设备分类
wb.save()  # 保存表
wb.close()  # 关闭表
app.quit()

