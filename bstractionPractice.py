from abc import ABC, abstractproperty, abstractmethod

from selenium.webdriver.common.devtools.v129.runtime import CallArgument


class Car(ABC):

    def Show(self):

        print("every car has four weels")
    @abstractmethod
    def Speed(self):
        pass


class Maruti(Car):

    def Speed(self):
        print('100km/h')

        x = int(input("Enter the numerical digit"))

        print(f"----------Here is the table of {x}")

        for i in range(1,11):
            print(f"{x} * {i} = ",i * x)

class Sazuki(Car):

    def Speed(self):
        print('170 km/h')



objMaruti = Maruti()

objMaruti.Show()
objMaruti.Speed()