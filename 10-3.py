file_path = 'guest.txt'
with open(file_path,'w') as file_object:
    while True:
        name = input("输入姓名(输入q退出程序)")
        if name == 'q':
            break
        file_object.write(name)