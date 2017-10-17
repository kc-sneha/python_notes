#list
grades = [10,20,30,40,50]

print(sum(grades)/len(grades))
#tuples
tuple_grades = (10,20,30,40,50)

#Note:lists and tuples are almost same. only difference is tuples are immutable (cannot be changed )

grades.append(55)
print(grades)

set_grades = {50,100,23,50}
print(set_grades)


#Note: sets are unique and unordered

#Note: we can add two tuples.
#example of adding two tuples:

tuple_grades = tuple_grades + (100,)
print(tuple_grades)

#Note:list can be assigned a different value.
grades[0] = 15
print(grades)

#Note:cannot change the values of a tuple and a set. But we can add value to a set.
set_grades.add(10)
print(set_grades)




##Set operations

set1 = {1,2,3,4,5}
set2 = {1,3,5,7,9,11}

print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))

