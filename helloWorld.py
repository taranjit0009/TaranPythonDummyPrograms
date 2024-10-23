import sys
from traceback import print_tb

print('Hello Python')
print(sys.version)

txt= 'hello world'

print(txt[2:8])

print(txt.upper())

print(txt.replace('h','J'))

#:Listing

thisList = ['apple','banana','mango']

print(thisList)

thisList.insert(2,"Watermelon")

print(thisList)

thisList.append('peach')

print(thisList)

tropical = [2,3,4,3,67,7]

thisList.extend(tropical)
print(thisList)

# List Comprehension

myList = [22,23,24,34,32,52,43,31,21]

newList = []

for x in range(len(myList)):
    if '2' in str(myList[x]):
        newList.append(myList[x])

print(newList)

newList1 = [myList[x] for x in range(len(myList)) if '2' in str(myList[x])]

print('New Output',newList1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


tryTuple = (12,23,22,12,44,2,'taran')

for x in tryTuple:
      print(x)

di=list(tryTuple)

print(di)


dict1 = {'first Name':'Rahul',
         'Lname':'Sigh'}

dict1["first Name"]='Amandeep Kaur'

print(dict1)