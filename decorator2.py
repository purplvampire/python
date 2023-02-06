# 學習裝飾器與閉包的使用
import functools


user = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

get_admin_password = make_secure(get_admin_password)

print(get_admin_password())

# 上述可置換為下方語法

# decorator function
def make_secure(func):
    @functools.wraps(func)  # 置換成套用的函式
    def secure_function(*args, **kwargs):  # 套用萬用參數以應對不同的function參數值
        if user["access_level"] == "guest":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."
            
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))

# 進階用法,decorator套用參數, 順序會是先執行decorator, 再將return的結果套用到function中
def make_secure(access_level):  # 用於呼叫裝飾器的裝飾器
    def decorator(func):        # 這個才是裝飾器
        @functools.wraps(func)  # 置換成套用的函式
        def secure_function(*args, **kwargs):  # 套用萬用參數以應對不同的function參數值
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."
                
        return secure_function  # 裝飾器結果2
    
    return decorator            # 裝飾器結果1

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"



@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())

user = {"username": "jose", "access_level": "guest"}
print(get_dashboard_password())
