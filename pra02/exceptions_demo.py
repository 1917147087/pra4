try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")#when the numerator or denominator are not valid numbers.
except ZeroDivisionError:
    print("Cannot divide by zero!")#when the denominator is 0
print("Finished.")
