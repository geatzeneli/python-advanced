from personClass import Adult, Child

def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    person.print_info()

if __name__ == "__main__":
    main()
