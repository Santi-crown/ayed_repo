import os

def clear_console():
    """Función para limpiar la consola"""
    # El comando 'cls' limpia la consola en sistemas Windows
    # El comando 'clear' limpia la consola en sistemas Unix/Linux/MacOS
    os.system('cls' if os.name == 'nt' else 'clear')
def show_manu():
    'Function to show the menu'
    clear_console()
    print("Bienvenido al menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
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
# harryWand = Wand('pluma de fénix', 'acebo', 11, "child-who-lived")
# hermioneWand = Wand('pluma de fénix', 'tejo', 10)
# ronWand = Wand('pelo de unicornio', 'roble', 12)
# dumbledoreWand = Wand('fibra de corazón de dragón', 'sauce', 13, "Twisted, yet powerful, like the wizard who wields it.")
# voldemortWand = Wand('escama de dragón', 'caoba', 15, "Only i will live forever")
#
# # Mostrar detalles de las varitas
# print(harryWand)
# print(hermioneWand)
# print(ronWand)
# print(dumbledoreWand)
# print(voldemortWand)
def main():
    'Main function'
    while True:
        show_manu()
        option = input('Select an option: ')

        if option == '1':
            clear_console()
            print('You have chose option 1.')
            input('Press Enter to continue...')
        elif option == '2':
            clear_console()
            print('You have chose option 2.')
            input('Press Enter to continue...')
        elif option == '3':
            clear_console()
            print('You have chose option 3.')
            input('Press Enter to continue...')
        elif option == '4':
            clear_console()
            print('Bye.')
            break
        else:
            clear_console()
            print("Opción no válida. Por favor, selecciona una opción válida.")
            input("Presiona Enter para continuar...")
main()
