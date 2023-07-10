countrypopulation = {'usa' : 382_200_000, 'france' : 67_000_000, 'china' : 393_000_000}
sortedbykey = {k : v for k, v in sorted(countrypopulation.items())}
sortedbyval = {k : v for k, v in sorted(countrypopulation.items(),key = lambda v : v[1])}
print(sortedbykey)
print(sortedbyval)
sortedbyval2 = {k : v for k, v in sorted(countrypopulation.items(),key = lambda v : v[1], reverse=True)}
print(sortedbyval2)