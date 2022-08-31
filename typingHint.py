#! python3
# Understand typing hint
from typing import List


# 比照Swift設定傳入值型別與回傳值型別
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

x = [1,2,3]

list_avg(x)
