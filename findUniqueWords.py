#Given two Sentences, construct an array that has the words that appear in one sentence and not the other.

# Function to return all uncommon words or unique words from 2 given strings

def findUniqueWords(str1, str2): 
  
    count = {}       

    for word in str1.split(): 
        count[word] = count.get(word, 0) + 1
      
    for word in str2.split(): 
        count[word] = count.get(word, 0) + 1
  
    return [word for word in count if count[word] == 1] 
  
str1 = "Python is the best language"
str2 = "Commiting Python code to git was best idea"
print(findUniqueWords(str1, str2))