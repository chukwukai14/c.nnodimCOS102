week = "sunday"
position = 1
print(week + ", you'll always be the " + str(position)+ "st day of the week to me.")

position = 2
week = "Monday"
week + ", you'll always be the " + str(position) + "nd day of the week to me."

print("I am a dog")
print("what's up")
print('what\'s up')
print("1\n2 3")

sentence = 'mY NAME is Ikechukwu'
sentence.capitalize()
sentence.title()
sentence.upper()
sentence.lower()
sentence.split()

stri = "This movie was awesome"
stri.replace('movie', 'project')

pdapc = "A townhall different from balablu bulaba"
pdapc.startswith('A')
pdapc.startswith('townhall')

message = 'I am learning {}'
message.format('python')

l = ['I', 'Like', 'To', 'Study']
s = ' '.join(l)
print(s)
s.split()

datestr = '1956-01-31'
datestr.split('-')

day = '31'
month = '01'
year = '1956'
'/'.join([day, month, year])

my_basket = [1, 2, 3, 4, 89, 43, 7, 10, 23, 11]
[num for num in my_basket if num %2 == 0]