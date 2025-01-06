def validate(N):
    # If input is empty, consider it invalid
    if not N:
        return False
    
    # Convert number N to a list of digits
    digits = [int(digit) for digit in str(N)]
    
    # Start with the sum of the unmodified digits
    total_sum = 0
    
    # Iterate from the rightmost digit (index -1) to the left
    for i in range(len(digits)-1, -1, -1):
        digit = digits[i]
        
        # If the position is even from the right (1-based index), double the digit
        if (len(digits) - i) % 2 == 0:
            digit = digit * 2
            # If doubling results in a number > 9, subtract 9 to make it a single digit
            if digit >= 10:
                digit -= 9
        
        # Add the processed digit to the total sum
        total_sum += digit
    
    # Check if the total sum is divisible by 10
    return total_sum % 10 == 0

# Main function to repeatedly prompt for valid numbers
def main():
    print("Validate a number with the Luhn Algorithm!")
    
    # List of valid sample numbers
    valid_samples = [
        "4532015112830366",  # Valid Credit Card
        "6011514433546201",  # Valid Credit Card
        "12344",             # Valid based on Luhn algorithm
        "79927398713"        # Valid for testing
    ]
    
    print("\nHere are some valid numbers for reference:")
    print("\n".join(valid_samples))
    
    while True:
        N = input("\nEnter any number: ")
        
        # Check if the entered number is valid
        if validate(N):
            print(f"{N} is a valid number.")
            break  # Exit the loop once a valid number is entered
        else:
            print(f"{N} is not a valid number. Please try again.")
            
# Run the program
if __name__ == "__main__":
    main()
