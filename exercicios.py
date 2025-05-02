try:
    valor_1 = int(input("inserir um numero inteiro:"))
    valor_2 = int(input("inserir outro numero inteiro:"))
    resultado = valor_1 // valor_2
    print(resultado)
except ZeroDivisionError:
    print("integer division or modulo by zero ")
except KeyboardInterrupt:
    print("acho que você nao quis inserir um numero")