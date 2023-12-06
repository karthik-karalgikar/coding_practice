def lengthOfLastWord(s):
    wordList = s.split()
    lastWord = wordList[-1]
    return len(lastWord)

s = "Hello World"
result = lengthOfLastWord(s)
print(result)

'''
TRACING:
First I create a function called lengthOfLastWord with one parameter, 
that is, 's' which is the input string
Next, I use the split() function to convert the string into a list
and I will store the value into a variable called 'wordList'
For example, the string is "Hello World". 
When I use the split function, the output will be ->
["Hello", "World"]

Next I will access the last element of the list using wordList[-1] 
and store that value in a variable called lastWord.
Here, the last element of the list wordList is "World"
So, lastWord will have the value "World".

Finally I will return the length of lastWord(length of the word
"World" is 5), which is the expected
output.
'''
