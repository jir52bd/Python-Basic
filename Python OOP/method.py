#Create a class
class Area:
    lenght = 30
    width = 20

    def calculate_area(self):
        area = self.lenght * self.width
        print(area)

#Create object of room calss
object1 = Area()
object1.lenght = 10
object1.width = 8
object1.calculate_area()