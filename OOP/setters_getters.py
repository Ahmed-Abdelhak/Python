class Product:

      def __init__(self, price):
            self.price = price           # intializaing my private field with the property


      @property                           # getter
      def price(self):
            return self.__price      

      @price.setter                   # setter
      def price(self, value):
            if value < 0:
                  raise ValueError(" cannot be negative")
            self.__price = value      




pro = Product(10)
pro.price = 5
print(pro.price)
