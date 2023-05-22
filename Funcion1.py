precio = int(input("Ingrese el precio del producto: ")) #Pido el precio del producto

def aplicarAumento():
    aumento = precio * 0.05 #Le aplico un 5% de aumento
    nuevo_precio = precio + aumento
    return nuevo_precio

precio_con_aumento = aplicarAumento() 
print("El precio de su producto con un 5% de aumento es de:", precio_con_aumento) #Muestro el precio nuevo con el aumento
