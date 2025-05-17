class Fruit:
    def __init__(self, fruit) ->None:
        self.fruit =  fruit

class Apple: 
    def __init__(self, color, size) -> None:
        self.color  = color
        self.size = size

# object

apple = Apple("red", "medium")
print(apple)

# object

f = Fruit(apple)
print(f)
print(f.fruit)
print(f.fruit.color)