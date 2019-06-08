import json
# Change Json to Python
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
# Change Python to Json
pythonValue = {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)

