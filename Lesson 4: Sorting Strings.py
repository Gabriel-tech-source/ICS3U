def trim(w):
    """Remove any leading or trailing whitespace (including newlines) from the word."""
    return w.strip()

def iSort(A):
    """Sort the array A using insertion sort."""
    n = len(A)
    for i in range(1, n):
        for j in range(i):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]

def printIt(A):
    """Print the sorted array in the required format: 4 lines, 10 words per line."""
    for i in range(0, len(A), 10):
        print(' '.join(A[i:i+10]))

def main():
    # List of words
    words = [
        "MIMIC", "POUND", "MAXIM", "LINEN", "UNMET", "FLESH", "BOOBY", "FORTH", "FIRST", "STAND",
        "BELLY", "IVORY", "SEEDY", "PRINT", "YEARN", "DRAIN", "BRIBE", "STOUT", "PANEL", "CRASS",
        "FLUME", "OFFAL", "AGREE", "ERROR", "SWIRL", "ARGUE", "BLEED", "DELTA", "FLICK", "TOTEM",
        "WOOER", "FRONT", "SHRUB", "PARRY", "BIOME", "LAPEL", "START", "GREET", "GONER", "GOLEM"
    ]
    
    # Sorting the words using insertion sort
    iSort(words)
    
    # Printing the sorted words
    printIt(words)

# Run the main function
if __name__ == '__main__':
    main()
