# Digit Product
def digit_product(number):
    result = 1
    while number>0:
        digit = number % 10
        if digit > 0:
            result *= digit
        number = number // 10
    return result


digit_product(int(input()))



#Largest Power of 3
def largest_power_of_three(number):
    result=1
    while number>=3*result:
        result *= 3
    return result

largest_power_of_three(int(input()))


#Triangle
def triangle(a,b,c):
    a,b,c = sorted([a,b,c])

    if a + b <= c:
        return "No Triangle"
    elif a**2 + b**2 == c**2:
        return  "Right Triangle"
    elif  a**2 + b**2 - c**2 > 0:
        return "Acute Triangle"
    else:
        return "Obtuse Triangle"
        


a=int(input())
b=int(input())
c=int(input())
triangle(a,b,c)


def sum_digits(number):
    result = 0
    while number>0:
        result += number%10
        number //= 10
    return result


# The Root of the Number
def the_root_of_the_number(number):
    while number >= 10:
        number = sum_digits(number)
        print(number)
    return number

A = the_root_of_the_number(int(input()))



# Number Of Divisors
def number_of_divisors(number):
    result = 0
    divisor = 1
    while number >= divisor:
        if number % divisor  == 0:
            result+=1
        divisor+=1
    return result


number_of_divisors(int(input()))





#Quadratic Equation
import math

def quadratic_equation(a,b,c):
    if a == 0:
        print("Non-quadratic equation")
        if b == 0 and c!=0:
            print("No Solutions")
        elif b!=0:
            print("One solution: {!s}".format(-c/b))
        else:
            print("Infinite solutions")
    else:
        print("Quadratic equation")
        D = b * b - 4 * a * c
        print("Discriminant: {!s}".format(D))
        if D < 0:
            print("No Solutions")
        elif D == 0:
            print("One Solutions {!s}".format(-b / 2 * a))
        else:
            s_1 = -b+math.sqrt(D)/ 2 * a
            s_2 = -b-math.sqrt(D)/ 2 * a
            print("Two Solutions {!s} {!s}".format(s_1, s_2))

    
    
    

a=float(input())
b=float(input())
c=float(input())
quadratic_equation(a,b,c)

