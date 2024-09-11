"""This program is a calculator made by https://github.com/JoaoRm42"""

def number_mod(number1, number2):
    """This function will print the modulus of the numbers"""
    print(int(number1) % int(number2))

def number_div(number1, number2):
    """This function will print the division of the numbers"""
    print(int(number1) / int(number2))

def number_mult(number1, number2):
    """This function will print the multiplication of the numbers"""
    print(int(number1) * int(number2))

def number_sub(number1, number2):
    """This function will print the subtraction of the numbers"""
    print(int(number1) - int(number2))

def number_sum(number1, number2):
    """This function will print the addition of the numbers"""
    print(int(number1) + int(number2))

def do_operation(number1, number2, operator):
    """This function will call the right function to
    do the operation and get the final result from them"""
    if operator == "+":
        number_sum(number1, number2)
    elif operator == "-":
        number_sub(number1, number2)
    elif operator == "*":
        number_mult(number1, number2)
    elif operator == "/":
        number_div(number1, number2)
    elif operator == "%":
        number_mod(number1, number2)

def operator_check(operator):
    """Function to check if operator is an operator or not"""
    operator_list = ["*", "/", "+", "-", "%"]
    if operator in operator_list:
        return 0
    print ("The operator you just inserted is not an valid operator")
    return 1

def number_check(number):
    """Function to check if the input is a number or not"""
    if number.isdigit():
        return 0
    print("The Number you just inserted is not a valid number")
    return 1

def main():
    """Calculator"""
    num1 = input("Insert Number: ")
    if number_check(num1):
        return 1
    op = input("Insert Operator: ")
    if operator_check(op):
        return 1
    num2 = input("Insert Number: ")
    if number_check(num2):
        return 1
    do_operation(num1, num2, op)

if __name__ == "__main__":
    main()
