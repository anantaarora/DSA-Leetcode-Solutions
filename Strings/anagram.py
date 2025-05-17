# Given an array of strings, remove each string that is an anagram of an earlier string, 
# then return the remaining array in sorted order.


words = ['code', 'doce', 'ecod', 'framer', 'frame']
result = []
seen = set()
for word in words:
  sorted_word = ''.join(sorted(word))
  if sorted_word not in seen:
    seen.add(sorted_word)
    result.append(word)
result.sort()
print(result)