'''产生数据'''
class AssetManage:
  def __init__(self,num):#此处需要做一下num的描述符限制---只能输入数字
      self.num=num
  def devices(self):
      deviceId=[i for i in range(self.num)] #设备编号
      deviceName=[]                         #设备名称
      deviceAssort = []                     #设备分类
      ownerApart=[]                         #所属科室
      deviceSystemId=[]
      for dec in deviceId:
        devn ='设备'+str(dec)
        systemid='082400000'+str(dec)
        deviceName.append(devn)
        deviceAssort.append('信息设备')
        ownerApart.append('设备科')
        deviceSystemId.append(systemid)
      return  deviceId,deviceName,deviceAssort,ownerApart,deviceSystemId
  def org(self):
      '''组织结构导入数据源'''
      #group, hostipital, hospital_district, department
      