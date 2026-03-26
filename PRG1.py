def sum_of_digits(N):
    return sum(int(digit) for digit in str(N))


N = int(input("Enter an integer: "))

print("Sum of digits:", sum_of_digits(N))

def sum_of_digits(N):
    total = 0
    while N > 0:
        total += N % 10
        N //= 10
    return total


N = int(input("Enter an integer: "))

print("Sum of digits:", sum_of_digits(N))