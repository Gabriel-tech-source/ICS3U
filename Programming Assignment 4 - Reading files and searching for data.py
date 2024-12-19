"""
Wordle Database Program
Author: [Your Name]
Description: A simple program to search for Wordle puzzle solutions by word
             or by date. Data is stored in a file called "wordle.dat".
"""
months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

def merge(day, month, year):
    return int(year + months[month] + day)

def main():
    print("Welcome to the Wordle Database!")
    
    with open("wordle.dat", "r") as file:
        lines = file.readlines()
    
    dates, words = [], []
    for line in lines:
        month, day, year, word = line.split()
        dates.append(merge(day, month, year))
        words.append(word)
    
    while True:
        choice = input("Enter 'w' to search by word or 'd' to search by date (or 'q' to quit): ").strip().lower()
        
        if choice == 'w':
            word = input("Enter the word to search for: ").strip().upper()
            if word in words:
                date = dates[words.index(word)]
                print(f"The word {word} was the solution on {date}.")
            else:
                print(f"{word} was not found.")
        
        elif choice == 'd':
            year = input("Enter the year: ").strip()
            month = input("Enter the month (3-letter abbreviation, e.g., 'Jan'): ").strip().capitalize()
            while month not in months:
                print("Invalid month. Please enter a valid month abbreviation.")
                month = input("Enter the month (e.g., 'Jan'): ").strip().capitalize()
            
            day = input("Enter the day: ").zfill(2).strip()
            date = merge(day, month, year)
            
            if date in dates:
                word = words[dates.index(date)]
                print(f"The word on {date} was {word}.")
            else:
                print(f"No word found for {date}.")
        
        elif choice == 'q':
            break
        
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
