list =[0,1,2,3,4]
same_list = [x for x in range(5)]
print(same_list)

multiply_list = [x*3 for x in range(5)]
print(multiply_list)

print([n for n in range(10) if n%2==0])

ppl = ["sukkU"," chetu","SEDU"]
print([people.strip().lower() for people in ppl])
