#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re    # 載入剪貼簿模組與正規表示式模組

# Create phone regex.
phoneRegex = re.compile(r'''(
    (\d{3} | \(\d{3}\))?        # 2 types area code
    (\s | - | \.)               # separator(space or - or .)
    (\d{3})                     # first 3 digits
    (\s | - | \.)               # separator(space or - or .)
    (\d{4})                     # last 4 digits
    (\s*(ext | x | ext.)\s*(\d{2,5}))?       # separator(space(or not) + ext or x or ext.) extension(at least)
    )''', re.VERBOSE)

# Create eamil regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username(一個以上字元)
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name(一個以上字元)
    (\.[a-zA-Z]{2,4})           # dot-something(網域類型)
    )''', re.VERBOSE)


# Find matches in clipboard text.
text = str(pyperclip.paste()) # 將剪貼簿上的字串設為變數text
matches = [] # 建立空清單

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]    # phoneNum = phoneNum + ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))  # 將清單用換行符號串連成一個字串
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
