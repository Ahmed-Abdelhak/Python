import numpy as np
from collections import Counter

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1, 12, 2)]
print(nums_list2)


# Rewrite the for loop to use enumerate
names = ['Ahmed','Mo','Abdelhak']
indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)


# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)







""" Practice with NumPy arrays"""
nums = [[1, 2,  3, 4, 5]
        [6, 7,  8, 9, 10]]
# Print second row of nums
print(nums[:, 1])
# Print all elements of nums that are greater than six
print(nums[nums > 6])
# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)
# Replace the third column of nums
nums[:, 2] = nums[:, 2] + 1
print(nums)







# Create a list of arrival times
arrival_times = [*range(10, 60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i], time) for i, time in enumerate(new_times)]

def welcome_guest():
      return "welcome"
# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')


"""
Profiling to find out the runtimes for each line in a function
"""
# pip install line_profiler
# %load_ext line_profiler
# %lprun -f function_name function_name(args)



"""
code profiling for memory usage
- Inspects memory by querying the operating system
- Results may differ between platforms and runs
- Can still observe how each line of code compares to others based on memory consumption

!Note: you must put the function in a module and import it
"""
# pip install memory_profiler
# %load_ext  memory_profiler
#%mprun -f function_name function_name(args)


primary_types = [1,2,3,4,]
# Combine two items from names and three items from primary_types
differing_lengths = [*zip(names[:2], primary_types[:3])]

print(*differing_lengths, sep='\n')

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

generations = ['as','pd','sx','ys']
# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [n[0] for n in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)
