finished = False
result = 0
while not finished:
    try:
        numerator = int(input("Enter the numerator: "))# TODO: this line
        denominator = int(input("Enter the denominator: "))# TODO: this line
        fraction = numerator / denominator
        pass
    except:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)