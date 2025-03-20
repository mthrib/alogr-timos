# Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo). 

def valor():
    numero = float(input("Qual seu valor?"))
    
    if numero >= 0:
        print("Seu númro é positivo! ")
    else:
        print("Seu valor é negativo! ")
valor()
