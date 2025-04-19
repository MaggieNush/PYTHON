class juice:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
        self.ingredients = []

    def describe(self):
        print(f"This is a {self.size} {self.name} that costs {self.price}.")
        print("Ingredients:", ", ".join(self.ingredients))

    def apply_discount(self, discount_percent):
        discount_amount = self.price * (discount_percent / 100)
        self.price = self.price - discount_amount

    def customize_ingredients(self):
        print("Let's build your juice!🍊")
        while True:
            ingredient = input("Add an ingredient (or type 'done' to finish): ")
            if ingredient.lower() == 'done':
                break
            self.ingredients.append(ingredient)
        print("Your juice is ready!")


my_juice = juice("Berry Blast", 300, "500ml")
my_juice.describe()

my_juice.customize_ingredients()
my_juice.describe()