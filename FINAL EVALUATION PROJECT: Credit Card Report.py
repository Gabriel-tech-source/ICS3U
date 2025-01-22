# Credit Card Report: Final Project
# Author: Gabriel Abdulnour
# Date: January 2025
# Description: This program reads credit card data from a file, identifies expired or soon-to-expire cards,
#              sorts the data by expiry date, and writes the results to an output file.
def read_data(file_name):
    """
    Reads credit card data from the specified file.
    :param file_name: Name of the input file.
    :return: A list of credit card records, where each record is a list of fields.
    """
    data = []
    try:
        with open(file_name, "r") as file:
            next(file)  # Skip the header line
            for line in file:
                line = line.strip()  # Remove any leading/trailing whitespace
                if line:  # Ignore empty lines
                    fields = line.split(",")  # Split the line by commas
                    given_name = fields[0]
                    surname = fields[1]
                    cc_type = fields[2]
                    cc_number = fields[3]
                    exp_month = int(fields[4])  # Convert month to integer
                    exp_year = int(fields[5])   # Convert year to integer
                    # Append the processed record to the data list
                    data.append([given_name, surname, cc_type, cc_number, exp_month, exp_year])
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return data


def format_date(exp_month, exp_year):
    """
    Formats the expiry date as YYYYMM for sorting purposes.
    :param exp_month: Expiry month as an integer.
    :param exp_year: Expiry year as an integer.
    :return: An integer representing the formatted date (YYYYMM).
    """
    return exp_year * 100 + exp_month  # Combine year and month into a YYYYMM integer


def filter_and_sort_data(data, current_month, current_year):
    """
    Filters and sorts credit card data based on expiry date.
    :param data: List of credit card records.
    :param current_month: Current month as an integer.
    :param current_year: Current year as an integer.
    :return: A sorted list of expired or soon-to-expire credit card records.
    """
    current_date = format_date(current_month, current_year)  # Get the current date in YYYYMM format
    filtered_data = [
        record for record in data
        if format_date(record[4], record[5]) <= current_date  # Filter expired cards or soon-to-expire cards
    ]
    # Sort by expiry date (YYYYMM)
    filtered_data.sort(key=lambda record: format_date(record[4], record[5]))
    return filtered_data


def write_output(file_name, sorted_data, current_month, current_year):
    """
    Writes the filtered and sorted credit card data to an output file.
    :param file_name: Name of the output file.
    :param sorted_data: List of sorted credit card records.
    :param current_month: Current month as an integer.
    :param current_year: Current year as an integer.
    """
    current_date = format_date(current_month, current_year)  # Get the current date in YYYYMM format
    with open(file_name, "w") as file:
        for record in sorted_data:
            given_name = record[0]
            surname = record[1]
            cc_type = record[2]
            cc_number = record[3]
            exp_month = record[4]
            exp_year = record[5]
            expiry_date = f"{exp_year:04d}{exp_month:02d}"  # Format expiry date as YYYYMM
            # Determine the status of the card based on expiry date
            status = "EXPIRED" if format_date(exp_month, exp_year) < current_date else "RENEW IMMEDIATELY"
            file.write(f"{given_name} {surname}: {cc_type:12} #{cc_number} {expiry_date} {status}\n")
    print(f"Output written to {file_name}.")


# Input and output file names
input_file = "data.dat"
output_file = "output.txt"

# Current date (January 2025)
current_month = 1
current_year = 2025

# Step 1: Read data from the input file
data = read_data(input_file)
if not data:
    print("No data to process. Exiting.")
    # The code does not use `return`, as this is not inside a function; using `exit()` instead
    exit()

# Step 2: Filter and sort the data
sorted_data = filter_and_sort_data(data, current_month, current_year)

# Step 3: Write the filtered and sorted data to the output file
write_output(output_file, sorted_data, current_month, current_year)
