# program to print unique vowel in the given word

s=input("enter the name:")
for i in s:
    if i=='a'or i=='e'or i=='i'or i=='o' or i=='u':
        print(i,end=" ")

#  program to enter the name and percentage marks and display information
d={}
n=int(input("enter the number : "))
for i in range(n):
    name=input("enter the name : ")
    marks=int(input("enter the marks : ")) #sum of values
    d[name]=marks
print(d)

