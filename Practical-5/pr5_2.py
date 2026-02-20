d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("Value of a:", d['a'])
print("Value of d:", d['d'])
print("Value of c:", d['c'])

total = d['a'] + d['b'] + d['c'] + d['d']
print("Sum of values:", total)

print("Sum using sum() function:", sum(d.values()))

d['e'] = 5
print("Updated dictionary:", d)
