n, x, y, a, b = [int(i) for i in input().split()]
numbers = list(range(1, n+1))
numbers[x-1:y] = numbers[x-1:y][::-1]
numbers[a-1:b] = numbers[a-1:b][::-1]
print(*numbers)




           




