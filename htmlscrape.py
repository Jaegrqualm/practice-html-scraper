from lxml import html
import requests
import sys

#get main page
main_page = requests.get('http://distrowatch.com')
tree = html.fromstring(main_page.content)

#read top 100 into lists
ranks = tree.xpath('//th[@class="phr1"]/text()')
names = tree.xpath('//td[@class="phr2"]//a/@href')
scores = tree.xpath('//td[@class="phr3"]/text()')

print(ranks)
print(names)
print(scores)

distros_info = []
count = 0
#get the data for each distro
for x in names:
	URL = 'http://distrowatch.com/table.php?distribution=' + x
	distro_page = requests.get(URL)
	tree2 = html.fromstring(distro_page.content)
	distro_data = tree2.xpath('//tr/td[1]/text()')
	#remove useless data
	distro_info = []
	for y in range(len(distro_data) -  61, len(distro_data),1):
		distro_info.append(distro_data[y])
	
	distros_info.append(distro_info) 
		
	#get the per-distro data right	
	output = ''
	for y in range(len(distros_info[count])):
		output = output + distros_info[count][y] + ','
	
	#write it all to a file
	with open('/home/roger/Documents/python/distrowatchdata.csv','a') as f:		
		f.write(ranks[count] + ',' + names[count] + ',' + scores[count] + ',' + output + '\n')

	count+=1
	print('done: ' + str(count))

	

		

	

		

		