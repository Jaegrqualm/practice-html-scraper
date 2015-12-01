#test stuff without having to download 100 webpages
from lxml import html
import requests


distro_page = requests.get('http://distrowatch.com/table.php?distribution=lxle')
tree = html.fromstring(distro_page.content)

distro_data = tree.xpath('//tr/td[1]/text()')
#print(distro_data[148])
print( len(distro_data))

#distro_data = tree.xpath('//tr/td[1]/text()')

distro_info = []
for y in range(len(distro_data) -  61, len(distro_data) - 8,1):
	distro_info.append(distro_data[y])

print(distro_info)




'''
#remove useless data
for y in range(156,148):
#int y = 156, y >= 148, y--:
	distro_data.pop(y)
	y+=1

for y in range(95,0):
	distro_data.pop(y)
	y+=1
		
print(distro_data)
'''