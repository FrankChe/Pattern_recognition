#coding = utf-8

# list1 = []
# list1.append(1)
# print list1
input_ = []
single = []
#lists [[] for i in range()]

fo = open("connect-4.data","r+")
input_ = fo.readlines()

for line in input_:
	del single[:]
	i = 0
	temp = line.split(",")
	if i == 0:
		print temp
		break
	# while i<len(line):
		
	# 	if line[i] == "d":
	# 		single.append("draw")
	# 		i = i+1
	# 		break
	# 	if line[i] == "w":
	# 		single.append("win")
	# 		i = i+1
	# 		break
	# 	if line[i] == "lose":
	# 		single.append("lose")
	# 		i = i+1
	# 		break
	# 	if line[i] != "," and line[i] != "\n":
	# 		single.append(line[i])
	# 	i = i+1


print single
# for line in input_:
# 	single = line
# 	print single[1]
# 	i = 0
# 	while i<len(single):
# 		if single[i] == ",":
# 	 		print single[i]
# 	 		del single[i]
# 	 	i = i+1
# 	print single

#print list1
# length = len(str)
# print length
# i = 0
# while i < length:
# 	list1.append(str[i])
# 	i = i+2
# print list1

fo.close()