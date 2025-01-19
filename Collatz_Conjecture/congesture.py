import csv

n = int(input("Enter a number: "))

with open('collatz_conjecture.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['number', 'collatz_conjecture'])

    for i in range(1, n+1, 1):
        con_list = [i]
        original_i = i  # Save the original number
        while i != 1:
            if i % 2 == 0:
                i = i // 2  # Integer division to keep i as an integer
            else:
                i = i * 3 + 1
            con_list.append(i)
        writer.writerow([original_i, con_list])
        con_list.clear()
