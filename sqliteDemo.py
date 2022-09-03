#! python3
# This is SQL Lite demo
from sqliteDatabase import create_table, add_entry, get_entries
menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to the programming diary!"

# 執行輸入
def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    
    add_entry(entry_content, entry_date)

# 執行檢視
def view_entries(entries):
    # 將清單分拆成個別的字典
    for entry in entries:
        # 呼叫Tuple(),0=content,1=date
        print(f"{entry[1]}\n{entry[0]}\n\n")


print(welcome)
create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        # 呼叫輸入處理
        prompt_new_entry()
    elif user_input == "2":
        # 呼叫get_entires()返回值,用view_entries()處理
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")