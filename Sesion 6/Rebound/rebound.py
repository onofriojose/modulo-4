def division():
    try:
        suma = 3000
        contador = 0
        resultado = suma / contador
        print(resultado)
        
    except ZeroDivisionError:
        print(f'División por cero.') #Error: division by zero no permitido
        
division() #invocando a la funcion division()