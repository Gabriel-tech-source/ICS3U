import turtle

# Function to plot a point on the canvas
def plotIt(t, x, y, d, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(d, color)
    t.penup()

# Function to rotate the image (flip the coordinates)
def rotate_image(cols, rows, image_data):
    rotated_image = []
    for col in range(cols):
        rotated_column = []
        for row in range(rows):
            rotated_column.append(image_data[row][col])
        rotated_image.append(rotated_column)
    return rotated_image

# Function to read and parse the XPM file
def read_xpm_file(filename):
    with open(filename, 'r') as f:
        # Read header line, which contains cols, rows, and num_colors
        header = f.readline().split()
        if len(header) < 3:
            raise ValueError(f"Unexpected header format in {filename}. Expected 3 values, but got {len(header)}.")
        
        cols, rows, num_colors = map(int, header[:3])  # Only take the first 3 values for cols, rows, and num_colors
        
        # Read color definitions
        colors = {}
        for _ in range(num_colors):
            sym, c, color_name = f.readline().split()
            colors[sym] = color_name
        
        # Read image data
        image_data = []
        for line in f:
            # Strip extra spaces and newlines, and avoid empty lines
            stripped_line = line.strip()
            if stripped_line:  # Skip empty lines
                image_data.append(stripped_line)
    
    # Validate the number of rows and columns in the image data
    if len(image_data) != rows:
        raise ValueError(f"Expected {rows} rows in the image data, but got {len(image_data)}.")
    
    # Validate each row length and adjust if necessary
    for i, row in enumerate(image_data):
        row = row.strip()  # Remove leading/trailing spaces
        
        # If row is shorter than expected, pad it with spaces
        if len(row) < cols:
            if len(row) != len(image_data[i-1]):  # Avoid printing repeated warnings for the same length mismatch
                print(f"Warning: Row {i + 1} is shorter than expected ({len(row)} < {cols}). Padding the row.")
            row = row.ljust(cols)  # Pad the row with spaces to match the expected number of columns
        
        # If row is longer, truncate it
        elif len(row) > cols:
            print(f"Warning: Row {i + 1} is longer than expected ({len(row)} > {cols}). Truncating the row.")
            row = row[:cols]  # Trim the row to match the expected number of columns
        
        # Assign the cleaned row back
        image_data[i] = row
    
    return cols, rows, colors, image_data

# Main function to display the image
def display_image(filename, rotate=False):
    # Set up the turtle window
    turtle.bgcolor("gray40")  # Background color
    turtle.tracer(0, 0)       # Speed up plotting (batch updates)
    t = turtle.Turtle()       # Create turtle object
    t.hideturtle()            # Hide turtle cursor

    # Read XPM file
    cols, rows, colors, image_data = read_xpm_file(filename)
    
    # Ensure we do not have an index error by checking row count
    if len(image_data) != rows:
        print(f"Warning: Image data has {len(image_data)} rows, expected {rows} rows. Adjusting.")
        rows = len(image_data)  # Adjust to the actual number of rows in the data

    # Calculate center of image
    center_x = -(cols / 2)
    center_y = (rows / 2)
    
    # Adjust coordinates for rotation if needed
    if rotate:
        image_data = rotate_image(cols, rows, image_data)

    # Plot each point
    for row in range(rows):
        for col in range(cols):
            # Ensure the index is valid
            if row < len(image_data) and col < len(image_data[row]):
                color_symbol = image_data[row][col]
                color = colors.get(color_symbol, "black")  # Default to black if not found
                x = center_x + col
                y = center_y - row  # Flip the y-coordinate for turtle's coordinate system
                plotIt(t, x * 5, y * 5, 5, color)  # Reduced scaling factor to reduce lag
    
    turtle.update()  # Final update to display the image

# Ask the user for rotation choice and file selection
def main():
    # Prompt user for file choice
    print("Select an image:")
    print("1. smiley_emoji_mod.xpm")
    print("2. rocky_bullwinkle_mod.xpm")
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        filename = "smiley_emoji_mod.xpm"
    elif choice == "2":
        filename = "rocky_bullwinkle_mod.xpm"
    else:
        print("Invalid choice. Defaulting to smiley_emoji_mod.xpm.")
        filename = "smiley_emoji_mod.xpm"
    
    # Ask for rotation choice
    rotate_choice = input("Do you want to rotate the image? (yes/no): ").lower()
    rotate = rotate_choice == "yes"
    
    display_image(filename, rotate)

# Run the program
if __name__ == "__main__":
    main()
