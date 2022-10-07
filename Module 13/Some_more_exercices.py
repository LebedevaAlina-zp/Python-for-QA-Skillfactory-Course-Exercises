#3.7. В клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги. Узнайте число фазанов и число кроликов.
# There are rabbits and pheasants in the cage. They have 35 heads and 94 legs in all. Find out the number of rabbits and pheasants.

h = 35 #heads number
l = 94 #legs number

for r in range(1, h + 1):
    if r*4 + (h-r)*2 == l:
        print('%d rabbits and %d pheasants' % (r, h-r))

# 13.8.13. При помощи генератора списков создайте таблицу умножения чисел от 1 до 10.
# Using lists comprehension create a multiplication table for numbers from 1 to 10.
Multi_table = [[str(i)+'*'+str(j)+'='+str(i*j) for j in range(1, i+1)] for i in range (1, 11)]
for row in Multi_table:
    print(row)
    
#13.8.17
#Используя функцию zip() внутри генераторов списков, вычислите поэлементные произведения списков.
# Using zip() function inside list comprehension calculate the products of corresponding element multiplication of the lists:  
# L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  и M = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

L = [i for i in range(0, 10)]
M = [i for i in range(9, 0, -1)]

N = [a*b for a,b in zip(L,M)]
print(N)

# 13.8.18
# Реализуйте программу, которая сжимает последовательность символов. На вход подается последовательность вида:
# aaabbccccdaa
# Необходимо вывести строку, состоящую из символов и количества повторений этого символа. Вывод должен выглядеть как:
# a3b2c4d1a2
# Write a program that converts a test string like 'aaabbccccdaa' into a string like 'a3b2c4d1a2' consisting of symbols and the numbers of their repetitions in a row.

s = input('Enter some text: ')

s_new = s[0]
letter_count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        letter_count += 1
    else:
        s_new += str(letter_count) + s[i]
        letter_count = 1
s_new += str(letter_count)

print(s_new)
