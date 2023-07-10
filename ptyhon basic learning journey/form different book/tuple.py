tup = ('ir', 'am', 'coming', 'for', 'u')
#print(tup[:-1])
#print(tup[1:])

result = tuple(map(lambda i,j : i+j,tup[:-1],tup[1:]))
print('before concatination:',str(tup))
print('after concatination:',str(result))