# Допишите функцию check_h так, чтобы она проверяла гипотезу Сиракуз для числа n.

# Гипотеза Сиракуз заключается в том,
# что любое натуральное число можно свести к 1,
# если повторять над ним следующие действия:
# если число четное, то разделить его пополам,
# если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.

def check_h(n):
    while n > 1:
        n = n / 2 if not(n % 2) else (n * 3 + 1) / 2
        print(n)
        if n == 1:
            return True
            break
    return False


print(check_h(14))
