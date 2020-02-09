from collections import OrderedDict

from class_1.class1 import Car,ElectriCar
# my_dog = Dog('white',6)
# her_dog=Dog('red',3)
# print ('name:'+my_dog.name + 'age:'+ str(my_dog.age))
# my_dog.sit()
# my_dog.roll_over()
# her_dog.sit()
# her_dog.roll_over()
#class类-----------------------------------------------------------------------------------------------------------
my_new_car= Car('audi','24',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23  #修改默认值
my_new_car.read_odometer()
my_new_car.update_odometer(30)      #调用方法更新里程数
my_new_car.read_odometer()
my_new_car.increment_odmeter(3)
my_new_car.read_odometer()
#子父类调用--------------------------------
my_tesla = ElectriCar('tesla','model_s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas()
my_tesla.battery_size.describe_battery()   # 调用ElectriCar 属性的battery_size ，调用Battery()
my_tesla.battery_size.get_rang()            #获取里程数
my_tesla.battery_size.battery_size = 85   #调用Battery() 修改电池属性
my_tesla.battery_size.get_rang()
#OrderedDict 创建空字典
favorite_language = OrderedDict()
favorite_language['jen']='python'
favorite_language['aa']='c'
favorite_language['cc']='java'
for name,language in favorite_language.items():
    print(name.title()+language.title())
