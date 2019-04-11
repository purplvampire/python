import pyperclip
# 將剪貼簿的字串存成變數text
text = pyperclip.paste()

# 切割字串變成清單
lines = text.split('\r\n')

# 將清單內的字串依序進行加工
for i in range(len(lines)):     # 以清單的長度為範圍
    lines[i] = '* ' + lines[i]  # 將每個清單上的字串依序加工
    print(lines)

# 將清單內的字串依序進行加工
for line in lines:          # 依序呼叫清單內的字串
    line = line.strip('* ') # 刪除特定字串
    print(line)

# 將調整後的字串貼回剪貼簿
pyperclip.copy(text)


