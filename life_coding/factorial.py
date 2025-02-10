
def make_factorial(number):
    list_number = list(range(1, number+1))
    result = 1
    for x in list_number:
        result *= x
    return result

a = make_factorial(5)
print(a)

