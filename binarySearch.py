def toTwenty():
	for number in range(1,21):
		return list((number))
		

def toForty():
	for number in range(2,42,2):
		return list((number))

def toOneThousand():
	for number in range(10,1010,10):
		return list((number))



def search_to20(x):
	numb_range=list(range(x+1))
	count=1
	for i in numb_range:
		count-=1
		print ('Count:{}'.format(count-1))
		print('Index:{}'.format(numb_range.index(x)))
		print('Length of List:{}'.format(len(numb_range)))
		print('List:{}'.format(numb_range))

def search_to40(x):
	numb_range=list(range(2,x+2,2))
	count=1
	for i in numb_range:
		count-=1
		print ('Count:{}'.format(count-1))
		print('Index:{}'.format(numb_range.index(x)))
		print('Length of List:{}'.format(len(numb_range)))
		print('List:{}'.format(numb_range))

def search_to1000(x):
	numb_range=list(range(x+10))
	count=1
	for i in numb_range:
		count-=1
		print ('Count:{}'.format(count*-1))
		print('Index:{}'.format(numb_range.index(x)))
		print('Length of List:{}'.format(len(numb_range)))
		print('List:{}'.format(numb_range))
		
search_to20(19)
search_to40(28)
search_to1000(100)


