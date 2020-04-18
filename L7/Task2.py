class Clothes:
    def __init__(self, user_data):
        self.user_data = user_data

class Coat(Clothes):
    @property
    def get_textile_cons(self):
        return self.user_data/6.5 + 0.5


class Suit(Clothes):
    @property
    def get_textile_cons(self):
        return 2*self.user_data + 0.3

test1 = Coat(100)
print(test1.get_textile_cons)

test2 = Suit(30)
print(test2.get_textile_cons)
