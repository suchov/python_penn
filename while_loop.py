# while loop
x = 4
while (x < 128):
    x *= 2
    print("x is now:", x)


# while loon - programms that continiously runs and whait for something to happen

# this program runs while input not equal 'hello'

inp = input("Hi! Please say hello. ")
print("")
while inp != 'hello':
    inp = input("Please say hello. ")
    print("")

print('It\'s about time!')