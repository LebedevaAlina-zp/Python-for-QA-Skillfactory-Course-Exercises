per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

percent_list = list(per_cent.values())

money = float(input("Enter the deposit amount: "))

def depose_calc(x):
    return money*0.01*x

deposit = list(map(depose_calc, percent_list))

def round2(x):
    return round(x, 2)

print(list(map(round2,deposit)))

max_deposit = sorted(deposit)[-1]

print('The maximum amount you can earn - ', round(max_deposit,2))

