# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
#
#
# file_path = 'D:\pi_digits.txt'
# with open(file_path) as file_object2:
#     # for line in file_object2:
#     #     print(line.rstrip())
#     lines = file_object2.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))
# file_path = 'pi_million_digits.txt'
# with open(file_path) as file_object:
#     lines = file_object.readlines()
#     pi_string = ''
#     for line in lines:
#         pi_string += line.strip()
#
# birthday = input("在这里输入你的生日（950801）")
# if birthday in pi_string:
#     print("你的生日在圆周率前100万个里")
# else:
#     print("你的生日不在哟")
