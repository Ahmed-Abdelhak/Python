class Parent:
      def __init__(self):
            super().__init__()  # calling the constructor of "Object" class

      parent_attribute = 2



class Child(Parent):

      # here I will override the implementation of the Parent Constructor
      def __init__(self):
            self.ch = 1

      ## Note that, the Parent constructor will not be created !!! unlike JAVA !
      # to call it use  super().__init__()  in your child constructor      


print(Child().parent_attribute)
