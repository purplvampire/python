#! python3

import time
import re

'''  建立分公司VPN人員名單

讀取分公司申請名單並按公司別分類

'''

print(
    '''
    =====歡迎使用分公司VPN分類系統=====

    使用前請先準備好分公司VPN人員申請名單
    並確保營業員與後台都整併再一起
    將檔名存成branch_users.txt
    放在執行檔所在目錄

    謝謝您的配合，並祝您順利完成作業
    '''

)

time.sleep(1)

# 讀取分公司清單
branch_list = []
# with open("branch_list.txt", "r", encoding="utf-8") as f:
#     for list in f.readlines():
#         list = list.strip()
#         branch_list.append(list)

with open("branch_category.txt", "r", encoding="utf-8") as f:
    for list in f.readlines():
        list = list.strip().split(",")
        branch_list.append(list)

print("讀取分公司申請人清單...")

# 將分公司使用者申請表存成清單
def branch_users():
    branch_users = []
    # 讀取分公司申請名單
    with open("branch_users.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line == "\n":
                continue
            # 逐行將字串轉為[分公司,原編]清單
            branch, num = line.strip().split(",")
            branch_users.append([branch, num])
    return branch_users

branch_users = branch_users()


time.sleep(1)

print("分類進行中...")

# 將分公司使用者清單依公司別分類

def to_separate_users(branch):
    branch_dic = {}
    group_users = []
    # 逐次處理分公司人員清單
    for list in branch_users:
        # 建立判斷式，若申請名單中的分公司有在分公司類別，則將原編加入群組，然後更新{分公司:群組}字典
        if branch in list[0]:
            group_users.append(list[1])
            # 處理掉重複的使用者原編，建立部門VPN字典
            branch_dic[branch] = set(group_users)
    return branch_dic

time.sleep(1)


# 將分類好的分店使用者存檔
def store_vpn_list():
    for branch in branch_list:
        users = to_separate_users(branch[0])
        with open("branch_vpn.txt", "a+", encoding="utf-8") as f:
            f.write(str(users) + "\n")
    print("檔案轉存中...")

store_vpn_list()

time.sleep(1)

print('''

    檔案已完成，檔名為\"branch_vpn.txt\"，請開啟檢視，謝謝您的使用。

    另外，請不要忘了使用設定檔轉換工具建立分公司VPN群組設定檔，
    以節省您寶貴的設定時間。

''')



