import pandas as pd

ls = [1, 3, 5, 7]
var = pd.Series(ls, index=['x', 'y', 'z', 'a'])
print(var)
x = [12, 34]
print(len(''.join(list(map(int, x)))))
