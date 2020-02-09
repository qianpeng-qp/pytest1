class Dog():
    def __init__(self,name,age):
        """"一次模拟小狗的尝试"""
        """"初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """"模拟小狗命令蹲下"""
        print (self.name.title()+" is now sitting")
    def roll_over(self):
        """模拟小狗命令时打滚"""
        print (self.name.title()+" rolled over")


class Car():
    """"一次模拟汽车"""
    def __init__(self,make,model,year):
        """初始化汽车属性"""
        self.make = make
        self.model =model
        self.year =year
        self.odometer_reading=0                          #添加默认值
    def get_descriptive_name(self):
        """获取完整信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印里程书"""
        print('里程数'+str(self.odometer_reading))
    def update_odometer(self,mileage):
        """更新里程数且禁止将里程数回调"""
        if(self.odometer_reading<mileage):
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer")
    def increment_odmeter(self,mailes):
        """将里程数增加指定值"""
        self.odometer_reading += mailes
class ElectriCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):  #创建实例
        """初始化父类属性，初始化子类属性"""
        super().__init__(make,model,year)       #super 使实例有父类的属性
        self.battery_size = Battery()
    def describe_battery(self):
        print(str(self.battery_size))
    def fill_gas(self):
        print("有油布")
    def fill_gas(self):            #方法重写
        print("没油了")
class Battery():
    """模拟电动车电瓶"""
    def __init__(self,battery_size=60):           #初始化子类特有属性
        """初始化电瓶属性"""
        self.battery_size=battery_size
    def describe_battery(self):
        """打印电瓶属性"""
        print(" test"+str(self.battery_size))
    def get_rang(self):
        """打印信息，指出电瓶续航里程数"""
        if self.battery_size == 60:
            range= 180
        elif self.battery_size == 85:
            range =270
        print("续航里程数："+str(range))