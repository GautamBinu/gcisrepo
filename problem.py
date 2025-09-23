def oddoreven(n):
    ''' prints statements if its odd or even depending on if it gives a reminder on dividing with 2'''
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def squareandcube(n):
    ''' prints statements with both square and cube'''
    print("the square of your number is ", n * n)
    print("the cube of your number is ", n * n * n)


# starting point/function of the program
def main():
    ''' takes input of integer from user and then calls both of the other functions'''
    x = int(input("enter a number: "))
    oddoreven(x)
    squareandcube(x)


main()  # calling of the function
