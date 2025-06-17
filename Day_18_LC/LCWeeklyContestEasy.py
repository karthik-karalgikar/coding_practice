'''Generate Tag for Video Caption

Easy
3 pt.
You are given a string caption representing the caption for a video.
The following actions must be performed in order to generate a valid tag for the video:
Combine all words in the string into a single camelCase string prefixed with '#'. 
A camelCase string is one where the first letter of all words except the 
first one is capitalized.
 All characters after the first character in each word must be lowercase.

Remove all characters that are not an English letter, except the first '#'.
Truncate the result to a maximum of 100 characters.

Return the tag after performing the actions on caption.
'''

def generatetag(caption):
    a = caption.split()
    if not a:
        return "#"
    
    a[0] = a[0].lower()
    for i in range(1, len(a)):
        a[i] = a[i].capitalize()

    concatStr = "#" + ''.join(a)

    return concatStr

caption = "Leetcode daily streak achieved"
result = print(generatetag(caption))

