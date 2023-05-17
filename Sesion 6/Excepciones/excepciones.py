contador = 0
calculo_suma = 0
print("Sumatoria de 4 numero enteros")
while contador < 4:
    try:
        valor = int(input(f'Ingrese el numero entero {contador+1}: '))
        calculo_suma += valor
        contador +=1
    except:
        print('Valor Errado: ingrese numero entero correcto')
    
print("El resultado de la suma es: ", calculo_suma)