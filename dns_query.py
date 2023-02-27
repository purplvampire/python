#! python3
# 用來處理DNS主機查詢IP資料
query_text = input("Please enter IP file:")

query_ip = []
with open(query_text, "r") as f:
    for line in f.readlines():
        ip = line.strip().split()
        # print(ip)
        if "181" in query_text:
            ip, _ = ip[5].split("#")
        else:
            ip, _ = ip[3].split("#")
        query_ip.append(ip)

query_ip = set(query_ip)


def convert(query_ip):
    for ip in query_ip:
        print(ip)

convert(query_ip)