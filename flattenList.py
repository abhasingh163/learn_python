def flattenList(mylist):
	for val in mylist:
		if(isinstance(val,list)):
			for nestedval in flattenList(val):
				yield nestedval
		else:
			yield val

mylist=[1,2,[3,4,[5,6,1],1,8],9,[10,21]]
print(list(flattenList(mylist)))
flattenList(mylist)