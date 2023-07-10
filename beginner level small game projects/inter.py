import copy
list_of_lists= [1, 2, 3, 4, 5, 6]
list_of_lists_copy = copy.deepcopy(list_of_lists)
list_of_lists_copy[0]= 10

print(list_of_lists)
print(list_of_lists_copy)