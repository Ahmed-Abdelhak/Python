class StrExtended(str):  # first inherit from string

      #overriding lower() method
      def lower(self,str):
            return str.lower() + " " + "extended"


print(StrExtended().lower("Ahmed"))


# note, you cannot extend built-in types !  
# ( only with a Forbidden Fruit (https://pypi.python.org/pypi/forbiddenfruit))
