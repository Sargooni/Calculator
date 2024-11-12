#calculator
from telnetlib import EXOPL


def main():
    x = float(input("x = "))
    y = float(input("y = "))

    calc(x, y)

def calc(num1, num2):
    addanswer = (num1 + num2)
    minanswer = (num1 - num2)
    multianswer = (num1 * num2)
    divanswer = (num1 / num2)
    modanswer = (num1 % num2)
    expanswer = (num1 ** num2)
    flooranswer = (num1 // num2)
    
    print(f"x + y = {addanswer}")
    print(f"x - y = {minanswer}")
    print(f"x * y = {multianswer}")
    print(f"x / y = {divanswer}")
    print(f"x mod y = {modanswer}")
    print(f"x ** y = {expanswer}")
    print(f"x // y = {flooranswer}")

main()
