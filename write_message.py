filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")

with open(filename,'a') as file_object:
    file_object.write('I alse love finding meaning in large datasets')
