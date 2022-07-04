class Pizza:
    name = ''
    spicy = False
    sauce = False
    cheese = False


class PizzaBuilder(Pizza):

    def name(self, name):
        self.name = name
        return self

    def add_sauce(self):
        self.sauce = True
        return self

    def add_pepperoni(self):
        self.spicy = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def __str__(self):
        result = self.name + "\n"
        result += "Has Spicy\n" if self.spicy else ""
        result += "Has Sauce\n" if self.sauce else ""
        result += "Has Cheese\n" if self.cheese else ""
        return result


if __name__ == "__main__":
    pizza = PizzaBuilder().name("Peperoney").add_cheese().add_sauce()
    print(pizza)
