# pattern_drawing.py

# Prompt User for Pattern Size:
while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print() # Add a space before printing the pattern for better readability

# Draw the Pattern:
row = 0
while row < size:
    # Inner for loop to print asterisks for each column in the current row
    for col in range(size):
        print("*", end="")
    # After completing each row, print a newline character
    print()
    row += 1