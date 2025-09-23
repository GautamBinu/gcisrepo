#checks whether if a number is even or odd and prints a statment
def oddoreven(num):
    ''' prints statements if its odd or even depending on if it gives a reminder on dividing with 2'''
    if num % 2 == 0:
        print("Even number")
    else:
        print("not even number")

#prints the square of a number
def square(num):
    ''' prints statements with square'''
    print("the square of your number is ", num * num)

#prints the cube of a number
def cube(num):
    ''' prints statements with cube'''
    print("the cube of your number is ", num * num * num)



# starting point/function of the program takes input from user
def main():
    ''' takes input of integer from user and then calls both of the other functions'''
    x = int(input("enter a number: "))
    oddoreven(x)
    square(x)
    cube(x)


main()  # calling of the function
