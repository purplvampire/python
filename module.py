# 建立自己的模組化工具
# 設定自己的模組資料夾
import sys as system
# 列印模組工具的收尋路徑
print(system.path)
print('--------------------------------------------------------------')
# 新增模組資料夾到收尋路徑中
system.path.append('modules')
# 列印模組工具的收尋路徑
print(system.path)
# 載入自己存放在modules資料夾的模組工具程式檔
# 呼叫測試模組變數
import testModule
result = testModule.test()
print(result)
# 呼叫geometry的distance函式
import geometry
result = geometry.distance(1,1,2,2)
print(result)

# 可建立封包資料夾用以分類不同的模組工具
# 在封包資料夾下方建立一個__init__.py的空程式即可
# 存取封包資料夾下的模組與函式
import geometryFolder.point as point    # 建立封包.模組別稱
result = point.distance(1,2)            # 呼叫函式(變數)
print(result)
