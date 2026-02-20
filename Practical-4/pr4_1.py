l = ['Rutul', 24012011123, 18, 'CE', 8.95]

l.insert(1, 'Patel')
print(f"Main List:{l}")

l.remove(18)

print(f"List after Remove Operation: {l}")

l[4] = 8.72

print(f"List after Update Operation: {l}")

l.append('UVPCE')

print(f"List after Append Operation: {l}")

l.extend(['Ganpat', 'University'])

print(f"List after Extend Operation: {l}")
