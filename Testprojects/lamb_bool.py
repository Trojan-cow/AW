from word2number import w2n


def is_div(n):

    while True:
        try:
            m = round((float(n)), 0)
            n = int(m)
            return lambda a: n % 7 == 0
        except ValueError:
            try:
                res = w2n.word_to_num(n)
                res = round(res, 0)
                return lambda a: res % 7 == 0
            except ValueError:
                print("invalid input, enter only real numbers")
                n = (input("enter a number:"))


num = (input("enter a number:"))
x = is_div(num)
print(x(num))
