def is_even(number):
    if number % 2 != 0:
        return True
    return False

def sum_evens(numbers):
    total = 0
    for num in numbers:
        if is_even(num):
            total += num
    return total

def main():
    numbers = [1, 2, 3, 4, 5, 6]
    total = sum_evens(numbers)
    print(f"The sum of even numbers is: {total}")

if __name__ == "__main__":
    main()
