def factorial(n):
    """
    Calculates the factorial of a given number n.
    """
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1,n):
            result *= i  
        return result

def main():
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is {factorial(number)}.")

if __name__ == "__main__":
    main()
