# Доп задача:
# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 10^5.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
import time
import math

n = int(input('Enter marker number: '))

start = time.time()
# list_1 = list()
# for i in range(n):
#     summ = 0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:
#             summ += j
#     list_1.append(tuple([i, summ]))
# for i in range(len(list_1)):
#     for j in range(i, len(list_1)):
#         if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
#             print(*list_1[i])


def sum_of_proper_divisors(n):
    s = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            s += k
    return s
# n = int(input())
for i in range(1, 100000):
    j = sum_of_proper_divisors(i)
    if i < j <= n and i == sum_of_proper_divisors(j):
        print(i, j)


# def sum_of_divisors(n):
#     s = 1
#     i = 2
#     j = n
#     j_sqrt = math.isqrt(j)
#     while i <= j_sqrt:
#         if j % i == 0:
#             f = 1
#             m = 1
#             while j % i == 0:
#                 j //= i
#                 m *= i
#                 f += m
#             j_sqrt = math.isqrt(j)
#             s *= f
#         i += 1
#     if j > 1:
#         s *= j + 1
#     return s
#
# def sum_of_proper_divisors(n):
#     return sum_of_divisors(n) - n

end = time.time()
print(end - start)