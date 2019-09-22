import paramiko

#服务器信息，主机名（IP地址）、端口号、用户名及密码

hostname = "192.168.92.134"
port = 22
username = "test"
password = "test"

#创建SSH对象  
client = paramiko.SSHClient()
#自动添加策略，保存服务器的主机名和密钥信息
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
client.connect(hostname, port, username, password, compress=True)

# 执行linux命令
# stdin, stdout, stderr = ssh.exec_command('ls')  # 執行命令
# result = stdout.read()  # 獲取命令結果
# print (str(result,encoding='utf-8'))
stdin, stdout, stderr = client.exec_command('ls -al /home')
result = stdout.readlines()
for line in result:
    print(line.strip('\n'))
stdin, stdout, stderr = client.exec_command('netstat -a | grep ssh')
result = stdout.readlines()
for line in result:
    print(line.strip('\n'))


