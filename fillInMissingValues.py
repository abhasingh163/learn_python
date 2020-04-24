def fillInMissingValues(arr):
	val = -1
	for i in range(len(arr)):
		if(arr[i] != -1):
			val = arr[i]
		else:
			arr[i] = val
	return arr

arr=[6,7,8,-1,-1,3,4,5,6,-1]
print(fillInMissingValues(arr))