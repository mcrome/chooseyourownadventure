class Player_1:
    name = input("What is your name?")
    favorite_color = input("What is your favorite color?")
# I do not know that!
    age = int(input("What is your age?"))
    if age >= 18:
        is_adult = False
    else:
        is_adult = True
    level = 1
    health = 15
class Player_1:
    def __init__(self, name, favorite_color, age, is_adult, level, health):
        self.name = name
        self.favorite_color = favorite_color
        self.age = age
        self.is_adult = is_adult
        self.level = level
        self.health = health

print(Player_1.name)
