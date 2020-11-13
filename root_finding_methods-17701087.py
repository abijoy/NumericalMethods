'''
ID: 17701087
Name: Md. Alamin

Following root finding algorithms (assignment 02) are submitted to:
Dr. Kazi Asrafuzzaman
Associate Professor, Computer Science & Engineering, University of Chittagong.
'''
#USAGE: python3 root_finding_methods-17701087.py


import math


def f(x):
    return math.cos(x) - 3*x + 1


def g(x):
    return (1 + math.cos(x)) / 3


def derivFunc(x):
    return -math.sin(x) - 3


def bisection():
    print("Enter initial guesses.\n")
    a = int(input("a: "))
    b = int(input("b: "))
    t = float(input("Enter tolerance: "))

    if (f(a) * f(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    step = 0
    c = a
    while ((b - a) >= t):

        # Find middle point
        c = (a + b) / 2
        print(f'a: {a} \t b: {b} \t c: {c}')
        # Check if middle point is root
        if (f(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (f(c) * f(a) < 0):
            b = c
        else:
            a = c
        step += 1

    print(f"The value of root is {c} \n total steps taken: {step}")


def newtonRaphson():
    x = int(input("Enter initial guess: "))
    t = float(input("Enter tolerance: "))
    h = f(x) / derivFunc(x)
    step = 0
    while abs(h) > t:
        h = f(x) / derivFunc(x)
        x = x - h
        step += 1

    print(f"The value of root is {x} \n total steps taken: {step}")


def fixedPoint():
    N = 100 # max number of iteration
    step = 1
    x = int(input("Enter initial guess: "))
    t = float(input("Enter tolerance: "))
    while(abs(f(x)) > t):
        x1 = g(x)
        step += 1
        if(step > N):
            print("Not convergent")

        x = x1
    print(f"The value of root is {x} \n total steps taken: {step}")


def secant():
    N = 100
    step = 0
    print("Enter initial guesses.\n")
    x0 = int(input("x0: "))
    x1 = int(input("x1: "))
    t = float(input("Enter tolerance: "))
    x2 = x0
    while(abs(x1 - x0) > t):
        x2 = x1 - ((f(x1) * (x1 - x0)) / (f(x1) - f(x0)))
        print(f'x0: {x0} \t x1: {x1} \t x2: {x2}')
        x1, x0 = x2, x1
        step += 1

        if(step > N):
            print("not convergent.")
            return
    print(f"The value of root is {x2} \n total steps taken: {step}")


def regulaFalsi():
    N = 100
    step = 0
    print("Enter initial guesses.\n")
    x0 = int(input("x0: "))
    x1 = int(input("x1: "))
    t = float(input("Enter tolerance: "))

    if (f(x0) * f(x1) >= 0):
        print("You have not assumed right x0 and x2 and b\n")
        return

    x2 = x0
    while(abs(x1 - x0) > t and step <= N):
        x2 = x0 - ((f(x0) * (x0 - x1)) / (f(x0) - f(x1)))
        print(f'x0: {x0} \t x1: {x1} \t x2: {x2}')
        if(f(x2) < t):
            break
        if(f(x0) * f(x2) < 0):
            x1 = x2
        else:
            x0 = x2
        step += 1
    print(f"The value of root is {x2} \n total steps taken: {step}")


if __name__ == '__main__':
    print("This program will find root of this non-leaner eqn. : cos(x) - 3x + 1")
    print("Which method do you want to use:")
    print("\t1. Bisection Method\n\t2. Newton-Rapson Method\n\t3. Fixed Point Method\n\t4. Secant Method\n\t5. Regula-Falsi Method\n")

    c = int(input("Enter your choice: "))

    if(c == 1):
        bisection()
    elif(c == 2):
        newtonRaphson()
    elif(c == 3):
        fixedPoint()
    elif(c == 4):
        secant()
    else:
        regulaFalsi()

