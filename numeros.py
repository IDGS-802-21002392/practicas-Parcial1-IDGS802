#Diana Lorena Hdez Rojas

class numeros:
    def pedirNumero(self):
        lista = []
        num=int(input("Cuantos numeros quieres ingresar: "))
        for i in range(num):
            numero = int(input("Dame un numero: "))
            lista.append(numero)
            print(lista)

        lista.sort()
        print("Numeros ordenados ", lista)
        pares = []
        impares =[]
        for i in lista:
            if i%2 == 1:
                impares.append(i)
            else:
                pares.append(i)
        print("Lista de impares ", impares)
        print("Lista de pares ", pares)

        for i in lista:
            numeroRepetido = lista.count(i);
            if numeroRepetido>1:
                numeros = numeroRepetido
                num = i
        print("Veces repetido: ", numeros, "Numero repetido: ", num)

obj = numeros()
obj.pedirNumero()

