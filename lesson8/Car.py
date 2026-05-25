class Car:
    def __init__(self, name, color, year, gjendja, motor, doors):
        self.name = name
        self.color = color
        self.year = year
        self.gjendja= gjendja
        self.motor = motor
        self.doors=doors

    def start(self):
        print("kerri u nis!!")

    def drive(self):
        print(self.name , "eshte duke levizur")

    def stop(self):
        print("kerri eshte ndalur")

    def bbreak(self):
        print("kerri eshte duke ndalur")

    def jepiGaz(self):
         print("kerri eshte duke rritur shpejtesine")