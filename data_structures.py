numbers = [1, 3, 5, 4, 6, 6, 13, 15, 10, 8]

even_numbers = []

even_count = 0
# just loop through numbers
for number in numbers:
    if (number % 2 == 0):
        even_numbers.append(number)
        even_count += 1
print(even_numbers)
print(f"There are {even_count} even numbers in the list.")
print(f"There are {len(even_numbers)} even numbers in the list.")