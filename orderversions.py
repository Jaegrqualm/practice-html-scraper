from copy import deepcopy
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
count = 0

for x in range(len(distro_info[0])):
	temp = []
	count+=1
	#count2=0
	for y in range(len(distro_info)):
		temp.append(distro_info[y][x])
		#count2+=1
		#print(count2)
	#print (temp)

	#print (count)
	
	package_info.append(temp)
	

#write the values as ordinal integers
count = 0
pairs=[]
for x in package_info:

	pair = {}
	
	setx = set(x)
	sorted_setx = sorted(setx)
	
	setx.clear()
	
	i=0
	for y in sorted_setx:
		pair[y] = i
		i+=1
	pairs.append(deepcopy(pair))
	pair.clear()
		
for m in range(len(distro_info[0])):
	#print(pairs[m])
	for n in range(len(distro_info)):
		#print(pairs[n])
		distro_info[n][m] = pairs[m][distro_info[n][m]]
	


		

	
	
f = open('/home/roger/Documents/python/distrowatchdata.csv','w')	
for x in distro_info:
	for y in x:
		f.write(','+str(y))
	f.write('\n')

f.close()