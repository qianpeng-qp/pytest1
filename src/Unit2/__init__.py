class Employee():
    def __init__(self, emp_id, emp_name, emp_edu='本科'):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_edu = emp_edu

    file = 'Employee.txt'
    iempdata = list()
    def readfile(self):
        fo = open(self.file, 'r', encoding="utf-8")
        lines = fo.readlines()
        fo.close()
        if len(lines) < 2:
            return []
        for line in lines[1:]:
            line = line.split('\t')
            info_emp = {
                'emp_id': line[0],
                'emp_name': line[1],
                'emp_birth': line[2],
                'emp_edu': line[3],
                'emp_sex': line[4],
                'emp_kpi': int(line[5])
            }
            self.iempdata.append(info_emp)
        return self.iempdata
    def _getNewId(self):
        """获取最大员工id+1"""
        if len(self.iempdata) != 0:
            dempDataRow = max(self.iempdata, key=lambda x: x['emp_id'])
            print(dempDataRow)
            iNewid = int(dempDataRow['emp_id'])+1
        else:
            iNewid =1
        return iNewid



my_employee = Employee('eu','23')
print(my_employee.readfile())
print(my_employee._getNewId())
