import re
import sys
import time


print(r'''

    =========== 歡迎使用VPN設定檔轉換工具 ===========
    
    請輸入本次作業的設定群組：

    (A)：A群組
    (B)：B群組


    或輸入"Q"結束程式
    
''')


group_choice = input("設定群組代號：")

# Quit tool if enter Q key.
while True:
    if group_choice.upper() == "Q":
        print("程式即將終止...感謝您的使用，我們下次見")
        time.sleep(1)
        sys.exit()
    else:
        break


# Take out branch users.
time.sleep(1) 
print("分公司申請人員建檔...")

branch_users = []
with open("branch_users.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        branch_name, branch_user = line.strip().split(",")
        branch_users.append(branch_user)


# Write branch users to config file.
building_branch_users = []

for line in branch_users:
    if line == "員工編號":
        continue
    line = "edit \"" + line + "\"\n set type radius\n set radius-server \"IDEXpert\"\n" + "next\n"
    building_branch_users.append(line)

with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("config user local\n")

for line in building_branch_users:
    with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write(line)

with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("end\n\n")

time.sleep(1) 
print("分公司申請人員建檔完成\n")


# Take out branch vpn data source from file-branch_vpn.txt.
time.sleep(1)
print(f"設定分公司VPN群組\"{group_choice.upper()}\"設定檔...")

branch_dataSource = []

with open("branch_vpn.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        line = line.strip("\]}")
        line = line.strip("{")

        # Multiple users in the branch_group.
        if "," in line:
            symbolRegex = re.compile(r'[,]')
            new_line = symbolRegex.sub(' ', line)
            if "\'" in new_line:
                symbolRegex = re.compile(r'[\']')
                new_line2 = symbolRegex.sub('\"', new_line)
                branch, group = new_line2.split(": {")
                branch_dataSource.append([branch, group])

        # Only one user in the branch_group.
        elif "," not in line:
            symbolRegex = re.compile(r'[\']')
            single_user = symbolRegex.sub('\"', line)
            single_user = single_user.split(": {")
            branch_dataSource.append(single_user)


# Create branch category from category branch_category.txt.
branch_category = []

with open("branch_category.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip().split(",")
        branch_category.append(line)


# Setup group number clear.
branch_group_clear = []

for devision in branch_category:
    if group_choice.upper() == "A":
        # Excluding the blank group of A.
        if devision[1] == "":
            continue
        group = f"edit \"{devision[1]}\"\n unset member\n next\n"
        branch_group_clear.append(group) 
    elif group_choice.upper() == "B":
        # Excluding the blank group of B.
        if devision[2] == "":
            continue
        group = f"edit \"{devision[2]}\"\n unset member\n next\n"
        branch_group_clear.append(group) 
    else:
        continue

for i in branch_group_clear:
    print(i)

with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("config user group\n")

for line in branch_group_clear:
    with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write(line)

with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("end\n\n")

# Building branch vpn config.
branch_config = []

for branch_vpn_list in branch_dataSource:
    for branch in branch_category:
        if branch[0] in branch_vpn_list[0]:
            if group_choice.upper() == "A":
                group = f"edit \"{branch[1]}\"\n set member {branch_vpn_list[1]}\n next\n"
                branch_config.append(group)
            elif group_choice.upper() == "B":
                group = f"edit \"{branch[2]}\"\n set member {branch_vpn_list[1]}\n next\n"
                branch_config.append(group) 
            else:
                continue
        else:
            continue

with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("config user group\n")

for line in branch_config:
    with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write(line)

with open(f"branch_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("end\n")

time.sleep(1)
print(f"設定完成，檔名為: branch_config_{group_choice.upper()}.txt\n\n")


############################################################

############################################################

# Take out headquater users.
time.sleep(1) 
print("總公司申請人員建檔...")

head_users = []

with open("head_users.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        devision, user = line.strip().split(",")
        head_users.append(user)



# Write headquater users to config file.
building_head_users_account = []

for line in head_users:
    if line == "員工編號":
        continue
    line = "edit \"" + line + "\"\n set type radius\n set radius-server \"IDEXpert\"\n" + "next\n"
    building_head_users_account.append(line)

with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("config user local\n")

for line in building_head_users_account:
    with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write(line)

with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("end\n\n")

time.sleep(1) 
print("總公司申請人員建檔完成\n")


time.sleep(1)
print(f"設定總公司VPN群組\"{group_choice.upper()}\"設定檔...")

# Take out headquater vpn data source from file-head_vpn.txt.
head_dataSource = []

with open("head_vpn.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        line = line.strip("\]}")
        line = line.strip("{")

        # Multiple users in the head_group.
        if "," in line:
            symbolRegex = re.compile(r'[,]')
            new_line = symbolRegex.sub(' ', line)
            if "\'" in new_line:
                symbolRegex = re.compile(r'[\']')
                new_line2 = symbolRegex.sub('\"', new_line)
                devision, group = new_line2.split(": {")
                head_dataSource.append([devision, group])


        # Only one user in the head_group.
        elif "," not in line:
            symbolRegex = re.compile(r'[\']')
            single_user = symbolRegex.sub('\"', line)
            single_user = single_user.split(": {")
            head_dataSource.append(single_user)
        
        # Skip if out of choice.
        else:
            continue


# Create branch category from category file-head_category.txt.
head_category = []

with open("head_category.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip().split(",")
        head_category.append(line)


new_head_category =[]

for i in head_category:
    i[0] = "\"" + i[0] + "\""
    new_head_category.append(i)

# Building vpn config to the head_config_[A/B].txt.

# Setup group number clear.
head_group_clear = []

for devision in new_head_category:
    if group_choice.upper() == "A":
        # Excluding the blank group of A.
        if devision[1] == "":
            continue
        group = f"edit \"{devision[1]}\"\n unset member\n next\n"
        head_group_clear.append(group) 
    elif group_choice.upper() == "B":
        # Excluding the blank group of B.
        if devision[2] == "":
            continue
        group = f"edit \"{devision[2]}\"\n unset member\n next\n"
        head_group_clear.append(group) 
    else:
        continue

with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("config user group\n")

for line in head_group_clear:
    with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write(line)

with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("end\n\n")

# Setup add headquarter employee to devision group.
head_config = []

for head_vpn_list in head_dataSource:
    for devision in new_head_category:
        if devision[0] == head_vpn_list[0]:
            if group_choice.upper() == "A":
                group = f"edit \"{devision[1]}\"\n set member {head_vpn_list[1]}\n next\n"
                head_config.append(group) 
            elif group_choice.upper() == "B":
                group = f"edit \"{devision[2]}\"\n set member {head_vpn_list[1]}\n next\n"
                head_config.append(group) 
            else:
                continue

with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("config user group\n")

for line in head_config:
    with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write(line)

with open(f"head_config_{group_choice.upper()}.txt", "a+", encoding="utf-8") as f:
        f.write("end\n")

time.sleep(1)
print(f"設定完成，檔名為: head_config_{group_choice.upper()}.txt")