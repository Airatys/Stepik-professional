def filter_anagrams(word, words):
    text = sorted(word)
    mylist = []
    for i in words:
        if text == sorted(i):
            mylist.append(i)
    return mylist