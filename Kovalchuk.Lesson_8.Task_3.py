# 3 C помощью модуля os добавьте на свой рабочий стол папку my_folder,
# в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.

import os
os.mkdir('C:/Users/Kawa/Desktop/my_folder')
os.chdir('C:/Users/Kawa/Desktop/my_folder')
f1 = open('test_1.txt', 'w')
f1.close()
f2 = open('test_2.txt', 'w')
f2.close()
f3 = open('test_3.txt', 'w')
f3.close()
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir('C:/Users/Kawa/Desktop')
os.rmdir('my_folder')