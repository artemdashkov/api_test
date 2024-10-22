import random
list_1 = [1, 2, 3, 4, 5, 6, 7]
a = random.sample(list_1, 3)
list_1_len = len(list_1)
list_2 = list(range(0, list_1_len))
number = random.randint(1, 10)

print('a\t\t\t\t', a)
print('list_1_len\t\t', list_1_len)
print('list_2\t\t\t', list_2)
print('number\t\t\t', number)
