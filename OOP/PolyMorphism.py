from abc import ABC, abstractmethod

class UiControl(ABC):  #abstract class
      
      @abstractmethod
      def draw(self):
            pass


class Button(UiControl):

      def draw(self):
            # return super().draw()
            return print("Button")


class TextBox(UiControl):

      def draw(self):
            # return super().draw()
            return print("TextBox")






list_to_draw = [TextBox(), Button()]

def draw(UiControl):
      UiControl.draw()

for i in list_to_draw:
      draw(i)
      
