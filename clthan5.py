'''
0! = 1
1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 = 6
4! = 4 * 6 = 24
5! = 5 * 24 = 120
6! = 6 * 120 = 720
'
'
n! = n * (n-1)
'''


def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n - 1)


print(fact(5))
print(fact(6))
