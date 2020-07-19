from translate  import Translator

try:
    with open('test.txt',mode='r') as my_file:
        my_line = my_file.readline()
        print(my_line)
except FileNotFoundError as err:
    print('This file is not existed', err)
except IOError as err:
    print('IO Error', err)

to_lang = 'te'

translator = Translator(to_lang=to_lang)
translation = translator.translate(my_line)

with open('test-te.txt', mode='w') as my_file1:
    my_file1.writelines(translation)

# print(translation)