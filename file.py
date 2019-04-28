helloFile = open('hello.txt')   # 將檔案存成實體物件
helloContent = helloFile.read() # 將檔案物件讀取並存成helloContent變數
print(helloContent)             # 印出變數資料
sonnetFile = open('sonnet29.txt')
test = sonnetFile.readlines()   # 將每行字串變成清單
print(test)

# 覆寫檔案
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!!\n')
baconFile.close()
# 新增字串
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
# 讀取檔案
baconFile = open('bacon.txt', 'r')
content = baconFile.read()
baconFile.close()
print(content)

# 使用shelve模組儲存純文字檔
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
print(shelfFile['cats'])
print(list(shelfFile.keys()))   # 將shelfFile的清單轉成清單格式(型別轉換),印出key值(有s)
print(list(shelfFile.values())) # 將shelfFile的清單轉成清單格式(型別轉換),印出value值(有s)
shelfFile.close()
test = type(shelfFile)  # 檢視shelfFile型別
print(test)






