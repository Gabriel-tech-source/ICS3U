# Recursive function to find the nth Fibonacci number
def fib(n):
    if n < 0:
        return "Error: Fibonacci sequence does not support negative numbers."
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Function to get a valid number of terms from the user
def getNum(prompt):
    while True:
        try:
            # Ask user for input
            num = int(input(prompt))
            if num <= 0:
                print("Please enter a positive integer.")
            else:
                return num
        except ValueError:
            # Handle invalid input
            print("That's not a valid number. Please enter a whole number.")

# Main function
def main():
    print("Program for printing the Fibonacci sequence!")
    
    # Ask for the number of terms to generate
    terms = getNum("Please input a whole number: ")
    
    # Print the Fibonacci sequence
    sequence = []
    for i in range(terms):
        sequence.append(fib(i))  # Append the Fibonacci number for the current index
    
    print(" ".join(map(str, sequence)))  # Print the sequence as space-separated values

# Run the program
if __name__ == '__main__':
    main()
