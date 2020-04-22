class Point:
      static_attr = 10   #this is called a class level attribute, shared with all instnces

      def __init__(self,x):     # ctor    # self is a point object (this)
            self.x = x
            self.__private = "this is a private field in python"


      @classmethod
      def factory_method(cls):              # class method  (factory method)
            return cls(1)                   # returns an object initialied with x=1


      def my_line(self):                     #instance method
            print(f"{self.x}")   


      def __str__(self):                    # magic method ( ToString() in Java )
            return self.x




Point.static_attr = 5   # here I set the static attr which is shared over all the instances

instace_1 = Point(10)
instace_1.z = 20

instace_2 = Point(5)

isinstance(instace_1 , Point)  # True or False

print(type(instace_1))   # __main__ .Point    main is the module, Point is the class