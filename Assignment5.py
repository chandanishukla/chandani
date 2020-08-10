#program to take take emplty  dictionary  and input from user,print the sum of values
d={}
n=int(input("enter the number:"))
for i in range(n):
    key=input("enter the keys:")
    value=int(input("enter the values:")) #sum of values
    d[key]=value
print(d)
print(sum(d.values()))


#number of each vowel in the given string
s=input("enter the name:")
vowels="aeiou"
for i in vowels:
    print(i,s.lower().count(i))
for i in s:
    if i in 'aeiou':
        print(i,s.lower().count(i))


#occurance of each letter in the string
a=(input("enter a string:"))
for i in a:
    print(i,a.count(i),end=" ")





