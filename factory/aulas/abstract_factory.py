from abc import ABCMeta, abstractmethod

# abstractFacoty
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass

    @abstractmethod
    def criar_pizza(self):
        pass

# concretoFactoryA
class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaCamarao()

    
# controFactoryB
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocolis()

    def criar_pizza(self):
        return PizzaBolonha()

    
#abstractProdutoA
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, PizzaVeg):
        pass

# abstractProdutoB
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, PizzaVeg):
        pass

# produtoConcreto
class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

    
# produtoConcreto
class PizzaCamarao(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com camarão na {type(PizzaVeg).__name__}')


# produtoConcreto
class PizzaBrocolis(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

# produtoConcreto
class PizzaBolonha(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com bolonha na {type(PizzaVeg).__name__}')


# cliente
class Pizzaria:

    def fazer_pizzas(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg()
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)


pizzaria = Pizzaria()
pizzaria.fazer_pizzas()
        