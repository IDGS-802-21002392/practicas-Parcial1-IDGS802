
class declarar:
    def realizarPiramide(self):
        numero = int(input("Dame un numero: "))
        i = 1
        while i <= numero:
            j = 0
            while j < i:
                print("*", end="")
                j += 1
            print()
            i += 1


def main():
    #Linea para limpiar la terminal
    
    obj=declarar()
    obj.realizarPiramide()

if __name__ == "__main__":
    main()
