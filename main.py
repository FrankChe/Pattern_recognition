'''
top-k pattern mining
'''

def importData(name) :
	# import data from name
	try :
		fo = open(name)
		data = [lst.strip().split(',') for lst in fo.readlines()]
		return [t[1:5] for t in data], [t[0] for t in data]
	except Exception, e :
		print e
	finally :
		fo.close()
# --- end of importData ---

class Pattern :
	# attributes
	pattern = dict()

	# methods
	def __init__(self, *arr) :
		for p, v in arr :
			self.pattern[p] = v

	def disp(self) :
		for k in self.pattern.keys() :
			print 'attr'+str(k), '=', self.pattern[k]

	def frequency(self, dataset) :
		num = 0
		for i in range(len(dataset)) :
			matched = 0
			for j in range(len(dataset[i])) :
				if (j in self.pattern.keys()) :
					if (self.pattern[j] == dataset[i][j]) :
						matched += 1
			if matched == len(self.pattern.keys()) :
				num += 1
		return 1.0*num/len(dataset)

	def globaldiff(self, dataset, label) :
		posi, nage = [], []
		for i in range(len(dataset)) :
			if label[i] == 'e' :
				posi.append(dataset[i])
			else :
				nage.append(dataset[i])
		return self.frequency(posi) - self.frequency(nage)

	def localdiff(self, dataset, label, ptdict) :
		posi, nage = [], []
		for i in range(len(dataset)) :
			if label[i] == 'e' :
				posi.append(dataset[i])
			else :
				nage.append(dataset[i])
		posifrq, nagefrd = self.frequency(posi), self.frequency(nage)

	def toString(self) :
		s = ''
		for i in self.pattern.keys() :
			s += str(i) + self.pattern[i]
		return s


if __name__ == '__main__' :
	dataset, label = importData('data.txt')
	p1 = Pattern([0, 'x'], [1, 's'], [2, 'w'])
	p1.disp()
	print p1.globaldiff(dataset, label)
	print p1.toString()
	print label
	#print len(dataset)
