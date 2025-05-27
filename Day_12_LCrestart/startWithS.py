'''
Print only the words that start with the letter s in a sentence
'''
st = "Print only the words that start with the letter s in a sentence"

for word in st.split():
    if word[0] == "s":
        print(word)