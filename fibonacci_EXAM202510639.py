# Fibanacci-factorial-assignment-
Implementation of Fibonacci sequence and factorial calculation using Python.
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Invalid input")
else:
    first = 0
    second = 1

    print("Fibonacci sequence:")

    for i in range(n):
        print(first)
        next = first + second
        first = second
        second = next
