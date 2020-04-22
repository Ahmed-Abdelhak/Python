from abc import ABC, abstractmethod

class InvalidStreamOperation(Exception):
      pass  

class Stream(ABC):  # this is an abstract class (inherits from the ABC class)
                    # you cannot create an obj from abstract class, it's just a contract

      def __init__(self):
            self.__opened = False    # just demonstrate a field

      @abstractmethod
      def read(self):
            pass       # to provide no implementation (pass the interpreter)


      def open(self):
            if self.__opened:
                  raise  InvalidStreamOperation("stream is already opened")
            else:
                  self.__opened = True
      
      def close(self):
            if not self.__opened:
                  raise  InvalidStreamOperation("stream is already closed")
            else:
                  self.__opened = False


class FileStream(Stream):
      """Note: if you create a constructor, it will override the constructor of the parent  object which is Stream, so Stream constructor will not executed, unless you call the super().__init__"""

      def read(self):
            print("reading the fileStream")


class NetworkStream(Stream):

    def read(self):
        print("reading the NetworkStream")

file_stream = FileStream()
file_stream.open()
file_stream.read()
file_stream.close()
