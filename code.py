#coding=utf-8
#!/usr/bin/python

import math

def Min(no1,no2):
	if no1 < no2:
		return no1
	else:
		return no2
#store 3 class total numbers
# winNo, loseNo, drawNo

# globalDiff   store global difference num and assumping the pattern is attr0 = b and attr1 = b
##假设前景集合为win，其余为背景集合


lists = []
fo = open("connect-4.data","r+")
str = fo.readlines()
for str_ in str:
	lists.append(str_.strip().split(','))
print lists[0][len(lists[0])-1]

i = 0
winNo = 0
loseNo = 0
drawNo = 0
length = len(lists[0])

while i < len(lists):
	if lists[i][length-1] == "win":
		winNo += 1
	elif lists[i][length-1] == "loss":
		loseNo += 1
	elif lists[i][length-1] == "draw":
		drawNo += 1
	else:
		pass
	i += 1

print winNo
print loseNo
print drawNo

globalSumFront = 0
globalSumBack = 0
i = 0
while i < len(lists):
	if lists[i][0] == 'b' and lists[i][1] == 'b':
		if lists[i][length-1] == 'win':
			globalSumFront += 1
		else:
			globalSumBack += 1
	i += 1

print "globalSumFront = ",globalSumFront
print "globalSumBack = ",globalSumBack

globalFrontRate = float(globalSumFront) / winNo
globalBackRate = float(globalSumBack) / (loseNo + drawNo)

print "globalFrontRate = ",globalFrontRate
print "globalBackRate = ",globalBackRate

globalDiff = math.fabs(globalFrontRate - globalBackRate)
print "globalDiff = ",globalDiff

#partitionDiff
# Q1sum,Q2sum
Q1Frontsum = 0
Q2Frontsum = 0
Q1Backsum = 0
Q2Backsum = 0
i = 0
while i < len(lists):
	if lists[i][0] == 'b':
		if lists[i][length-1] == 'win':
			Q1Frontsum += 1
		else:
			Q1Backsum += 1
	elif lists[i][1] == 'b':
		if lists[i][length-1] == 'win':
			Q2Frontsum += 1
		else:
			Q2Backsum += 1
	else:
		pass
	i += 1

Q1FrontsumRate = float(Q1Frontsum) / winNo
Q1BacksumRate = float(Q1Backsum) / (loseNo + drawNo)
Q2FrontsumRate = float(Q2Frontsum) / winNo
Q2BacksumRate = float(Q2Backsum) / (loseNo + drawNo)

print "Q1FrontsumRate = ",Q1FrontsumRate
print "Q1BacksumRate = ",Q1BacksumRate
print "Q2FrontsumRate = ",Q1FrontsumRate
print "Q2BacksumRate = ",Q1BacksumRate


partitionDiff = Min((globalFrontRate/Q1FrontsumRate - globalBackRate/Q1BacksumRate),(globalFrontRate/Q2FrontsumRate - globalBackRate/Q2BacksumRate))
print "partitionDiff = ",partitionDiff

#已知：
#在前景集合中频率 globalFrontRate 大于某个阈值 
#在局部差异度大于 partitionDiff 某个阈值
#求：
#报告前K个全局差异度 globalDiff 最大的模式













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


#print single
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