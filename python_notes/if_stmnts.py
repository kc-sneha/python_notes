people = ["sukku","chetu","sedumon"]
person = input("do you know this person?")

if person in people:
	print("i know {}".format(person))
else:
	print("i dont know {}".format(person))



##########

def who_do_u_know():
	people = input("list of ppl u know")
	ppl_list = [ppl.strip() for ppl in people.split(",")]
	#ppl_list = people.split(",")
	#ppl_widout_spaces = []
	#for person in ppl_list:
	#	ppl_widout_spaces.append(person.strip())
	return ppl_list

def ask_list():
	name = input("enter a name")
	if name in who_do_u_know():
		print("known person")


askList()
	
