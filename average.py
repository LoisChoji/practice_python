a = input("enter a set of numbers: ")
result = a.split()
sum = 0
for i in result:
    sum += int(i)
print(sum/len(result))