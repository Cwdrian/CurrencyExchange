class Currency:

    currencies = { #i updated these currencies
    'CHF': 0.923681,  # Swiss franc
    'CAD': 1.265096,  # Canadian dollar
    'GBP': 0.741392,  # British pound
    'JPY': 112.256361,  # Japanese yen
    'EUR': 0.864329,  # Euro
    'USD': 1.0  # US dollar
}

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def __repr__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def changeTo(self, new_unit):

        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __add__(self, other):

        if isinstance(other, Currency):
            if self.unit != other.unit:
                other.changeTo(self.unit)
            return Currency(other.value + self.value, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(other + self.value * Currency.currencies[self.unit], self.unit)
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self, other):

        return self.__add__(other)

    def __radd__(self, other):
        res = self + other
        if self.unit != "USD":
            res.changeTo("USD")
        return res

    def __sub__(self, other):

        if isinstance(other, Currency):
            if self.unit != other.unit:
                other.changeTo(self.unit)
            return Currency(self.value - other.value, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value - other * Currency.currencies[self.unit], self.unit)
        else:
            raise TypeError("Unsupported operand type for -")

    def __isub__(self, other):

        return self.__sub__(other)

    def __rsub__(self, other):
        res = other - self.value
        res = Currency(res, self.unit)
        if self.unit != "USD":
            res.changeTo("USD")
        return res

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
