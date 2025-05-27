'''
Given a sentence, return a sentence with the words reversed
'''

def sentence(text):
    wordlist = text.split()
    reverse_word = wordlist[::-1]
    print(reverse_word)

    return ' '.join(reverse_word)

text = "My name is Karthik"
res = sentence(text)
print(res)
