#Note: A dictionary is a key value set
my_dic = {'name':'abs','age':20,'grades':[10,29,30,40,99]}
lottery_player = {
	'name':'abc',
	'numbers':(11,2,33,43,54)
}
universities = [
	{
	'name':'mit',
	'location':'us'
	},
	{
	'name':'oxford',
	'location':'uk'
	}
]

print(sum(lottery_player['numbers']))

print(lottery_player)

lottery_player['name'] = 'sneha'

print(lottery_player)
