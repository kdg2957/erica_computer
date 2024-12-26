def sparse_add(ms,ns):
	mvalues = ms.values()
	nvalues = ns.values()
	for key in ms:
		value = ns.get(key)
		if value != None:
			ms[key] += value
			del ns[key]
	for key in ns:
		ms[key] = ns[key]
	return ms

# Test code
print(sparse_add({},{})) # {}
print(sparse_add({2: 3, 9: 7},{})) # {2: 3, 9: 7}
print(sparse_add({},{0: 1, 2: 2, 6: 9})) # {0: 1, 2: 2, 6: 9}
print(sparse_add({2: 3, 9: 7},{0: 1, 2: 2, 6: 9})) # {2: 5, 9: 7, 0: 1, 6: 9}