# Prints out all lines of "99 bottles of beer on the wall"

for i in range(1, 99):

	number_of_bottles = str(100 - i)

	print(f'{number_of_bottles} bottles of beer on the wall!')
	print(f'{number_of_bottles} bottles of beer!')
	print('Take one down, pass it around!')

	number_of_bottles = str(100 - i - 1)
	
	if number_of_bottles > '1':
		print(f'{number_of_bottles} bottles of beer on the wall!')
		print() # Empty line between stanzas
	else:
		break

print("1 bottle of beer on the wall!")
print()

# Last two stanzas

print('Only one bottle of beer on the wall!')
print('Only one bottle of beer!')
print('Take it down, pass it around!')
print('No more bottles of beer on the wall!')
print()

print('No more bottles of beer on the wall!')
print('No more bottles of beer!')
print('Go to the store, buy some more!')
print('99 bottles of beer on the wall!')
