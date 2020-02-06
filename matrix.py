#nested lists are a common way to create matices
#check how to add matrices or sub with python

#here the inner list comprehension fills the the rows values
#the outer list comprehension creates 6 rows

matrix = [[i for i in range(5)] for _ in range(6 )]
print(matrix)