def avgWordLength(sentence):
	words = sentence.split()
	return sum(len(word) for word in words) / len(words)

sentence = "Hi my name is Bob"
print(avgWordLength(sentence))