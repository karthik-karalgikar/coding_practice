# Count the occurrences of each word in a given sentence

def count_words(str):
  counts = dict()
  words = str.split()

  for word in words:
      if word in counts:
         counts[word] += 1
      else:
         counts[word] = 1

  return counts

print( count_words('the quick brown fox jumps over the lazy dog.'))

# Sample Output:
# { 'the': 2, 
#   'jumps': 1, 
#   'brown': 1, 
#   'lazy': 1, 
#   'fox': 1, 
#   'over': 1, 
#   'quick': 1, 
#   'dog.': 1} 