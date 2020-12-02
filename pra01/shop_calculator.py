number=int(input("please enter the number of items:"))
time=number
total=0
while number<0:
    print("Invalid number of items!")
    number = int(input("please enter the number of items:"))
while number>0:

    number=number-1
    price=float(input("price of item:"))

    total=total+price
if total>100:
        total=total*0.9

print("Total price for",time,"items is ",total)