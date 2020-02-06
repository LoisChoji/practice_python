#give name from list below and we tell you their birthdays
birthdays = {
     'benjamin':'01/17/1706',
     'albert': '12/12/2000',
     'george': '09/10/1993',
  }
print("welcome to the birthday dictionary, we know the birthdays of: ")
for birthday in birthdays:
    print(birthday)
name = input("enter the name of anybody and  i will give you their birthday:  ")
for k,v in birthdays.items():
    if name == k:
          print(name,"'s birthday is ", v)
#if v not in birthdays:
 #   print("please enter another name that is there")