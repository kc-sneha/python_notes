class lotteryPlayer:
	def __init__(self,name):
		self.name = name
		self.numbers = (2,3,4,5,6,7)
	def total(self):
		return sum(self.numbers)

player = lotteryPlayer("abc")

#print(player.name)
#print(player.numbers)
#print(player.total())


class Student:
	def __init__(self,name,school):
		self.name = name
		self.school =school
		self.marks = []
	def avg_marks(self):
		return sum(self.marks)/len(self.marks)
	def go_to_school(self):
		print("i am going to {}".format(self.school))

##Note1:ClassMethods:der is no need of object(self) bcos it doesnt matter who calls the class method.It can be called using class name.So dont have to pass self. 
##Note2:StaticMethod:Same like Class method.All objects share the same method.
	
	@staticmethod
	def go_to_school_static_method():
		print("iam going to school")

anna = Student("anna","mit")
anna.marks.append(27)
anna.marks.append(29)
print(anna.go_to_school())
#print(anna.avg_marks())
Student.go_to_school_static_method().

##Excercise
class Store:
	def __init__(self,name):
		self.name = name
		self.items = []
	def add_items(self,name,price):
		dict = {
			'name':name,
			'price':price	
		}
		self.items.append(dict)
	def stock_price(self):
		return sum(item['price'] for item in self.items)
	

store = Store("aaa")
store.add_items('item1',10)
store.add_items('item2',20)
print(store.stock_price())
