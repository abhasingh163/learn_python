#You have a 2-D array of friends like [[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]]
#Write a function that creates a dictionary of how many friends each person has. People can have 0 to many friends. However, there won't be repeat relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship.

def countFriends(friendList):
	if(friendList == None):
		return {}
	
	mydict = {}
	for friend in friendList:
		mydict[friend[0]] = mydict.get(friend[0], 0)
		if(len(friend) == 2):
			mydict[friend[0]] = mydict.get(friend[0], 0) + 1
			mydict[friend[1]] = mydict.get(friend[1], 0) + 1
	
	return mydict
	
friendList = [['A','B'],['B','C'],['C','D'],['A','D'],['A','E'],['J'],['M'],['N','O']]
print(countFriends(friendList))
