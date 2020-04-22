from collections import deque
# queue are imported from Collection module, deque class
# because, if we just made a list and removed the first element, we need to shift the   elements to the left, this is over killing

#  from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()

print(queue)

#-----------------------------

result = "Ahmedinho"

print(len(result))
print(result[0:3])  # substring
print(result[-1])
print(result[-1])
print(result[-1])
print("a7a" not in result)  # true
print("a7a" in result)  # False

# ------------------------------
print(10 // 3)  # will return integer =3

# ----------------------------------

my_set = {1, 4}
# dictionary  {1:3 , "A":4}   key:value
my_set.add(3)
print(my_set)

my_second_set = {1,3,5}

print(my_second_set | my_set)  # {1, 3, 4, 5} union
print(my_second_set & my_set)  # {1} intersect
print(my_second_set - my_set)  # {3,4} that exist in the second, but not in my_set
print(my_second_set ^ my_set)  # ^ carret {3,4,5}  !intersect
# ----------------------------------


def add_two_numbers(a, b):
    if a in my_set:
        return "ss"
    elif a not in my_set:
        return "fuck yeah"
    else:
        ""


print(add_two_numbers(2, 3))


# ----------------------------------
# dictionaries :

my_dict = dict(x=1, y=2)  # equivilant to   {"x":1 , "y": 2}
my_dict["z"] = 3
my_dict.pop("x")
my_dict.get("z")
del my_dict["z"]

for key,value in my_dict.items():    #.items() make a tuple, and i'm unpacking it  key,value
    print(value)


# ----------------------------------
# terniary operator

age = 2
message = "ata" if age == 2 else "fuck"

# ----------------------------------

num = 100

while num > 5:
    print(num)
    num = num // 2


# ---------------------------------
# params in c#

def myFuckzz(*params):
    for num in params:
        print(num)


myFuckzz(1, 2, 3, 4, 5)
# ------------------------------


def pass_dict(**mydic):
    print(mydic)


pass_dict(a=2, b=3)  # {'a': 2, 'b': 3}


# ------------------------------
my_letters = list(range(20))  # [1...19]
my_chars = list("Hello world")  # [H,e,l ...]

zeros_to_100 = [0] * 100

concat_lists = zeros_to_100 + my_letters

# ---------------------------------

# object destructuring in JS ( in python: obnject unpacking)

nusss = [1, 2, 3, 4, 5]
first_num, second_num, *others = nusss

nusss.append(3)  # at the end
nusss.insert(0, 1)  # index, obj
nusss.remove(3)
"ahmed"[0:3]  # substring
del nusss[0:3]  # remove range
len(nusss)  # gets the size

print("------")
# filter returns a "lazy" obj of type filter
heee = filter(lambda item: item > 3, nusss)
# lazy object must be iterable to execute
print(list(heee))


# -----------------------------------------


# lambda expressions with Tuples
my_tuples = [
    ("prod1", 6),
    ("prod2", 5),
    ("prod3", 7)
]

# lambda expression: (input)=>(outp)
my_sorted_tuples = sorted(my_tuples, key=lambda item: item[1]) #tuple[0,1]

# map
prices = map(lambda x: x[1], my_sorted_tuples)
print(list(prices))


# -----------------------------------------

# List comprehention is better than "map" and "filter"
my_prices =[item[1] for item in my_tuples]
print("my_prices")
print(my_prices)

my_filtered = [item for item in nusss if item >3]
print("my_filtered")
print(my_filtered)

# -----------------------------------------
#zip function
new_l1 = [1,2,3]
new_l2 = [4,5,6]
print(list(zip(new_l1,new_l2)))  # [(1,4),(2,5),(3,6)]

# -----------------------------------------

# stacks in python are the same as "lists"

# 1- creat an empty list
my_stack = []

# 2- push elements
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)

# 3- pop
my_stack.pop()   # now my_stack is [1,2]

# last item of the stack is
last_item_of_stack = my_stack[-1]

# falsy values are  0 , "" , []

if not my_stack:  # equavilant to  if(!mystack.Any())  in C#
    print("stack is empty")
else:
    print(my_stack)    

 

#-----------------------------------------
# Tuples are immputable type of lists

x_tuple = 1, 2  # equals:  x_tuple = (1,2)

print(x_tuple[0:1])

print(x_tuple * 3)  # repeat three times in a new tuple   (1, 2, 1, 2, 1, 2)

tuple([3,2,4,])

#-----------------------------------------

# swapping variables using a tuple
x= 10
y = 11
x,y = y,x     # y,x is creating a new Tuple  so, it's Tuple unpacking x,y = (y,x)


#-----------------------------------------

# generator object, can generate numbers, instead of list comprehension, if you deal with large list

genObj = (item*2 for item in range(100)) #need to iterate over genobj

#-----------------------------------------

# Unpacking operator with iterable objects ( the spread operator in JS  ...spread )

charss = [*"hello world"]
xars = [*range(5)]

my_first_one = [1,2,3]
my_second_one = [3,4,5]

m_col = [*my_first_one , "a7a" , *my_second_one]


#--------------------------------

# unpacking dictionaries

dic1 = {"x":15,"y":6}
dic2 = {"z":1}

dic_combined = {**dic1, "f": 3 ,**dic2}

print(dic_combined)

#----------------------------------------------------
# simulating the cache

cache = {}

def check_cache(url):
    if cache.get(url):
        return str(cache.get(url)) + " cached"
    else:
        s = url
        cache[s] = 123
        return str(123) + " server"

print(check_cache("123"))         
print(check_cache("123"))  

print(2 << 10)  # equavilant to 2 power 10
