numbers = [1,2,3,4,5,6,7,8,9]
def even_numbers():
	evens = []
	for num in numbers:
		if num % 2 == 0:
			evens.append(num)
	return evens

even_nums = even_numbers()
print(even_nums)

##################

def user_menu(choice):
	if choice == "a":
		return "Add"
	elif choice == "q":
		return "quit"
