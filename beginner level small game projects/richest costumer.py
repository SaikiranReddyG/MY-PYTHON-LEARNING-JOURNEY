costumers = [{'name': 'sai', 'balance': [1000, 2000, 3000]},
             {'name': "kiran", "balance": [500, 200, 1000]},
             {'name': 'reddy', "balance" : [3000, 4000]},
             {'name': 'gangula', 'balance': [2000, 1000, 5000]},]

richest_costumer = None
richest_costumer_wealth = 0
for costumer in costumers:
    total_wealth = sum(costumer['balance'])
    if total_wealth > richest_costumer_wealth:
        richest_costumer = costumer['name']
        richest_costumer_wealth = total_wealth

print('the richest is: {} and with the total wealth of: {}'.format(richest_costumer, richest_costumer_wealth))


#practice:
costumers = [{'name': 'sai', 'balance': [1000, 2000, 3000]},
             {'name': "kiran", "balance": [500, 200, 1000]},
             {'name': 'reddy', "balance" : [3000, 4000]},
             {'name': 'gangula', 'balance': [2000, 1000, 5000]},]

richest_costumer = None
richest_costumer_wealth = 0

for costumer in costumers:
    total_wealth = sum(costumer['balance'])
    if total_wealth > richest_costumer_wealth:
        richest_costumer = costumer['name']
        richest_costumer_wealth = total_wealth

print('THE RISCHEST COSTUMER I HAVE IS:{} & HIS BALANCE IS: {}'.format(richest_costumer, richest_costumer_wealth))