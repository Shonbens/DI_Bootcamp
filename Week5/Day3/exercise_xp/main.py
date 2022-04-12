# exercise 1
""""This is my code!"""

number = -10
absolute_number = abs(number)
print(absolute_number)

some_str = "2022"
print(int(some_str))

# hello = input("say hi!")


# exercise 2

class Currency:
    def __init__(self, coin, amount):
        self.coin = coin
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.coin}s"

    def __int__(self):
        return self.amount

    def __repr__(self):
        rep = f"{str(self.amount)} {self.coin}s"
        return rep

    def __add__(self, other):
        if self.coin == other.coin:
            return self.amount + other.amount
        else:
            return f"Cannot add between {self.coin} and {other.coin} "

    def __iadd__(self, other):
        self.amount += other.amount + 5
        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', -10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + c2)
print(c1)
print(c1)
print(c1)
c1 += c2
print(c1)
print(c1 + c3)

