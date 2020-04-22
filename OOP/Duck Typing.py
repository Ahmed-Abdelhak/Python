class Button():
      def draw(self):
            return print("Button")


class TextBox():
      def draw(self):
            return print("TextBox")


"""
instead of having an Abstract class and define the draw() method in it, to enforce the children to implement this method.

you can depend on python as a "Duck Typing" language, in other words, if the list of objects has a method called draw() , you will get a result when you Iterate over the list !
"""

list_to_draw = [TextBox(), Button()]

for i in list_to_draw:
      i.draw()
      
