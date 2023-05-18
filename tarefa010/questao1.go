package main

import "fmt"

func questao1() {
	var anos, meses, dias int

	fmt.Print("Digite o número de anos: ")
	fmt.Scan(&anos)

	fmt.Print("Digite o número de meses: ")
	fmt.Scan(&meses)

	fmt.Print("Digite o número de dias: ")
	fmt.Scan(&dias)

	totalDias := (anos * 365) + (meses * 30) + dias

	fmt.Println("A idade expressa em dias é:", totalDias, "dias")
}
