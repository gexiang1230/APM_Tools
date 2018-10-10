from AssetManagement import AssetManage
from  AssetsBatch import AssetsBatch


ams=AssetManage(5000) #生成行数为10的数据----设备编号，设备名称，设备分类
adb=ams.devices() #获得设备编号，设备名称的列表
abs=AssetsBatch(adb[0],adb[1],adb[2],adb[3],adb[4]) #将数据源传入
abs.AssetsReport()          #生成报表