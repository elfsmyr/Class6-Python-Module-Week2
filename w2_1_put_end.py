x=int(input())
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for i in range(x):
    a=numbers.pop(0)
    numbers.append(a)

print(numbers)

"""girilen degerin sayı olup olmadıgını kontrol eden while dongusu ekle"""