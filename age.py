driving = input('have you driven before?')
if driving != '有' and driving != '沒有':
	print('please enter yes or no')
	raise SystemExit
age = input('your age?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('license gained')
	else:
		print('why you drove before?')
elif driving == 'No':
	if age >= 18:
		print('is a ideal time to take the license')
	else:
		print('Few years later you will try')