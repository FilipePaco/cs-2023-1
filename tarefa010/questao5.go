package main

import "fmt"

func questao5() {
	var salarioMinimo, salarioUsuario float64

	fmt.Print("Digite o valor do salário mínimo: ")
	fmt.Scan(&salarioMinimo)

	fmt.Print("Digite o valor do salário do usuário: ")
	fmt.Scan(&salarioUsuario)

	quantidadeSalariosMinimos := salarioUsuario / salarioMinimo

	fmt.Printf("O usuário ganha %.2f salários mínimos\n", quantidadeSalariosMinimos)
}
