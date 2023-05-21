package main

import "fmt"

func questao2() {
	// Média dos números 8, 9 e 7
	media1 := (8 + 9 + 7) / 3
	fmt.Println("Média dos números 8, 9 e 7:", media1)

	// Média dos números 4, 5 e 6
	media2 := (4 + 5 + 6) / 3
	fmt.Println("Média dos números 4, 5 e 6:", media2)

	// Soma das duas médias
	somaMedias := media1 + media2
	fmt.Println("Soma das duas médias:", somaMedias)

	// Média das médias
	mediaMedias := (media1 + media2) / 2
	fmt.Println("Média das médias:", mediaMedias)
}
