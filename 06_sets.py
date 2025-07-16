"""
            SETS
"""

my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set))
my_set = {12, 14, 16, 18, 20}
print(my_set)
my_other_set = {15, "Aaron", "Tumba "}
print(type(my_other_set))

my_other_set.clear()
print(len(my_other_set))

del my_set
print(my_set) # Se elimina la variable