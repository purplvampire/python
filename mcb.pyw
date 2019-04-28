#! python3
# mcb.pyw - Save and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        Py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()   # 將字典的value存到key中
elif len(sys.argv) == 2:
# TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))  # 列出字典的key
    else:
        pyperclip.copy(mcbShelf[sys.argv[1]])   # 呼叫字典的value

mcbShelf.close()
