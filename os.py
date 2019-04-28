import os
print(os.path.join('usr', 'bin', 'spam'))

# 呼叫檔案路徑
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

# 取得當前路徑
print(os.getcwd())

# 變更當前路徑
os.chdir('C:\\Windows\\System32')
print(os.getcwd())

# 建立新目錄
'''
os.makedirs('c:\\delicious\\walnut\\waffles')
os.chdir('c:\\delicious\\walnut\\waffles')
print(os.getcwd())
'''
test = os.path.abspath('.') # 當前目錄下的絕對路徑
print(test)
test = os.path.abspath('.\\Scripts') # 指定目錄下的絕對路徑
print(test)
test = os.path.isabs('.') # 是否為絕對路徑
print(test)
test = os.path.isabs(os.path.abspath('.')) # 是否為絕對路徑
print(test)
test = os.path.relpath('C:\\Windows', 'C:\\') # 起始目錄下絕對路徑的相對路徑
print(test)
test = os.path.relpath('C:\\Windows', 'C:\\spam\\eggs') # 起始目錄下絕對路徑的相對路徑
print(test)
# 將路徑分割為個別的目錄存成清單
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
test = calcFilePath.split(os.path.sep) # split:切成清單 os.path.sep:將路徑依序切割
print(test)
'''
test = os.path.getsize('C:\\Windows\\System32\\calc.exe')   # 計算檔案大小
print(test)
test = os.listdir('C:\\Windows\\System32')  # 列出目錄下所有檔案
print(test)
'''
# 印出目錄下每個檔案的大小，並告知目錄的大小
'''
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
    print(filename,os.path.getsize(os.path.join('C:\\Windows\\System32', filename)))
print('C:\\Windows\\System32', totalSize)
'''
test = os.path.exists('D:\\')   # 檔案或目錄是否存在
print(test)
test = os.path.isdir('D:\\')    # 目錄是否存在
print(test)
test = os.path.isfile('D:\\')   # 檔案是否存在
print(test)





