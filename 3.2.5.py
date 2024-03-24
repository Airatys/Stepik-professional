from datetime import *
n = input()
m = input()
print(min(date.fromisoformat(n), date.fromisoformat(m)).strftime('%d-%m (%Y)'))



