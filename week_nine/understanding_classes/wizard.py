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
        self.name = ""
        self.nick_name = ""
        self.house = ""
        self.blood = ""
        self.chosen_one = False
        # Attribute assignment section - very important
        self.setName(name)
        self.setNick_name(nick_name)
        self.setHouse(house)
        self.setBlood(blood)
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

    def getNick_name(self):
        return self.nick_name
    def setNick_name(self,nick_name):
        if not isinstance(nick_name,str):
            raise Exception("The name must be a string")
        self.nick_name = nick_name

    def getHouse(self):
        return self.house
    def setHouse(self, house):
        if not isinstance(house,str):
            raise Exception("The house must be a string")
        self.house = house

    def getBlood(self):
        return self.blood
    def setBlood(self, blood):
        if not isinstance(blood, str):
            raise Exception("The blood must be a string")
        self.blood = blood



# Hermione = Wizard('Hermione Grenger', 'None', 'Gryffinder', 'Mudblood')
# test 1
# Hermione = Wizard(1, 'None', 'Gryffinder', 'Mudblood')
# test 2
# Hermione = Wizard('Hermione Grenger', None, 'Gryffinder', 'Mudblood')
# test 3
# Hermione = Wizard('Hermione Grenger', 'None', 1.2, 'Mudblood')
# test 4
Hermione = Wizard('Hermione Grenger', 'None', 'Gryffinder', False)

# Test passed succesfully

# print(Hermione.name,Hermione.nick_name,Hermione.house,Hermione.blood,Hermione.chosen_one)

