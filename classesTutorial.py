class MyClass:
    x = 5


P1 = MyClass()
print(P1.x)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi {self.name} your age is {self.age}.")
class MatchStatment:

    def match(self):
        def calcu():
            a = int(input('Enter the value of a = '))
            b = int(input('Enter the value of b = '))

            while True:
                ch = input("Enter the sign of the action = ")
            #chh = ["+", "/", "-", "*"]


                match ch:
                    case "+":
                            print(a+b)
                            break
                    case "-":
                            print(a-b)
                            break
                    case "*":
                            print(a*b)
                            break
                    case "/":
                        if b == 0:
                            print("Error: Division by zero is not allowed.")
                        else:
                            print(f"Result: {a / b}")
                            break

                    case _:
                            print("Enter the sign again")



        calcu()

objCal = MatchStatment()
objCal.match()


# person1= Person('Taran',28)
# person1.introduce()