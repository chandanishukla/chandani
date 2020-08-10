#  display the number between 1 to 10 using while loop
i=1
while i<=10:
    print(i,end=" ")
    i=i+1


# display the even number between  10 and 20 including 10 an 20 also using while loop
i=10
while i<=20:
    if i%2==0:
        print(i,end=" ")
    i=i+1


#  print the table using while loop
num=int(input("Enter the number:"))
i=1
while i<=10:
    print(num ,"*",i,"=",i*num)
    i=i+1

#display number 1 to 10 except 3,5,7

for i in range(1,11):
    if i==3:
        continue
    elif i==5:
        continue
    elif i==7:
        continue
    print(i,end=" ")


#  program to find the missing number in the given list
list=[1,2,3,4,5,6,9,10]
for i in range(1,11):
    if i not in list:
        print(i,end=" ")


# program to find the missing even number in the given list

list=[1,2,3,4,5,6,9,10]
for i in range(1,11):
    if i not in list:
        if i%2==0:
            print(i)


# find the number less than or equal to 10 in the given list
list=[4,6,19,3,17,10,55,13]
for i in list:
   if i<=10:
       print(i,end=" ")

