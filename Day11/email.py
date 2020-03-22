# email: alphanumeric chars followed by @ followed by alphabets followed by . followed by alphabets

a = ["sfsekf@segns", "sefsef", "hkopesri@sgoisg.sf"]

import re

print(list(filter(lambda x: re.match(r'\w+@[a-zA-Z]+\.[a-zA-Z]' , x), a)))
