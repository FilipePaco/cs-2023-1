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


class Cavalo(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print("O cavalo relincha: Hihihi!")

    def correr(self):
        print("O cavalo está correndo.")


class Preguica(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print("A preguiça boceja: Zzzzz...")

    def subir_arvore(self):
        print("A preguiça está subindo na árvore.")


class AnimalInvalidoException(Exception):
    def __init__(self):
        super().__init__("Tipo de Animal Inválido")


class Veterinario:
    def examinar(self, animal):
        if isinstance(animal, (Cachorro, Cavalo, Preguica)):
            animal.emitir_som()
        else:
            raise AnimalInvalidoException()


class Zoologico:
    def __init__(self):
        self.jaulas = []

    def adicionar_animal(self, animal):
        self.jaulas.append(animal)

    def emitir_sons(self):
        for animal in self.jaulas:
            animal.emitir_som()
            if isinstance(animal, (Cachorro, Cavalo)):
                animal.correr()


# Teste das classes
veterinario = Veterinario()

cachorro = Cachorro("Rex")
gato = Cachorro("Mimi")  # Exemplo de animal inválido
pato = Cachorro("Donald")  # Exemplo de animal inválido

try:
    veterinario.examinar(cachorro)
    veterinario.examinar(gato)
    veterinario.examinar(pato)
except AnimalInvalidoException as e:
    print(e)

zoologico = Zoologico()
zoologico.adicionar_animal(Cachorro("Rex"))
zoologico.adicionar_animal(Cavalo("Pé de Pano"))
zoologico.adicionar_animal(Preguica("Sid"))

zoologico.emitir_sons()
