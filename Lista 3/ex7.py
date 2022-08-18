dict1 = {'c1': 10, 'c2': 20, 'c3': 30}
dict2 = {}

for i in dict1:
    dict2[dict1[i]] = i

print(dict1)
print(dict2)