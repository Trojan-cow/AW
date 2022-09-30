def is_div(n):
    try:
        if isinstance(n, int):
            return lambda a: n % 7 == 0

    except ValueError:
        while True:
            try:
                n = input("Please enter an integer: ")
                n = int(n)
                break
            except ValueError:
                print("No valid integer! Please try again ...")


num = input("Enter a number: ")
x = is_div(num)
print(x)

# proper exception
# float value to int
# loop till user gives integer value
