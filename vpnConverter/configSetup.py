#! python3
import paramiko
import time
import getpass
import sys



print(r'''

    =========== 歡迎使用防火牆VPN群組設定工具 ===========
    
    使用前請先整理好設定檔，避免組態設定錯誤，
    請輸入下周啟用VPN政策的群組設定檔：

    (A)：A群組
    (B)：B群組


    或輸入"Q"結束程式
    
''')


# Function Switch.
while True:
    choice = input("請輸入啟用群組代號：")
    print("\n您所選擇的是：", choice.upper())
    if choice.upper() == "A":
        config_class = "A"
        print("\n")
        break
    elif choice.upper() == "B":
        config_class = "B"
        print("\n")
        break
    elif choice.upper() == "Q":
        print("程式即將終止...感謝您的使用，我們下次見")
        time.sleep(1)
        sys.exit()
    else:
        print("您輸入的代號不正確，請重新輸入\n")
        continue


# Read config file.
head_config_file = "head_config_" + config_class +".txt"
branch_config_file = "branch_config_" + config_class + ".txt"

head_config = []
with open(head_config_file, "r", encoding="utf-8") as f:
    for line in f.readlines():
        head_config.append(line)


branch_config = []
with open(branch_config_file, "r", encoding="utf-8") as f:
    for line in f.readlines():
        branch_config.append(line)


# Connect to Firewall system with Login authentication.
print("總公司防火牆系統登入中....\n")

username = input("請輸入管理員帳號: ")
password = getpass.getpass('請輸入管理員密碼: ')

print("\n系統連線中，請稍後...\n")
time.sleep(1)

host_ip = '30.0.0.10'
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host_ip, username=username, password=password)

print("成功連線到防火牆系統 ", host_ip)


# Setup from config file.
command = ssh_client.invoke_shell()

print("設定作業執行中...")
time.sleep(1)

# Branch
print("設定分店人員VPN，讀取設定檔：", branch_config_file)
time.sleep(1)

# command.send("config user group\n")
for line in branch_config:
    if "\n" not in line:
        command.send(f"{line}\n")
    else:
        command.send(line)
# command.send("end\n")

print("分店人員VPN群組設定已完成\n")
time.sleep(1)

# Headquarter
print("設定總公司人員VPN，讀取設定檔：", head_config_file)
time.sleep(1)

# command.send("config user group\n")
for line in head_config:
    if "\n" not in line:
        command.send(f"{line}\n")
    else:
        command.send(line)
# command.send("end\n")

print("總公司人員VPN群組設定已完成\n")
time.sleep(1)

print("設定作業已執行完畢，設定記錄匯出中，請稍後...\n")
time.sleep(2)

output = command.recv(65535)
result = output.decode('ascii')
with open("config_log.txt", 'a+', encoding="utf-8") as f:
    f.write(result)

print("記錄已匯出到config_log.txt，請開啟檢視\n")

ssh_client.close
