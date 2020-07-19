# my_file= open('text.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
#
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
#
# print(my_file.readlines())
# my_file.close()

#Standered way to open a file is with that way you dont have to close it

try:
    with open('text1.txt') as my_file:
        print(my_file.readlines())
except FileNotFoundError as err:
    print("File Not Found", err)
except IOError as err:
    print('File Errors', err)


    # my_file.writelines('This is the first line I am wrtting')