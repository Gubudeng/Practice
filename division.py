# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can not divide by zero!")
#
# print("Give me two numbers, and I'll devide them.")
# print("Enter 'q' to quit. ")
#
# while True:
#     first_number = input("\nFirst number:")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number:")
#     try:
#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0")
#     except ValueError:
#         print("You input value error!")
#     else:
#         print(answer)
#
#
# def count_words(file_path):
#
#     try:
#         with open(file_path,'r', encoding='UTF-8') as file_object:
#             contents = file_object.read()
#     except FileNotFoundError:
#         msg = 'Sorry, the file ' + file_path + ' does not exist.'
#         print(msg)
#     else:
#         #计算单词的数量
#         words = contents.split()
#         number_words = len(words)
#         print(str(number_words))
#
# file_path = ['alice.txt','little_women.txt','moby_dick.txt','xxxx.txt']
# for file in file_path:
#     count_words(file)

