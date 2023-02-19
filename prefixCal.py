#! python3
# Ｕnit 26: 簡易前敘式計算機

def prefix(to_solve):
    op, num_1, num_2 = to_solve.split()
    print(num_1, op, num_2)


prefix('+ 2 3')


# 設定計算式函式
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# 簡易計算機

def prefix_cal(to_solve):
    op, num_1, num_2 = to_solve.split()
    operation = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    num_1 = int(num_1)
    num_2 = int(num_2)
    return operation[op](num_1, num_2)


result = prefix_cal('/ 2 3')
print(result)

# 進階版：Lambda, 不用預設計算式

def prefix_cal(to_solve):
    op, num_1, num_2 = to_solve.split()
    operation = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    num_1 = int(num_1)
    num_2 = int(num_2)
    return operation[op](num_1, num_2)

test_cal = prefix_cal('+ 5 6')
print(test_cal)

# 進階版：Operator, 直接套用內建函式
import operator

def prefix_cal(to_solve):
    op, num_1, num_2 = to_solve.split()
    operation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    num_1 = float(num_1)
    num_2 = float(num_2)
    return operation[op](num_1, num_2)

test_cal = prefix_cal('+ 5 6')
print(test_cal)


# 完整版：寫一個能計算較長前序式的計算函式
# 範例：(2 + 4) * 3 / (1 + 5)
import operator

def prefix_cal(to_solve):
    # 計算式
    operation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    # 檢查是否為整數或浮點數
    def isnumber(num):
        return num.replace('.', '').isnumeric()

    items = to_solve.split()    # 將字串拆成清單

    # 當字元數剩一位求解
    while len(items) > 1:
        for i in range(len(items) - 2):         # 最末碼為n-1, 保留最末碼為n-2
            # 每次取出3個字元
            op, num_1, num_2 = items[i:i + 3]   # list[0:3] = list[0,1,2], 最末碼為n-1 = 3-1 = 2

            # 符合前敘式的格式就跳出迴圈
            if op in operation.keys() and isnumber(num_1) and isnumber(num_2):
                print(f'{op} {num_1} {num_2}')
            
                # 處理前敘式運算
                num_1 = float(num_1)
                num_2 = float(num_2)

                # 重組清單,保留i之前,i+3之後,插入運算回傳值
                items = items[:i] + [str(operation[op](num_1, num_2))] + items[i + 3:] 

                break

    
    return float(items[0])  # 清單最後一碼 = 1-1 = 0

test_cal = prefix_cal('/ * + 2 4 3 + 1 5')
print(test_cal)