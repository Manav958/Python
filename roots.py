a=float(input("number"))
c=a**(1/2)
print (c)

'''input
130P 120C 110F
4P 9C 2F|4P 3C 2F|7P 1C 3F
'''
list1=[]
req = input().split()
for item in req:
	if item[-1]=='P':
		proteinsRequired = int(item[:len(item)-1])
	elif item[-1]=='C':
		carbohydratesRequired = int(item[:len(item)-1])
	else:
		fatsrequired = int(item[:len(item)-1])
items = input().split('|')
givenItems = []
for item in items:
	givenItems.append([0, 0, 0])
	itemm=item.split()
	for i in itemm:
		if i[-1]=='P':
			givenItems[-1][0] = int(i[:len(i)-1])
		elif i[-1]=='C':
			givenItems[-1][1] = int(i[:len(i)-1])
		else:
			givenItems[-1][2] = int(i[:len(i)-1])
print(givenItems, proteinsRequired, carbohydratesRequired, fatsrequired)

idx=-1
final=[]
for i in range(0, 1000):
	current=[0, 0, 0]
	for item in givenItems:
		current[0]+=i*item[0]
		current[1]+=i*item[1]
		current[2]+=i*item[2]
	if current[0]>proteinsRequired or current[1]>carbohydratesRequired or current[2]>fatsrequired:
		idx = i-1
		final=final[-1]
		break
	else:
		final.append(current)
print(idx, final)
potential = []
for i in range(0, 2**(len(givenItems))):
	b='0'*(len(givenItems)-len(bin(i)[2:]))+bin(i)[2:]
	print('chk', b)
	temp = [_ for _ in final]
	for j in range(0, len(givenItems)):
		if b[j]=='1':
			temp[0]+=givenItems[j][0]
			temp[1]+=givenItems[j][1]
			temp[2]+=givenItems[j][2]
	if temp[0]>proteinsRequired or temp[1]>carbohydratesRequired or temp[2]>fatsrequired:
		continue
	else:
		potential.append([temp, b])
print(potential)
potential.sort()
potential.reverse()
ekdumFinal=potential[0]
final=[proteinsRequired-ekdumFinal[0][0], carbohydratesRequired-ekdumFinal[0][1], fatsrequired-ekdumFinal[0][2]]
print(*final)
