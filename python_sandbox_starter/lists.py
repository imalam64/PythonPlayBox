# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1 ,2, 3, 5, 6]
fruits = ['Apples', 'Orange', 'Grapes', 'Pears']

# Constructor
numbers2 = list((1, 2, 3, 4, 5))

print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

#Insert into position
fruits.insert(2, 'Banana')

# Remove with pop
fruits.pop(2)

# Reverse list 
fruits.reverse()

# Sort List
fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)

# Change value
fruits[0] = 'Goji Berries'

print(fruits)