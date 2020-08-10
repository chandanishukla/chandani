

## remove duplicate value from the list
l=[3,2,5,4,7,6,3,5]
l = list(dict.fromkeys(l))
print(l)

#find biggest value of a given value using lambda function
x=lambda a,b:a if a>b else b
print(x(4,3))



# number of different vowels in the given string
vowels =['a','e','i','o','u']
a= input("Enter any Elements : ")
value = set(a)
result = value.intersection(vowels)
print("Vowels present in given elements :",result)