'''
import shutil, os
shutil.copy('test.txt', 'C:\\delicious')    # 將檔案複製到目錄
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')    # 將目錄複製到新目錄
shutil.move('C:\\bacon\\bacon.txt', 'C:\\bacon\\eggs') # 將檔案搬移或改名

import send2trash
baconFile = open('bacon.txt', 'a')  # Create the file
baconFile.write('Bacon is not a vegetable.')    # 寫入檔案
baconFile.close()   # 關閉檔案

send2trash.send2trash('bacon.txt')  # 刪除檔案(垃圾桶)
'''

'''import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

print('')'''

import zipfile, os
# os.chdir('C:\\')    # move to the folder with example.zip

# open zip file
exampleZip = zipfile.ZipFile('example.zip')
test = exampleZip.namelist()
print(test)

# print file size
spamInfo = exampleZip.getinfo('spam.txt')
test = spamInfo.file_size
print(test)

# print compression size
test = spamInfo.compress_size
print(test)

# calculate compression rate
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))

# extra all zip file
exampleZip.extractall('C:\\delicious')

# extra special zip file
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')

# close zip file
exampleZip.close()

# create zip file
newZip = zipfile.ZipFile('newzip.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()




