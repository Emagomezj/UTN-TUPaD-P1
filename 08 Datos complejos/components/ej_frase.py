import re
from collections import Counter
frase = input('Ingrese una frase').strip().lower()
limit = r"[;, ]"
words = [w for w in re.split(limit, frase) if w != ' ' and w!='']
unique_words = set(words)
print(words)
words_dict = {w:words.count(w) for w in words}
print(words_dict)

word_dict1 = Counter(words)
print(word_dict1)
