import urllib.request
import jsonpath
import json

url = 'https://www.zhipin.com/wapi/zpgeek/common/data/citysites.json'
request = urllib.request.urlopen(url)
content = request.read().decode('utf-8')
result = jsonpath.jsonpath(json.loads(content), '$..name')
print(result)

