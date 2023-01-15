# 範例: 建立密碼驗證器
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "1234"),
]

# dict_comprehensions
username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])

# 完整作法
for user in users:
    if user[1] == "Bob":
        print(user)


# 帳密驗證
username_input = input("Enter username: ")
password_input = input("Enter password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Correct!")
else:
    print("Incorrect!")