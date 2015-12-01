#change the version numbers into ordinal integers.
#data currently requires manual fixing before using this.

#read data into list
f = open('/home/roger/Documents/python/distrowatchdata.csv','r')
distro_info=[]
for line in f:
	distro_info.append(line.split(','))
f.close()

#get the data in the right order
package_info = []
for x in range(len(distro_info[0])):
	temp = []
	for y in range(len(distro_info)):
		temp.append(distro_info[y][x])
	
	package_info.append(temp)
	
#write the values as ordinal integers
for x in package_info:
	setx = set(x)
	sorted_setx = sorted(setx)
	
	pairs = {}
	i=0
	for y in sorted_setx:
		pairs[i] = y
		i+=1
	print(pairs)
	
	for n in range(len(distro_info[0])):
		for m in range(len(distro_info) - 1):
			distro_info[m+1][n] = pairs[distro.info[m+1][n]]
	
	
f = open('/home/roger/Documents/python/distrowatchdata.csv','w')	

		