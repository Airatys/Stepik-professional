d1, d2, d3 = int(input()), int(input()), int(input())
s = d1 + d2 + d3
r = min(d1, d2, d3)*2 + (s-min(d1, d2, d3)-max(d1, d2, d3))*2
print(min(s, r))