# Module 5 Practice 1

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors


    def go_to(self, new_floor):
        if 1 <= new_floor <= self.floors:
            for i in range (1, new_floor + 1):
                print(i)
        else:
            print('"Такого этажа не существует"')



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h3 = House('ЖК Возрождение', 28)
h3.go_to(3)
h4 = House('ЖК Ренессанс', 25)
h4.go_to(0)