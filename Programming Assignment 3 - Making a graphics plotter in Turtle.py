import turtle

def plotIt(T, x, y, d, color):
    # Plot a point at (x, y) with diameter d and color
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.dot(d, color)
    T.penup()

def readXPM(filename):
    # Open the XPM file and extract data
    with open(filename, "r") as file:
        cols, rows, num_colors = map(int, file.readline().split())
        
        color_map = {}
        for _ in range(num_colors):
            symbol, _, color = file.readline().split()
            color_map[symbol] = color

        # Read the image data
        image_data = [line.strip() for line in file.readlines()]

    return cols, rows, color_map, image_data

def rotateImage(cols, rows, image_data):
    # Rotate the image by swapping coordinates
    rotated_image = []
    for y in range(rows):
        new_row = []
        for x in range(cols):
            new_row.append(image_data[cols - x - 1][rows - y - 1])
        rotated_image.append(''.join(new_row))
    return rotated_image

def displayImage(filename, rotate=False):
    # Initialize the Turtle screen and turtle object
    turtle.bgcolor("gray40")
    turtle.tracer(0, 0)
    T = turtle.Turtle()
    T.hideturtle()

    # Read the XPM file
    cols, rows, color_map, image_data = readXPM(filename)

    if rotate:
        # Rotate the image if required
        image_data = rotateImage(cols, rows, image_data)

    # Adjust the coordinates to center the image on the screen
    start_x = -cols // 2
    start_y = rows // 2

    # Plot each point
    for y in range(rows):
        for x in range(cols):
            symbol = image_data[y][x]
            color = color_map.get(symbol, "black")
            plotIt(T, start_x + x * 10, start_y - y * 10, 5, color)  # 10px for spacing, 5px for dot size
    
    turtle.update()

def main():
    # Ask the user which image they want to view
    filename = input("Enter the XPM file (smiley_emoji_mod.xpm or rocky_bullwinkle_mod.xpm): ")
    rotate = input("Do you want to rotate the image? (yes/no): ").lower() == "yes"

    displayImage(filename, rotate)
    turtle.done()

if __name__ == "__main__":
    main()
