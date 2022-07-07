import urllib.request


# url = 'https://www.12306.cn/index/index.html'
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-07-04&leftTicketDTO.from_station=IOQ&leftTicketDTO.to_station=CIN&purpose_codes=ADULT'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)