data = { 'a': [5, 3, 9, 0, 2, 3, 1], 'b': [4, 7, 5, 1, 2], 'c': [8, 1, 3, 2, 4] }

for i in data.keys():
    data[i].sort()
    data.update({i:data[i]}) 
    """gereksiz kod satırı"""

print(data)
