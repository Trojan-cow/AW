import pandas as pd


cars_sold = {
    'brands': ['Ford', 'BMW', 'Chrysler'],
    'number': [10, 12, 5]
}
print(pd.DataFrame(cars_sold))
print(pd.DataFrame(cars_sold).index)
print(pd.__version__)


class Dog:

    att1 = "big"
    att2 = "black"

    def fun(self):
        print(self.att1)


dog1 = Dog()
dog1.fun()
