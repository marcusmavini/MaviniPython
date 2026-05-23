# Classe base para todos os animais
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

    def mover(self):
        pass

# Subclasse Cachorro que sobrescreve os métodos falar e mover
class Cachorro(Animal):
    def falar(self):
        return "Au!"

    def mover(self):
        return f"{self.nome} está andando."

# Subclasse Gato que sobrescreve os métodos falar e mover
class Gato(Animal):
    def falar(self):
        return "Miau!"

    def mover(self):
        return f"{self.nome} está andando."

# Subclasse Vaca que sobrescreve os métodos falar e mover
class Vaca(Animal):
    def falar(self):
        return "Muu!"

    def mover(self):
        return f"{self.nome} está andando."

class Voador:
    def voar(self):
        return f"{self.nome} está voando."

# Mixin para animais que podem nadar
class Nadador:
    def nadar(self):
        return f"{self.nome} está nadando."

# Subclasse Pato que herda de Animal, Voador e Nadador
class Pato(Animal, Voador, Nadador):

      def falar(self):
        return "Quack!"

      def mover(self):
        return f"{self.andar()}, {self.nadar()} E {self.voar()}"

      def andar(self):
        return f"{self.nome} está andando."

# Função que usa polimorfismo para chamar o método falar
def fazer_som(animal):
    return animal.falar()

# Função que usa polimorfismo para chamar o método mover
def fazer_movimento(animal):
    return animal.mover()

# Instâncias das classes
cachorro = Cachorro('Lug')
gato = Gato( 'Floquinho')
vaca = Vaca('Mimosa')
pato = Pato("Pato Donald")

# Chamando os métodos polimórficos
print(fazer_som(cachorro))  # Saída: Au!
print(fazer_som(gato))      # Saída: Miau!
print(fazer_som(vaca))      # Saída: Muu!
print(fazer_som(pato))      # Saída: Quack!

print(fazer_movimento(cachorro))  # Saída: O cachorro está andando.
print(fazer_movimento(gato))      # Saída: O gato está andando.
print(fazer_movimento(vaca))      # Saída: A vaca está andando.
print(fazer_movimento(pato))      # Saída: Pato Donald está andando, Pato Donald está nadando E Pato Donald está voando.