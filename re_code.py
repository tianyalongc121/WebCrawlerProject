# re 正则表达式

import re

content = 'Xiaoshuaib has 100 bananas'
result = re.match('^Xi.*?(\d+)\s.*s$', content)

print(result.group(1))

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
res = re.findall('Xi.*?(\d+)\s.*?s;', content, re.S)
print(res)
