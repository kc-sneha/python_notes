student = {
	'name':'Jose',
	'school':'Computing',
	'grade':(67,77,88)
}



def average_grade(data):
	grades = data['grade']
	return sum(grades) / len(grades)

print(average_grade(student))


def average_grade(students):
	total = 0
	count = 0
	for student in students:
		avg = sum(student[grades])/len(student[grades])
		
