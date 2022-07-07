import urllib.parse
import urllib.request

# urllib.parse.quote（）

searchWord = urllib.parse.quote("蝙蝠侠")
url = 'https://www.sogou.com/web?query=' + searchWord
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

# print(url)
requestObj = urllib.request.Request(url=url, headers=headers)
resp = urllib.request.urlopen(requestObj)
context = resp.read().decode("utf-8")
print(context)
