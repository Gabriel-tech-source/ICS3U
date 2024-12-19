"""
Wordle Database Program
Author: Gabriel
Description: This program allows users to search for Wordle puzzle solutions
              by word or by date. Users can input a specific date or word,
              and the program will return the corresponding puzzle solution.
              The data is stored in a file called "wordle.dat".
"""

months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

# Merge date components into an integer date
def merge(day, month, year):
    return int(year + months[month] + day)

# Sort words alphabetically and sync dates
def sort(words, dates):
    paired = sorted(zip(words, dates))
    return [p[0] for p in paired], [p[1] for p in paired]

# Search for a word using binary search
def isMatch(word, words, dates):
    low, high = 0, len(words) - 1
    while low <= high:
        mid = (low + high) // 2
        if words[mid] == word:
            return dates[mid]
        elif words[mid] < word:
            low = mid + 1
        else:
            high = mid - 1
    return 0

# Search by date
def searchByDate(date, dates, words):
    if date in dates:
        return words[dates.index(date)]
    return "Date not found."

# Main Program
def main():
    print("Welcome to the Wordle Database!")
    with open("wordle.dat", "r") as file:
        lines = file.readlines()

    dates, words = [], []
    for line in lines:
        month, day, year, word = line.split()
        dates.append(merge(day, month, year))
        words.append(word)

    words, dates = sort(words, dates)

    while True:
        choice = input("Enter 'w' to search by word or 'd' to search by date (or 'q' to quit): ").strip().lower()
        if choice == 'w':
            word = input("What word are you looking for? ").strip().upper()
            result = isMatch(word, words, dates)
            if result:
                print(f"The word {word} was the solution to the puzzle on {result}.")
            else:
                print(f"{word} was not found in the database.")
        elif choice == 'd':
            year = input("Enter the year: ").strip()

            # Validate month input
            while True:
                month = input("Enter the month (3-letter abbreviation, e.g., 'Jan'): ").strip().capitalize()
                if month in months:
                    break
                else:
                    print("Invalid month. Please enter a valid 3-letter month abbreviation (e.g., 'Jan').")

            day = input("Enter the day: ").zfill(2).strip()
            date = merge(day, month, year)
            if 20210619 <= date <= 20240421:
                word = searchByDate(date, dates, words)
                print(f"The word on {date} was {word}.")
            else:
                print(f"{date} is out of range. Please enter a valid date.")
        elif choice == 'q':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
