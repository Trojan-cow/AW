from word2number import w2n


def is_div(n):
    while True:
        try:
            m = round((float(n)), 0)
            n = int(m)

        except ValueError:
            try:
                n = w2n.word_to_num(n)
                n = round(n, 0)
            except ValueError:
                print("invalid input, enter only real numbers")
                n = (input("enter a number:"))
                continue
            except TypeError:
                print("invalid input, enter only real numbers")
                n = (input("enter a number:"))
                continue
        if n < 0:
            print("negative number")
            n = input("please input only positive numbers:")
            continue
        return lambda a: n % 7 == 0


num = (input("enter a number:"))
x = is_div(num)
print(x(num))
