'''产生数据'''
class AssetManage:
  def __init__(self,num):#此处需要做一下num的描述符限制---只能输入数字
      self.num=num

  def devices(self):
      deviceId=[i for i in range(self.num)] #设备编号
      # deviceId = [i for i in range(23000,24000)]  # 设备编号
      deviceName=[]                         #设备名称
      deviceAssort = []                     #设备分类
      ownerApart=[]                         #所属科室
      systemid = [i for i in range(8241008001, 8241008101)]#设备把编号
      SystemId=[]
      for one in systemid:
          one='0'+str(one)
          SystemId.append(one)
      for dec in deviceId:
        devn ='设备'+str(dec)
        deviceName.append(devn)
        deviceAssort.append('信息设备')
        ownerApart.append('设备科')
      return  deviceId,deviceName,deviceAssort,ownerApart,SystemId
  def org(self):
      '''组织结构导入数据源'''
      #group, hostipital, hospital_district, department

if __name__=='__main__':

      manage=AssetManage(100)
      m=manage.devices()
      print(m[4])