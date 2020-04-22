# guide : https://rszalski.github.io/magicmethods/#sequence

class TagCloud:

      def __init__(self, tags=None):     # initialize my Tag Cloud with an empty dictionary
            if tags is None:
                  self.tags = {}
            else:
                  self.tags = tags      

      def __len__(self):
            return len(self.tags)

      def __iter__(self):            # it will auto work when i Loop over my TagCloud obj
            return iter(self.tags)   # iterable object to iterate over my obj      
      
      def __reversed__(self):
            return reversed(self.values)
      
      def __getitem__(self, key):
            return self.tags[key.lower()]

      def __setitem__(self,key,value):
            self.tags[key.lower()] = value    

      def add(self, tag):

            # if tag.lower() in self.tags:
            #       self.tags[tag.lower()] = self.tags.get(tag.lower()) + 1   
            # else:
            #       self.tags[key.lower()] = 1       

            """the same code as above"""
            self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1  # if not exist, zero



my_cloud = TagCloud()

my_cloud.add("python")
my_cloud.add("Python")
my_cloud.add("c#")
my_cloud.add("java")


for i in my_cloud:
      print(i)

""" result is : 
python
c#
java
"""      
      
