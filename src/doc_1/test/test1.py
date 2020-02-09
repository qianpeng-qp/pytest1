with open('../pi_digits.txt') as file_object:
    data = file_object.readline()
    contens =[i for i in data ]
    print(contens)