list = input("enter numbers to check if its a palindrome: ")
first_check = (list[:])
second_check = (list[::-1])
if first_check == second_check: 
    if int(len(list) % 2 == 0):   
        print(list + " is a palindrome" + " even")

    elif int(len(list) % 2 == 1):
        print(list + " is a palindrome " + " odd")
else:
    print("no")