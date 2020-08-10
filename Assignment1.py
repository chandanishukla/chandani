# highest value between two numbers

num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
if (num1>num2):
    print("The largest value among two is : ",num1)
else:
    print("The largest value among two is : ",num2)



# Enter value is even or odd number

num=int(input("Enter the number : "))
if num%2==0:
     print("the given number is even : ",num)
else:
     print("the given number is odd : ",num)



# Highest number among three number

num1=int(input("enter the first number : "))
num2=int(input("enter the Second number : "))
num3=int(input("enter the Third number : "))
if (num1>num2 and num1>num3):
      print("the highest value among three is : ",num1)
elif(num2>num3):
      print("the highest value among three is : ",num2)
else:
     print("The highest value among three : ",num3)


#acending order and decending order
list=[3,5,4,7,5,8,9,5,2]
list.sort()
print(list)
list.sort(reverse=True)
print(list)


# smallest of two numbers

num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
if (num1<num2):
    print("The smallest number is : ",num1)
else:
    print("The smallest number is : ",num2)


# smallest number of three numbers
num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
num3=int(input("enter the third  number : "))
if (num1<num2 and num1<num3):
    print("The Smallest number is : ",num1)
elif(num2<num3):
     print("The Smallest Number is : ",num2)
else:
     print("the smallest number is : ",num3)



#number between 1 to 100
num= int(input("Enter number : "))
if(num<100):
    print("given number is in tthe range of 1 to 100")
else:
    print("the given number is out of range")



#single digit number 0 to 9 into english word
number=["ZERO","ONE","++TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
n=int(input("Enter any number : "))
print(number[n])


#number 1 to 10 using for loop
for num in range(1,11):
    print(num,end=" ")


#even number between 10 and below 10
for i in range(10,1,-2):
   print(i,end=" ")


#even number from list
list=[10,20,11,14,13,16,30]
for i in list:
      if i%2==0:
       print(i,end=" ")

#odd number between 10 to 20
list=[10,20,11,14,13,16,30]
for i in range(10,21):
    if i in list:
        if i%2!=0:
            print(i,end=" ")


#missed number
list=[10,12,15,18,30,40]
for i  in range(10,21):
     if i not in list:
         print(i,end=" ")


# 8th table
for i in range(1,11):
     print("8 *",i,"=",i*8)

# table as user input
num=int(input("Enter the number:"))
for i in range(1,11):
   print(num ,"*",i,"=",i*num)

#number divisible by3 in the list
list=[12,11,18,9,6,4,8]
for i in range(21):
      if i  not in list:
        if i%3==0:
              print(i,end=" ")


#divisible by 3 but not 5
list=[12,15,10,18,40,6]
for i in list:
      if i%3==0 and i%5!=0:
          print(i,end=" ")

#number is prime or not
num =int(input("Enter the number : "))
for i in range(2,num):
    if num%2==0:
        print("the given number is not prime : ",num)
        break
else:
      print("the given number is prime number: " ,num)
