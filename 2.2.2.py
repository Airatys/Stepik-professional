en, ru = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'
a, b, c = input(), input(), input()
counte = 0
countr = 0
s = a + b + c
for i in s:
    if i in 'AaBCcEeHKMOoPpTXxy':
        counte += 1
    elif i in 'АаВСсЕеНКМОоРрТХху':
        countr += 1
if counte == 3:
    print('en')
elif countr == 3:
    print('ru')
elif counte + countr == 3:
    print('mix')
        




