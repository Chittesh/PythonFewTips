from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return self.currency , self.amount + other.amount

    def __sub__(self, other):
        return self.currency , self.amount - other.amount

    def __eq__(self, other):
        #Tupple comparion
        return ((self.currency, self.amount ) == (other.currency, other.amount))

    def __gt__(self, other):
        return ((self.currency, self.amount) > (other.currency, other.amount))

    def __lt__(self, other):
        return ((self.currency, self.amount) < (other.currency, other.amount))

amount1 = Money ('EUR', 10)
amount2 = Money ('EUR', 20)
amount3 = Money ('EUR', 10)

print(amount1 == amount3) #True
print(amount1 + amount2)  #('EUR', 30)
print(amount1 - amount2)  #('EUR', -10)
print(amount1 >= amount2)