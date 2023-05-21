package main

import "fmt"

func questao3() {
	var saldo float64

	fmt.Print("Digite o valor do saldo: ")
	fmt.Scan(&saldo)

	saldoReajustado := saldo + (saldo * 0.15)

	fmt.Printf("O saldo com reajuste de 15%% é: %.2f\n", saldoReajustado)
}
