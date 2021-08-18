def read_int(prompt, min, max):
    try:
        value = min-10
        while value < min or value > max:
            value = int(input(prompt))
            if value < min or value > max:
                print("Error: the value is not within permitted range(", str(min) + "..", str(max) + ")")
            else:
                return value
    except ValueError:
        print("Error: Wrong Input")
        return None

    #


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

read_int(v, -10, 10)
