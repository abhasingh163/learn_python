def findAbsMinDiff(arr):
  arr = sorted(arr)
  arrlen = len(arr)
  if (arrlen > 1):
    diff = abs(arr[1] - arr[0])
    for i in range(1, len(arr)-1):
      if (abs(arr[i+1] - arr[i]) < diff):
        diff = abs(arr[i+1] - arr[i])
    return diff
  return False

arr=[8,5,-7,1,12,3]
print(findAbsMinDiff(arr))
