import json

import jsonpath

import urllib.request

# checkurl = "$.store.book[*]"
#
# books = json.load(open('book_example.json', 'r', encoding='utf8'))
# print(books)
#
# book_author_list = jsonpath.jsonpath(books,'$.store.book[*].author')
# print(book_author_list)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'cookie': 'miid=536765677517889060; t=78466542de5dbe84715c098fa2366f87; cookie2=11c90be2b7bda713126ed897ab23e35d; v=0; _tb_token_=ee5863e335344; cna=jYeFGkfrFXoCAXPrFThalDwd; xlly_s=1; tfstk=cdlVBIX7qIdVC-V6pSNwCDgVlVEAa8mxXMa3nx9gjUzPOZeuYsAcXzbAiJwAzG2c.; l=eBxbMUncLj6r4x9hBO5aourza77T6BAb4sPzaNbMiInca6BOT3r6QNCnaDoy7dtjgtCxretPp0kihRLHR3xg5c0c07kqm0JExxvO.; isg=BHBwrClf5nUOJrpxMvRIOGsqQT7CuVQDlydQ-WrHREsaJRDPEsmVk5EbfS1FtQzb',
    'referer': 'https://dianying.taobao.com/',
    'content-type': 'text/html;charset=UTF-8'
}


def create_request():
    res_obj = urllib.request.Request(
        url="https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1644570795658_173&jsoncallback=jsonp174&action=cityAction&n_s=new&event_submit_doGetAllRegion=true",
        headers=headers)
    return res_obj


def get_context(req_obj):
    resp = urllib.request.urlopen(req_obj)
    origin_context = resp.read().decode('utf-8')
    result = origin_context.split('jsonp174(')[1].split(')')[0]
    return result


def download_and_parse(context):
    with open('jsonpath_淘票票案例.json', 'w', encoding='utf-8') as fp:
        fp.write(context)


def parse_json():
    obj = json.load(open('jsonpath_淘票票案例.json', mode='r', encoding='utf-8'))
    region_name_list = jsonpath.jsonpath(obj, '$..regionName')
    print(region_name_list)
    print(len(region_name_list))


if __name__ == '__main__':
    req_obj = create_request()
    context = get_context(req_obj)
    download_and_parse(context)
    parse_json()
