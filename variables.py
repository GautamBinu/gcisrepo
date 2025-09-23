import math
'''

def variable_practice():
    age = float(input("enter your age:- "))*12
    days_in_year = 365
    name_of_first_pet = input("enter your pets name")
    pi = 3.14159
    print(str(age) + " months old", str(days_in_year) + " days in a year", name_of_first_pet + " is the name of your first pet", str(pi) + " is the first 6 digits of pi")
variable_practice()

'''


'''
def prompt():
    in1 = float(input("enter first no:"))
    in2 = float(input("enter second no:"))

    print("addition:, ", in1 + in2)
    print("subtraction:, ", in1 - in2)
    print("multiplication:, ", in1 * in2)
    print("division:, ", in1 / in2)
    print("remainder:, ", in1 % in2)
    print("quotient:, ", in1 // in2)
    print("exponent:, ", in1 ** in2)

prompt()

'''

'''
def circle_area(radius):
    area = math.pi * radius**2
    return area

def main():
    area = circle_area(10)
    print(area)
main()
'''

'''def triangle_area(brdth, hgt):
    area = 0.5 * brdth * hgt
    return area

def main():
    area = triangle_area(34,45)
    print(area)
main()'''

'''def area_sqr(radius):
    return math.pi* radius **2
def circumference(radius):
    return 2 * math.pi * radius


def main():
    x = float(input("enter a radius"))
    area = area_sqr(x)
    circumferene = circumference(x)
    print("area is", area)
    print("circumference is", circumferene)
    

if __name__ == '__main__':
    main()

def count_up(num1):
    total = 0
    i = 0
    while i <= num1:
        total += i
        print(i)
        i += 1
    print("Sum:", total)

count_up(90)
'''