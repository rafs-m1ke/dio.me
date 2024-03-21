from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')
    
    def desligar(self):
        print('Desligando a TV')
    
    @property
    def marca(salf):
        return 'Samsung'

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o ar condicionado')
    
    def desligar(self):
        print('Desligando o ar condicionado')
        
    @property
    def marca(self):
        return 'Consul'

controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)