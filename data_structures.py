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

# find the minimum value in the list
min_list_numbers = [5, 3, 8, -1, -2.2, 0, -4]

# define min number variable
min_number = min_list_numbers[0]

# iterate over the list and find the minimum value
for number in min_list_numbers:
    if number < min_number:
        min_number = number

print(min_number, "is the min number")

#Prompt and print - prompt user for the first name
# using the for loop:
# - print each letter of the name(on the same line)
# - count each letter in the name
# Print the count of letters in the name

name = input("Give me your name! ")
letter_count = 0

for n in name:
    letter_count += 1
    print(n, end=" ")

print(" ")
print(letter_count, "- the count of letters in the name", name)