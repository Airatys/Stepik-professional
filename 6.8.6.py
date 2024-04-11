

from collections import Counter

text = Counter('Арбуз Малина Малина Арбуз Клубника арбуз банан малина вишня черешня вишня арбуЗ'.lower().split())
text.__dict__['min_value'] = lambda: min(text.items(), key=lambda x: (x[1], x[0]))
dat = sorted(list(filter(lambda x: x[1] == text.min_value()[1], text.items())))
for i in dat:
    print(i[0], sep=', ', end=' ')