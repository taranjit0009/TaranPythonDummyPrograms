def my_funnction(*name):
    for x in name:
        print(x[0])
fruits = ["apple", "banana", "cherry"]
my_funnction(['taranjit','singh'],('taranjit2','singh2'),fruits)

#Arbitrary Keyword Arguments, **kwargs

def my_functon(**kids):
    print(kids['fname'])


my_functon(fname='taran',lname='Singh')


#Default Parameter Value
#If we call the function without argument, it uses the default value:

def country(countryName = 'Norway'):
    print('I am from :'+ countryName)

country('Sweden')
country()
country('India')

#Passing a List as an Argument
def listFunction(food1):
    for x in food1:
        print(x)

food = ['noodles','samosa','cookies']

listFunction(food)

#Return Values

def multiplication(x=7):
    return x * 6

print(multiplication())
print(multiplication(21))
