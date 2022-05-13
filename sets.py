fruits = {'apple', 'orange', 'banana'}

print(fruits)

fruits_2 = set(['orange', 'apple', 'mango', 'grapes'])

fruits_2.add('pinapple')

fruits_2.update(['strawberry', 'dragonfruit'])

fruits_2.remove('orange')
fruits_2.discard('apple')
fruits_2.pop()

print(fruits_2)

print(len(fruits_2))

# for fruit in fruits_2:
#     print(fruit)