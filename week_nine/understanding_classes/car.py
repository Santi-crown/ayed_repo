# Here we're gonna understand classes, finally.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.started = False

    def start(self):
        self.started = True
        print('El', self.brand, self.model, ' has started')

    def stop(self):
        self.started = False
        print('El', self.brand, self.model, ' has stopped')


laguna = Car('Renault', 'Laguna')
tesla = Car('Tesla', 'Model 3')


print(type(laguna))
print(type(tesla))
# calling the atributtes of the class
print(laguna.brand,laguna.model)
print(tesla.brand,tesla.model)

# calling the methods of the class, they change the state of the variable started
laguna.start()
tesla.start()
print(laguna.brand,laguna.model,laguna.started)
print(tesla.brand,tesla.model,tesla.started)
laguna.stop()
tesla.stop()
print(laguna.brand,laguna.model,laguna.started)
print(tesla.brand,tesla.model,tesla.started)






