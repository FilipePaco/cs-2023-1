class TestAvaliacao:
    def test_avaliacao(self):
        avaliacao = Avaliacao()

        # Teste 1 - Valores Inválidos
        try:
            avaliacao.avalia(-2.00, 8.00, 128, 12)
        except ValoresInvalidosException:
            print("Teste 1 - Passou")
        else:
            print("Teste 1 - Falhou")

        # Teste 2 - Valor Inválido
        try:
            avaliacao.avalia(5.00, -5.00, 128, 12)
        except ValoresInvalidosException:
            print("Teste 2 - Passou")
        else:
            print("Teste 2 - Falhou")

        # Teste 3 - Valor Inválido
        try:
            avaliacao.avalia(5.00, 8.00, -10, 12)
        except ValoresInvalidosException:
            print("Teste 3 - Passou")
        else:
            print("Teste 3 - Falhou")

        # Teste 4 - Valor Inválido
        try:
            avaliacao.avalia(5.00, 8.00, 128, -2)
        except ValoresInvalidosException:
            print("Teste 4 - Passou")
        else:
            print("Teste 4 - Falhou")

        # Teste 5 - Valor Inválido
        try:
            avaliacao.avalia(5.00, 8.00, 128, 128)
        except ValoresInvalidosException:
            print("Teste 5 - Passou")
        else:
            print("Teste 5 - Falhou")

        # Teste 6 - Reprovado por Falta
        assert avaliacao.avalia(5.00, 8.00, 32, 128) == "Reprovado por Falta."
        print("Teste 6 - Passou")

        # Teste 7 - Reprovado por Média
        assert avaliacao.avalia(2.00, 3.00, 16, 64) == "Reprovado por Média."
        print("Teste 7 - Passou")

        # Teste 8 - Prova Extra
        assert avaliacao.avalia(5.00, 5.00, 0, 128) == "Prova Extra."
        print("Teste 8 - Passou")

        # Teste 9 - Aprovado
        assert avaliacao.avalia(8.00, 8.00, 0, 128) == "Aprovado."
        print("Teste 9 - Passou")


# Execução dos testes
test = TestAvaliacao()
test.test_avaliacao()