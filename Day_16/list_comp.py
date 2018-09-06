import pdb
import requests
from collections import Counter
import re

resp = requests.get("http://projects.bobbelderbos.com/pcc/harry.txt")
words = resp.text.lower().split(" ")

cnt = Counter(words)
print(cnt.most_common(5))

words = [re.sub(r'\W+', r'', word) for word in words]

resp = requests.get("http://projects.bobbelderbos.com/pcc/stopwords.txt")
stopwords = resp.text.lower().split()

cleaned = [word for word in words if word.strip() and word not in stopwords]

cnt = Counter(cleaned)
print(cnt.most_common(5))

pdb.set_trace()

