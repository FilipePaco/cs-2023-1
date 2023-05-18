package main

import "fmt"

func questao6() {
	var numero int

	fmt.Print("Digite um número inteiro: ")
	fmt.Scan(&numero)

	antecessor := numero - 1
	sucessor := numero + 1

	fmt.Printf("O antecessor de %d é %d\n", numero, antecessor)
	fmt.Printf("O sucessor de %d é %d\n", numero, sucessor)
}
