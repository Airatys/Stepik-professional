# Зачастую переводить сериалы, не теряя изначальный смысл, невозможно, особенно за счет игр слов.
# Сумасшедший режиссер хочет снять сериал, в котором бы в целях эксперимента задействовал как можно больше языков, чтобы пользоваться красотой каждого из них.
# Тем не менее если задействовать слишком много языков, то сериал станет непонятен абсолютно всем, поэтому режиссер достает случайных людей на улице и спрашивает их, какие языки они знают, таким образом он будет использовать языки которые знают все из них.
# Напишите программу, которая определяет, какие языки будут использоваться в сериале.
# Формат входных данных
# На вход программе в первой строке подается число nn — количество людей, которых донимает режиссер. В каждой из следующих nn строк через запятую и пробел указывается список языков, которые знает человек.
# Формат выходных данных
# Программа должна вывести список языков для сериала в лексикографическом порядке. Если такой список составить нельзя, необходимо вывести текст: 
# Сериал снять не удастся

n = int(input())
mylist = []
for i in range(n):
    myset = set([i.strip() for i in input().split(',')])
    mylist.append(myset)

f = mylist[0]
for i in range(1, len(mylist)):
    f.intersection_update(mylist[i])
if len(f) == 0:
    print('Сериал снять не удастся')
else:
    print(*sorted(list(f)), sep=', ')
    




