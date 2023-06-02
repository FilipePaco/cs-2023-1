class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("O animal emite um som.")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print("O cachorro late: Au Au!")

    def correr(self):
        print("O cachorro está correndo.")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print("O gato mia: Miau!")

    def correr(self):
        print("O gato está correndo.")


class Pato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print("O pato faz: Quack!")


class AnimalTeste:
    def testar_sons(self):
        cachorro = Cachorro("Rex")
        gato = Gato("Mimi")
        pato = Pato("Donald")

        animais = [cachorro, gato, pato]

        for animal in animais:
            animal.emitir_som()


class Veterinario:
    def examinar(self, animal):
        animal.emitir_som()


class Zoologico:
    def __init__(self):
        self.jaulas = []

    def adicionar_animal(self, animal):
        self.jaulas.append(animal)

    def emitir_sons(self):
        for animal in self.jaulas:
            animal.emitir_som()
            if isinstance(animal, Cachorro) or isinstance(animal, Gato):
                animal.correr()


# Teste das classes
animal_teste = AnimalTeste()
animal_teste.testar_sons()

veterinario = Veterinario()

cachorro = Cachorro("Rex")
gato = Gato("Mimi")
pato = Pato("Donald")

veterinario.examinar(cachorro)
veterinario.examinar(gato)
veterinario.examinar(pato)

zoologico = Zoologico()
zoologico.adicionar_animal(Cachorro("Rex"))
zoologico.adicionar_animal(Gato("Mimi"))
zoologico.adicionar_animal(Pato("Donald"))

zoologico.emitir_sons()
