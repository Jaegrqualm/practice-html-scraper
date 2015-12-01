from lxml import html
import requests

#get main page
main_page = requests.get('http://distrowatch.com')
tree = html.fromstring(main_page.content)

#read top 100 into lists
ranks = tree.xpath('//th[@class="phr1"]/text()')
names = tree.xpath('//th[@class="phr2"]//a[@href=/text()')
scores = tree.xpath('//th[@class="phr3" @title="Yesterday: "/text()]')

print(ranks)
print(names)
print(scores)