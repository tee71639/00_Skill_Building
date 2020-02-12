# If statements!

like_coffee = input("Do you like coffee ").lower()

if like_coffee == "yes":
    print("I like coffee too")
elif like_coffee == "no":
    print("You are missing out!")
else:
    print("lol what")

    keep_going = input("Press <enter> to continue or any key to quit")
    print()