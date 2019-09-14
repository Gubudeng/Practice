file_path = 'D:\pi_digits.txt'
with open(file_path) as file_object2:
    lines = file_object2.readlines()

    for line in lines:
        print(line.rstrip())
