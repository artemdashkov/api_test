from example_class import Base

class Child(Base):
    def mult(self):
        return self.a + self.b

new_object = Child()

print(f'new_object.a:\t {new_object.a}')
print(f'new_object.b:\t {new_object.b}\n')

new_object.change_a(5)

print(f'new_object.a:\t {new_object.a}')
print(f'new_object.b:\t {new_object.b}\n')

print(f"new_object.sum():\t{new_object.sum()}\n")


class Child_2(Base):
    def __init__(self, a, b, c):
        Base.__init__(self, a, b)
        # super().__init__(a, b)
        self.c = c

    def all_sum(self):
        return self.a + self.b + self.c

object_child_2 = Child_2(1,2, 3)
print(f"====>\tobject_child_2: {object_child_2.all_sum()}")
