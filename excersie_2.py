largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try: count=int(num)
    except:
        print("Invalid Input")
        continue
    
    if largest is None or count>largest:
        largest=count
    if smallest is None or count<smallest:
        smallest=count

print("Maximum is", largest)
print("Minimum is", smallest)