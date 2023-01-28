def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.") # Debug訊息

    return dividend /divisor


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]

# 錯誤處理程序: 
# try程式執行, except錯誤處理, else都沒有錯誤時才執行, finally不論有無錯誤都要執行
try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError as e:
    print(e)
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")