"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__ (self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[name] = self
        
    def add_stock(self, amount):
        self.qty += amount

    def sell(self, amount):

        if self.qty == 0: 
          print('Sorry, these cupcakes are sold out')
          return

        if self.qty < amount:
          self.qty = 0
          return

        self.qty -= amount


    @staticmethod
    def scale_recipe(ingredients, amount):

        ingredient_name, ingredient_qty = ingredients

        for ingredient in ingredients:
          scaled_ingredients = []
          for amount_qty in ingredient:
            new_qty = amount_qty * amount


            scaled_ingredients.append[ingredient[0], new_qty] 

        return scaled_ingredients

    @classmethod
    def get (cls, name):

      for cupcake in cache(cls, name):
          return self.name

          if cupcake not in cache:
            print('Sorry that cupcake does not exist')

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
