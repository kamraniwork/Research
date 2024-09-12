class RecipeTemplate:
    def prepare_ingredients(self):
        raise NotImplementedError()

    def cook(self):
        raise NotImplementedError()

    def serve(self):
        raise NotImplementedError()

    def make_recipe(self):
        self.prepare_ingredients()
        self.cook()
        self.serve()

class PizzaRecipe(RecipeTemplate):
    def prepare_ingredients(self):
        print("Prepare pizza dough, sauce, and toppings")

    def cook(self):
        print("Bake the pizza in the oven")

    def serve(self):
        print("Serve the hot pizza slices")

class PastaRecipe(RecipeTemplate):
    def prepare_ingredients(self):
        print("Boil water and cook pasta")

    def cook(self):
        print("Mix pasta with sauce and toppings")

    def serve(self):
        print("Serve the hot pasta dish")

pizza = PizzaRecipe()
pizza.make_recipe()

pasta = PastaRecipe()
pasta.make_recipe()
