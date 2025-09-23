'''def add (num1, num2):
    return num1 + num2
def sub (num1, num2):
    return num1 - num2
def mult (num1, num2):
    return num1 * num2
def div (num1, num2):
    return num1 / num2

def main():
    num1 = int(input("enter the first number for your operation: "))
    num2 = int(input("enter the second number for your operation: "))
    print("addition", add(num1, num2))
    print("subtraction", sub(num1, num2))
    print("multiplication", mult(num1, num2))
    print("division", div(num1, num2))
main()'''


'''
num = int(input("enter the number for your operation to check whether it is postive or negetive: "))

if num == 0: print("Zero")
elif num > 0: print("the number is positive")
else: print("the number is negative")

print("*************************************************************")

num = int(input("enter the number for your operation to find odd or even: "))
if num == 0: print("Zero")
elif num % 2 == 0: print("the number is even")
else: print("the number is odd")

print("*************************************************************")

num = int(input("enter age "))
if num >= 18: print("Eligible to vote")
else: print("Not eligible to vote")

print("*************************************************************")

def main():
    global s1, s2, s3

    s1 = int(input("enter first side of the triangle: "))
    s2 = int(input("enter second side of the triangle: "))
    s3 = int(input("enter third side of the triangle: "))

def equi(s1, s2, s3):
    main()
    if s1 == s2 == s3: print("It is an equilateral triangle")
    else: print("It is an not an equilateral triangle")

if __name__ == '__main__':
    equi(s1=0, s2=0, s3=0)

print("*************************************************************")


s1 = int(input("Please enter a number: "))
print("even") if (s1 % 2 == 0) else print("odd")

print("*************************************************************")

s1 = input("Please enter a password: ")
print("access granted") if (s1 == "python123") else print("access denied")

print("*************************************************************")

num = int(input("enter the number for your operation to check whether it is postive or negetive: "))

if num == 0: print("Zero")
elif num > 0: print("the number is positive")
else: print("the number is negative")

print("*************************************************************")

s1 = int(input("enter age: "))
print("Eligible to Vote") if (s1 >= 18) else print("Not Eligible to Vote")



s1 = int(input("enter first number: "))
s2 = int(input("enter second number: "))

if s1 == s2: print("equal")

else: print("the first number is greater") if (s1 > s2) else print("the second number is greater")



age = int(input("enter age: "))
if age <= 2: print("you are an infant")
elif age <= 6: print("you are toddler")
elif age <= 13: print("You are a kid")
elif age >= 60: print("You are a senior citizen")
else: print("You are a teenager") if (age <= 18) else print("You are an Adult")


marks = int(input("enter marks: "))

if marks < 55: print("FAIL")
elif marks < 65: print("D Grade")
elif marks < 75: print("C Grade")
elif marks < 90: print("B Grade")
else : print("A Grade")



s1 = int(input("enter first number: "))
s2 = int(input("enter second number: "))
s3 = int(input("enter third number: "))
l1 = [s1, s2, s3]
l1.sort(reverse=True)
print(l1[0], "is the greatest number")




s1 = int(input("enter first side: "))
s2 = int(input("enter second side: "))
s3 = int(input("enter third side: "))
if s1 == s2 == s3: print("equalilaterl triangle")

else: print("Isosceles Triange") if (s1 == s3 or s1 == s2 or s2 == s3 ) else print("Scalene Triangle")

def count_dw(num1):
    total = 0
    while num1 >= 0:
        total += num1
        print(num1)
        num1 -= 1
    print("Sum:", total)


def count_up(num1):
    total = 0
    i = 0
    while i <= num1:
        total += i
        print(i)
        i += 1
    print("Sum:", total)

def main():
    y = int(input("Enter a number: "))
    x = input("Enter your choice (up or down): ")

    count_up(y) if (x.lower() == "up") else count_dw(y)

main()

word = input("please enter a word: ")
print(f"{word} is a palindrome" if (word[::-1] == word) else f"{word} not a palindrome")



def normal(word):
    for i in word:
        print(i)

def reverse(word):
    words = word[::-1]
    for i in words:
        print(i)

def main():
    word = input("enter your word: ")
    rev = input("enter your choise (rev or up): ").lower()
    normal(word) if (rev == "up") else reverse(word)
main()



count = 0
while True:
    count = count + 1
    if count % 5 == 0:
        continue
    elif count >= 100:
        break
    print(count)
print("Done!")

sum = 0
while True:

    input1 = int(input("enter a number: "))
    if input1 == 0: break
    elif input1 %2 != 0: continue
    else: sum += input1
print(f"The sum of all numbers is {sum}")


while True:

    input1 = input("enter a word: ")
    if input1 == input1[::-1]: print("it is a pallindrome")

    else: "not a pallindrome"


def hello(name= "gautam"):
    print(f"Hello {name}")
hello()
hello("kavya")
hello("muskan")



def to_ten():
    val = 10
    for i in range(val+1):
        print(i, end=" ")
to_ten()

def to_twen():
    val = 20
    for i in range(0,val+1,2):
        print(i, end=" ")
to_twen()

def odd():
    val = 15
    for i in range(5,val+1,2):
        print(i, end=" ")
odd()
def downn():
    val = 10
    for i in range(val,-1,-1):
        print(i, end=" ")
downn()

def statement():

    print("Hello \t I am \"Gautam\" \\ \n I go to RIT")

statement()

def loopy():
    for i in range(0,10+1):
        print(f"5 x {i} =", 5*i)
loopy()



def loopy():
    for i in range(6):
        print(i*"*")
loopy()


z = "Gautam"
for i in range(len(z)-1, -1, -1): 
    print(z[i], end="")
'''
def oddoreven(n):
    ''' prints statements if its odd or even depending on if it gives a reminder on dividing with 2'''
    if n%2 == 0: print("Even number")
    else: print("Odd number")
def squareandcube(n):
    ''' prints statements with both square and cube'''
    print("the square of your number is ", n*n)
    print("the cube of your number is ", n*n*n)

#starting point/function of the program
def main():
    ''' takes input of integer from user and then calls both of the other functions'''
    x = int(input("enter a number: "))
    oddoreven(x)
    squareandcube(x)

main() #calling of the function
