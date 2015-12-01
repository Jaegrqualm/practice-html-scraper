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
for x in range(len(distro_info[0])-3):
	temp = []
	for y in range(len(distro_info)-1):
		temp.append(distro_info[y+1][x+3])
	
	package_info.append(temp)
	

#write the values as ordinal integers
count = 0
pairs = {}
for x in package_info:
	setx = set(x)
	sorted_setx = sorted(setx)
	
	setx.clear()
	
	i=0
	for y in sorted_setx:
		pairs[y] = i
		i+=1
		
	print(pairs)
	for n in range(len(distro_info[0])-1):
		#print(distro_info[n+3])
		distro_info[n+1][count+3] = pairs[distro_info[n+1][count+3]]
		
	pairs.clear()
	count+=1
	
	
f = open('/home/roger/Documents/python/distrowatchdata.csv','w')	
for x in distro_info:
	for y in x:
		f.write(str(y) + ',')
	f.write('\n')

f.close()