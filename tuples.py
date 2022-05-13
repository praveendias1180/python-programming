import sys

sample = 'computer'

my_list = list(sample)
print(my_list)

my_set = set(sample)
print(my_set)

tuple_1 = ('a', 'b', 20, 4.1)
print(tuple_1)
print(type(tuple_1))

tuple_2 = 'c', 'a', 'b', 20, 4.1
print(tuple_2)

my_tuple = ('car', 'pen', 'ice')
# my_tuple[0] = 'bed'
a, b, c = my_tuple
print(a, b, c)

test_list = [1, 2, 3, 4, 5]
test_tuple = (1, 2, 3, 4, 5)
print(sys.getsizeof(test_list))
print(sys.getsizeof(test_tuple))