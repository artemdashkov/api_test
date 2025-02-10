class Bird:
    def fly(self):
        return "I can fly!"

class Sparrow(Bird):
    pass

class Ostrich(Bird):    
    def fly(self):
        raise Exception("I can't fly!")

def make_bird_fly(bird: Bird):
    print(bird.fly())

ostrich = Ostrich()
make_bird_fly(ostrich)