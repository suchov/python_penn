# exit the loop using brake

# x = 1
# while x <= 10:
#     if x == 5:
#         break # this break up the loop imideately
#     print(x)
#     x += 1


# exit the loop using continue

for number in range(1, 21):
    # test for odd number
    if (number % 2 != 0):
        # test for multiple of 3
        if (number % 3 == 0):
            continue
        print(number)