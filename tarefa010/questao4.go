package main

import "fmt"

func questao4() {
	var ipi float64
	var codigoPeca1, codigoPeca2 string
	var valorUnitarioPeca1, valorUnitarioPeca2 float64
	var quantidadePeca1, quantidadePeca2 int

	fmt.Print("Digite a porcentagem do IPI a ser acrescido: ")
	fmt.Scan(&ipi)

	fmt.Print("Digite o código da peça 1: ")
	fmt.Scan(&codigoPeca1)

	fmt.Print("Digite o valor unitário da peça 1: ")
	fmt.Scan(&valorUnitarioPeca1)

	fmt.Print("Digite a quantidade de peças 1: ")
	fmt.Scan(&quantidadePeca1)

	fmt.Print("Digite o código da peça 2: ")
	fmt.Scan(&codigoPeca2)

	fmt.Print("Digite o valor unitário da peça 2: ")
	fmt.Scan(&valorUnitarioPeca2)

	fmt.Print("Digite a quantidade de peças 2: ")
	fmt.Scan(&quantidadePeca2)

	totalPeca1 := valorUnitarioPeca1 * float64(quantidadePeca1)
	totalPeca2 := valorUnitarioPeca2 * float64(quantidadePeca2)

	totalPagar := (totalPeca1 + totalPeca2) * (ipi/100 + 1)

	fmt.Printf("O valor total a ser pago é: %.2f\n", totalPagar)
}
