import os

WANDS_COUNT = 0
def clear_console():
    """Función para limpiar la consola"""
    # El comando 'cls' limpia la consola en sistemas Windows
    # El comando 'clear' limpia la consola en sistemas Unix/Linux/MacOS
    os.system('cls' if os.name == 'nt' else 'clear')
def show_manu():
    'Function to show the menu'
    clear_console()
    global WANDS_COUNT
    if WANDS_COUNT < 1:
        print("Welcome to Olivanders' Wand Shop!")
        print('Wands: ', WANDS_COUNT)
        print("Here you can find the perfect wand for you.")
        print("Please choose an option:")
        print("1. View available wands")
        print("2. Buy a wand")
        print("3. Exit")
    else:
        print("Hey, wizzard, looks like you already get a wand, each wizzard just can buy a wand, see you")
        print("3. Exit")


class Wand:
    AVAILABLE_WOODS = ['sauce', 'acebo', 'roble', 'tejo', 'espino', 'cerezo', 'caoba']
    AVAILABLE_CORES = ['pluma de fénix', 'pelo de unicornio', 'escama de dragón', 'fibra de corazón de dragón']

    def __init__(self, core, wood, length, engraving=None):
        self.core = ""
        self.wood = ""  # Este atributo estaba faltando
        self.length = 0
        self.engraving = None
        self.price = 0
        self.setCore(core)
        self.setWood(wood)
        self.setLength(length)
        self.setEngraving(engraving)
        self.calculate_price()

    def getCore(self):
        return self.core

    def setCore(self, core):
        if core not in self.AVAILABLE_CORES:
            raise Exception("That material is not in our stock")
        else:
            self.core = core

    def setWood(self, wood):
        if wood not in self.AVAILABLE_WOODS:
            raise Exception("That material is not in our stock")
        else:
            self.wood = wood  # Se asigna el valor de wood al atributo self.wood

    def setLength(self, length):
        if length < 10 or length > 40:
            raise Exception("The min size should be 10 cm and max should be 40 cm")
        else:
            self.length = length

    def setEngraving(self, engraving):
        if engraving is not None:
            print("The wand was engraving with {}".format(engraving))
            self.engraving = engraving
            self.price += 10

    def calculate_price(self):
        prices_cores = {'pluma de fénix': 100, 'pelo de unicornio': 90, 'escama de dragón': 150,
                        'fibra de corazón de dragón': 200}
        prices_woods = {'sauce': 150, 'acebo': 200, 'roble': 250, 'tejo': 300, 'espino': 350, 'cerezo': 400,
                        'caoba': 450}
        price_core = prices_cores[self.core]
        price_wood = prices_woods[self.wood]
        price_length = self.length * 2
        self.price = price_core + price_wood + price_length

    def __str__(self):
        return "[Wand | core: {}, wood: {}, length: {}, engraving: {}] price = {}".format(self.core, self.wood,
                                                                                           self.length,
                                                                                           self.engraving if self.engraving else 'No',                                                                                           self.price)
def avaible_wands():
    global WANDS_COUNT
    harryWand = Wand('pluma de fénix', 'acebo', 11, "child-who-lived")
    hermioneWand = Wand('pluma de fénix', 'tejo', 10)
    ronWand = Wand('pelo de unicornio', 'roble', 12)
    dumbledoreWand = Wand('fibra de corazón de dragón', 'sauce', 13, "Twisted, yet powerful, like the wizard who wields it.")
    voldemortWand = Wand('escama de dragón', 'caoba', 15, "Only i will live forever")
    print("We have the wands of the most iconic characters")
    print('1.Harry \n2. Hermione \n3 .Ron \n4. Dumbledore \n5. Voldemorth')

    wands_dictionary = {'1': [harryWand,"Harrypotter's wand"], '2': [hermioneWand,"Hermione Granger's wand"], '3': [ronWand,"Ron Weasley's wand"], '4': [dumbledoreWand,"Albus Dumbledore's wand"], '5': [voldemortWand,"Lord Voldemort's wand"]}

    user_wand = input('If you want to see the features of a wand, just type the number: ')
    print('Great choice, characteristics of the magic wand')
    print(wands_dictionary[user_wand][1])
    print(wands_dictionary[user_wand][0])

    original_wand = wands_dictionary[user_wand[0]]
    WANDS_COUNT += 1
    input('Press enter to buy and go back to the menu')

def buy_wand():
    global WANDS_COUNT
    print("It looks like you want to buy a wand. Let's go: ")
    user_wand_materials = []
    cores_dic = {
        1: 'pluma de fénix',
        2: 'pelo de unicornio',
        3: 'escama de dragón',
        4: 'fibra de corazón de dragón'
    }
    core = int(input("First, choose a core for you wand, this is our stock: \n1.pluma de fénix \n2.pelo de unicornio \n3.'escama de dragón \n4.'fibra de corazón de dragón"))
    user_wand_materials.append(cores_dic[core])
    clear_console()
    wood_dic = {
        1: 'sauce',
        2: 'acebo',
        3: 'roble',
        4: 'tejo',
        5: 'espino',
        6: 'cerezo',
        7: 'caoba'
    }
    wood = int(input('Alright, now, choose the wood of you wand, these are avaible: \n1. sauce \n2. acebo \n3. roble \n4. tejo \n5. espino \n6. cerezo \n7. caoba'))
    clear_console()
    user_size= int(input('Okey, you are almost there, now, choose the size of your wand, rememer that the mix size is 40 cm and the minimum is 10: '))

    user_wand = Wand(cores_dic[core],wood_dic[wood],user_size,None)
    print('Your wand is:')
    print(user_wand)
    print('The price is: ', user_wand.price)
    WANDS_COUNT += 1
    input('Press enter to buy and go back to the menu')
    show_manu()



def customize():
    global user_

def main():
    'Main function'

    while True:
        show_manu()
        option = input('Select an option: ')
        if option == '1':
            clear_console()
            print('1. View available wands')
            avaible_wands()
            input('Press Enter to continue...')
        elif option == '2':
            clear_console()
            buy_wand()
            print('You have chose option 2.')
            input('Press Enter to continue...')
        elif option == '3':
            clear_console()
            print('Bye.')
            break
        else:
            clear_console()
            print("Opción no válida. Por favor, selecciona una opción válida.")
            input("Presiona Enter para continuar...")
main()
