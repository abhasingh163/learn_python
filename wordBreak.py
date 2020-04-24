#Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. 

def wordBreak(wordList, word): 
    if word == '': 
        return True
    else: 
        wordLen = len(word) 
        return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)]) 