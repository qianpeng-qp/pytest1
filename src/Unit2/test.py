fo = open('Employee.txt', 'r', encoding="utf-8")
lines = fo.readlines()
fo.close()
iempdata = list()
for line in lines[1:]:
    line = line.split()
    info_emp = {
        'emp_id': line[0],
        'emp_name': line[1],
        'emp_birth': line[2],
        'emp_edu': line[3],
        'emp_sex': line[4],
        'emp_kpi': int(line[5])
    }
    iempdata.append(info_emp)

print( iempdata)