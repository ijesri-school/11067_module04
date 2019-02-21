# Ibrahim Jesri | 02/12/2019 #
# Butler Community College | IN 252 | CRN 11067 | Module 03 #

fruits = ['banana', 'apple',  'mango']

print('#BEGIN WHILE STATEMENT#')
i = 1
while i <= 10:
  print(i)
  i += 1
print('#END WHILE STATEMENT#\n')

print('#BEGIN FOR STATEMENT#')
i = 1
for i in range(1, 11):
  print(i)
  i += 1
print('#END FOR STATEMENT#\n')

print('#BEGIN FOR STATEMENT#')
i = 1
for i in range(5, 10):
  print(i)
  i += 1
print('#END FOR STATEMENT#\n')

print('#BEGIN WHILE STATEMENT FOR FRUITS LIST#')
i = 0
while i < len(fruits) :
  print(fruits[i]) 
  i += 1
print('#END WHILE STATEMENT FOR FRUITS LIST#\n')

print('#BEGIN FOR STATEMENT FOR FRUITS LIST#')
i = 0
for value in fruits:
  i = fruits.index(value)
  print(value)
  i += 1
print('#END FOR STATEMENT FOR FRUITS LIST#\n')

print('#BEGIN FOR STATEMENT#')
i = 1
for i in range(1, 11):
  if i != 5:
    print(i)
    i += 1
print('#END FOR STATEMENT#\n')

# Ibrahim Jesri | 02/12/2019 #
# Butler Community College | IN 252 | CRN 11067 | Module 03 #