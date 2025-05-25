def lengthOfLastWord(s):
    wordList = s.split()
    lastWord = wordList[-1]
    return len(lastWord)

s = "my name is karthik"
result = lengthOfLastWord(s)
print(result)