def funcionA(funcionB):

    def funcionC():
        print("antes de la funcion decorar")

        funcionB()

        print("despues de la funcion decorar")

    return funcionC()


@funcionA
def saludar():
    print("hola pythonistas")