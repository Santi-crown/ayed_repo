# class Wizard:
#     def __init__(self, name, nick_name, house, blood):
#         self.name = name
#         self.nick_name = nick_name
#         self.house = house
#         self.blood = blood
#         self.chosen_one = False
#     def chosen(self):
#         chosen_one = True
#         print(self.name," is the chosen one")
#
# Hermione = Wizard('Hermione Grenger', 'None', 'Gryffinder', 'Mudblood')
# Harry = Wizard('Harry Potter', 'The Boy Who Lived', 'Gryffindor', 'half-blood')
# Ron = Wizard('Ron Weasley', 'Ron', 'Gryffindor','Pure-blood')
# Voldemort = Wizard('Tom Marvolo Riddle', 'Voldemort,  He-Who-Must-Not-Be-Named', 'Slytherin', 'Half-blood')
#
# print(type(Hermione))
# print(type(Harry))
# print(type(Ron))
# print(type(Voldemort))
#
# print(Hermione.name,Hermione.nick_name,Hermione.house,Hermione.blood,Hermione.chosen_one)
# Harry.chosen()
# print(Harry.name,Harry.nick_name,Harry.house,Harry.blood,Harry.chosen_one)

# <======================== Implenting getters and setters - To control the data type ========================>
class Wizard:
    def __init__(self, name, nick_name, house, blood):
        self.name = name
        self.nick_name = nick_name
        self.house = house
        self.blood = blood
        self.chosen_one = False
    def chosen(self):
        chosen_one = True
        print(self.name," is the chosen one")

    def getName(self):
        return self.name
    def setName(self, name):
        # With isinstance, we are checking if something is an instance of a certain class. For example, here we are checking if the name is a string.
        if not isinstance(name, str):
            raise Exception("The name does not correspond to the expected data type")
        self.name = name

# Hermione = Wizard(4,'None', 'Gryffinder', 'Mudblood')

# print(Hermione.name,Hermione.nick_name,Hermione.house,Hermione.blood,Hermione.chosen_one)

