country = input('Please input your country: ')
age = input('Please input your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can own a driving license')
	else:
		print('You cannot own a driving license')
elif country == 'Indonesia':
	if age >= 20:
		print('You can own a driving license')
	else:
		print('You cannot own a driving license')
elif country == 'USA':
	if age >= 16:
		print('You can own a driving license')
	else:
		print('You cannot own a driving license')
else:
	print('You can only input Taiwan, Indonesia or USA')