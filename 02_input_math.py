# get input

# ask user for name
name = input("What is your name? ")

# ask user for two numbers
num_1 = int(input("What is your favourite number? "))
num_2 = int(input("What is your second favourite number? "))

# add numbers together
add = num_1 + num_2

# multiply numbers together
multiply = num_1 * num_2

# greet user and display math
print("Hello", name)

print("{} + {} = {}".format(num_1, num_2, add))
print("{} * {} = {}".format(num_1, num_2, multiply))
