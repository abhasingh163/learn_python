def countWords(sentence):
	assert len(sentence)>1
	return sum(1 for word in sentence.split())
	#return len(sentence.split())

sentence="Hello, Good Morning. This is Manu Batham!!"
print(countWords(sentence))