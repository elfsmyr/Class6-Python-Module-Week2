from itertools import count

tuple1 = (20, 10, 60, 70, 50, 20, 80, 20, 10, 20, 60, 60, 50,80,80,74,74,74,96,96,96,96,96,96)
list=list(set(tuple1))
dict={}

for i in range(len(list)):
    dict[list[i]]=tuple1.count(list[i])
    
print(dict)

