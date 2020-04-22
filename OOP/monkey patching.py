class A:
      pass


def Test(self):
      return "test method"


# monkey patching !   # like Javascript, dynamic property and set it to a method, then call
A.test = Test

print(A().test())