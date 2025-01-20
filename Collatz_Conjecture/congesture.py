import csv

# Ask the user to enter a number 'n'.
n = int(input("Enter a number: "))

# Open a file named 'collatz_conjecture.csv' for writing.
with open('collatz_conjecture.csv', 'w', newline='') as file:
    # Create a writer to write data to the CSV file.
    writer = csv.writer(file)

    # Write the column names ('number' and 'collatz_conjecture') at the top of the CSV file.
    writer.writerow(['number', 'collatz_conjecture'])

    # Go through each number from 1 to 'n'.
    for num in range(1, n + 1):
        # Start the Collatz sequence with the current number.
        collatz_sequence = [num]
        
        # Keep going until the number becomes 1.
        while num != 1:
            # If the number is even, divide it by 2.
            if num % 2 == 0:
                num = num // 2
            # If the number is odd, multiply it by 3 and add 1.
            else:
                num = num * 3 + 1
            # Add the new number to the Collatz sequence.
            collatz_sequence.append(num)
        
        # Write the original number and its Collatz sequence to the file.
        writer.writerow([collatz_sequence[0], collatz_sequence])