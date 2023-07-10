print('welcome to the tip calculator!!')
total_bill = float(input('what was the total bill!!'))
tip_percentage = int(input('what percentage of tip would you llike to give!!'))
num_people = int(input('how many pepole to split the bill?'))

tip_amount = total_bill * (tip_percentage/100)
total_amount = total_bill + tip_amount
per_person_amount = total_amount / num_people

print(f'\nTipamount: ${tip_amount : 2f}')
print(f'totla bill amount: ${total_amount: 2f}')
print(f'amount per person: ${per_person_amount}')
