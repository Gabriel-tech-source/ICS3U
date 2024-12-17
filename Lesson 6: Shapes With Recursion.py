def triangle(ch, num):
    if num == 1:  # base case
        print(ch)
        return
    else:  # recursive step
        print(ch * num)  # print the row first
        triangle(ch, num - 1)  # then do the recursive call

# Test the modified function
ch = "#"
n = 8
triangle(ch, n)
