def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def sort(C):  # Exchange Sort (Selection Sort)
    for i in range(len(C) - 1):  # Outer loop
        min_index = i  # Assume the current element is the minimum
        for j in range(i + 1, len(C)):  # Inner loop finds the smallest element in unsorted part
            if C[j] < C[min_index]:
                min_index = j  # Update min_index if a smaller element is found
        # Swap the found minimum element with the current element
        swap(C, i, min_index)

A = [4, -1, 7, 3, 9, 0, 11, 2, 14]
sort(A)
print(A)
