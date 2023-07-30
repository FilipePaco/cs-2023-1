class ValoresInvalidosException(Exception):
    def __init__(self):
        super().__init__("Valores Inválidos.")


class Avaliacao:
    def avalia(self, nota1, nota2, faltas, cargaHoraria):
        result = None
        percentualFaltas = faltas / cargaHoraria
        media = (nota1 + nota2) / 2

        if (nota1 < 0.0 or nota1 > 10) or (nota2 < 0.0 or nota2 > 10) or (faltas < 0 or faltas > cargaHoraria) or cargaHoraria < 0:
            raise ValoresInvalidosException()

        elif percentualFaltas > 0.25:
            result = "Reprovado por Falta."

        elif media < 3.0:
            result = "Reprovado por Média."

        elif 3.0 <= media < 6.0:
            result = "Recuperação."

        else:
            result = "Aprovado."

        return result