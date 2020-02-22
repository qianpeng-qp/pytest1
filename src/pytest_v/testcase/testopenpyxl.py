from openpyxl import Workbook
#实例化对象
workbook = Workbook()
#创建一个sheet
worksheet = workbook.active


worksheet['A1'] = 'a1'
worksheet['B1'] = 'b1'

print(worksheet.title)#sheet名

worksheet.title = '测试1'

workbook.save(filename='testexl.xls')