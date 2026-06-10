from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        # Assigning to properties triggers the setters below
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        # Explicit conversion to float ensures precise decimal division
        float_value = float(value)
        if float_value <= 0:
            raise ValueError("Weight must be positive.")
        self._weight = float_value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        # Explicit conversion to float ensures precise decimal division
        float_value = float(value)
        if float_value <= 0:
            raise ValueError("Height must be positive.")
        self._height = float_value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight:.2f} kg")
        print(f"Height: {self.height:.2f} m")
        print(f"BMI: {self.calculate_bmi():.2f}")
        print(f"Category: {self.get_bmi_category()}")


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        # Adjusted ranges to < 25.0 and < 30.0 to prevent gaps (e.g., 24.95)
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25.0:
            return "Normal Weight"
        elif bmi < 30.0:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def calculate_bmi(self):
        # Adjusted BMI formula for children
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 14.0:
            return "Underweight"
        elif bmi < 18.0:
            return "Normal Weight"
        elif bmi < 24.0:
            return "Overweight"
        else:
            return "Obese"