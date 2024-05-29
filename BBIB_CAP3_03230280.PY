def calculate_sum_from_file(filename):
    """Reads a file line by line, extracts the first and last digit from each line,
    forms a two-digit number from these digits, and returns the total sum of all such numbers.

    Parameters:
    filename (str): The name of the file to read from.

    Returns:
    int: The total sum of all two-digit numbers formed.
    """
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace characters
                line = line.strip()
                
                # Initialize variables to hold the first and last digit
                first_digit = None
                last_digit = None
                
                # Loop through characters to find the first digit
                for char in line:
                    if char.isdigit():
                        first_digit = char
                        break

                # Loop through characters in reverse to find the last digit
                for char in reversed(line):
                    if char.isdigit():
                        last_digit = char
                        break

                # If both digits were found, form the two-digit number and add to the total sum
                if first_digit and last_digit:
                    number = int(first_digit + last_digit)
                    total_sum += number

        return total_sum
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"The file {filename} does not exist.")
        return None

def extract_digits(s):
    """
    Extracts the first and last digit from a given string.

    Parameters:
    s (str): The input string from which to extract digits.

    Returns:
    (str, str): A tuple containing the first and last digit as strings. 
                Returns (None, None) if digits are not found.
    """
    first_digit = None
    last_digit = None
    
    # Loop through characters to find the first digit
    for char in s:
        if char.isdigit():
            first_digit = char
            break
    
    # Loop through characters in reverse to find the last digit
    for char in reversed(s):
        if char.isdigit():
            last_digit = char
            break
    
    return first_digit, last_digit

def calculate_sum_from_input(user_input):
    """
    Takes a user input string, extracts the first and last digit,
    forms a two-digit number, and returns this number.

    Parameters:
    user_input (str): The input string from the user.

    Returns:
    int: The two-digit number formed from the first and last digits. 
         Returns None if digits are not found.
    """
    # Extract the first and last digits from the input string
    first_digit, last_digit = extract_digits(user_input)
    
    # If both digits were found, form the two-digit number and return it
    if first_digit and last_digit:
        number = int(first_digit + last_digit)
        return number
    else:
        return None

# Specify the file name
filename = "280.txt"

# Calculate the sum from the file
result = calculate_sum_from_file(filename)

if result is not None:
    # Print the calculated sum from the file
    print(f"The calculated sum from the data in {filename} is: {result}")

# User input section
user_input = input("Enter a string to calculate the initial and last digit sum: ").strip()
user_sum = calculate_sum_from_input(user_input)

if user_sum is not None:
    # Print the calculated sum from the user's input
    print(f"The calculated sum from your input '{user_input}' is: {user_sum}")
else:
    # Inform the user if the input does not contain enough digits
    print(f"Your input '{user_input}' does not contain enough digits to form a two-digit number.")