# Global array to store the Fibonacci sequence
S = []

# Recursive function to compute the Fibonacci sequence
def fib(n):
    # Base case for n = 1 (Fibonacci number 1)
    if n == 1:
        S.append(1)
        return
    # Base case for n = 2 (Fibonacci numbers 1 and 1)
    elif n == 2:
        S.append(1)
        S.append(1)
        return
    else:
        # Recursive case: Call fib(n-1) and then calculate the nth Fibonacci number
        fib(n - 1)  # Recursively compute the sequence up to n-1
        # Append the sum of the last two Fibonacci numbers to the array
        S.append(S[-1] + S[-2])
        return

# Calling the fib function to calculate the first 45 Fibonacci numbers
fib(45)

# Printing the Fibonacci sequence stored in the array S
print(S)
