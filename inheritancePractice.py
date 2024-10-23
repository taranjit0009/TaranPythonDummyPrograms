from ast import Param
from tkinter.font import names


class ParentA:
    def __init__(self,name,age):
        self.name= name
        self.age=age


    def personDetails(self):

        print("Name of the person = "+self.name + " ,Age of the person =",self.age)


class ChildA(ParentA):

    def print1(self):
        print('Called Child classsssss')

objChild_A = ChildA('Karan',16)
objChild_A.personDetails()
objChild_A.print1()