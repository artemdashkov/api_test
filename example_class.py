
class Base:
    def __init__(self, a='1', b='10'):
        self.a = int(a)
        self.b = int(b)

    def sum(self):
        return self.a + self.b

    def change_a(self, new_a):
        self.a = new_a

    def change_b(self, new_b):
        self.b = new_b

new_object = Base()

print(f'new_object.a:\t {new_object.a}')
print(f'new_object.b:\t {new_object.b}\n')

new_object.change_a(5)

print(f'new_object.a:\t {new_object.a}')
print(f'new_object.b:\t {new_object.b}\n')

print(f"new_object.sum():\t{new_object.sum()}\n")

