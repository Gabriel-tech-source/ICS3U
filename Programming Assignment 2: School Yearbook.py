"""
Author: Gabriel
Date: 2024-11-8
Description: This script arranges a given number of 1x1 yearbook photos in a rectangular 
             layout with the smallest perimeter. Users input the number of photos or "done" 
             to exit. The program outputs optimal dimensions and perimeter for valid entries.
"""

import math

def min_perimeter_photos(num_photos):
    """
    Finds the rectangle dimensions with the minimum perimeter
    to arrange 'num_photos' in a filled rectangle shape.
    
    Parameters:
    - num_photos: Total number of photos to arrange in a rectangle.
    
    Returns:
    - best_dims: Tuple containing the best dimensions (x, y).
    - min_perimeter: The smallest perimeter for the rectangle configuration.
    """
    min_perimeter = float('inf')  # Start with a very high perimeter for comparison
    best_dims = (1, num_photos)   # Default to 1 row and num_photos columns

    # Loop through possible factors up to the square root of num_photos
    for x in range(1, int(math.sqrt(num_photos)) + 1):
        if num_photos % x == 0:  # x is a valid factor of num_photos
            y = num_photos // x  # Calculate corresponding factor y
            perimeter = 2 * (x + y)  # Calculate the perimeter for (x, y)

            # Update if this perimeter is smaller than the previous minimum
            if perimeter < min_perimeter:
                min_perimeter = perimeter
                best_dims = (x, y)  # Update best dimensions to current (x, y)
    
    return best_dims, min_perimeter  # Return the best dimensions and smallest perimeter found

# Main loop for user input
print("Welcome to the school yearbook program!")  # Greet the user
while True:
    user_input = input("Input a number of photos (or 'done' to finish): ")  # Prompt for input
    if user_input.lower() == "done":  # Check if user wants to finish
        print("Thank you for using the program. Goodbye!")  # Farewell message
        break  # Exit loop if 'done' is entered
    
    try:
        num_photos = int(user_input)  # Attempt to convert input to integer
        if num_photos < 1:  # Validate that input is a positive integer
            print(f"{num_photos} is not a valid number of photos. Please enter a positive number.")
            continue  # Restart loop if input is invalid
        
        # Calculate best dimensions and perimeter for given number of photos
        dims, perimeter = min_perimeter_photos(num_photos)
        print(f"The best dimensions are {dims[0]} x {dims[1]} for a perimeter of {perimeter}.")
    
    except ValueError:
        # Error message if input is not a valid integer
        print("Invalid input. Please enter a positive integer or 'done' to finish.")
