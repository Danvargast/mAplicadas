import random
def realPositivoNegativo():
  real = int(input("Ingresa un nímero real: "))
  if real >= 0:
    print(f"El número {real} es positivo")
  elif real == 0:
    print(f"El número {real} es cero")
  else:
    print(f"El númer {real} es negativo")
def parImpar():
  número = int(input("Ingresa un número: "))
  if número % 2 == 0:
    print("El número es par")
  else:
    print("El número es impar")
def sumaCienNumeros():
  contador = 1
  suma = 0
  while contador < 101:
    suma = suma + contador
    contador = contador + 1
  print(f"La suma de los 100 primeros números es: {suma}")
def introducirContraseña():
  password = "Contraseña"
  while True:
    contraseñaUsuario = input("Ingresa la contraseña: ")
    if contraseñaUsuario == password:
      print("Contraseña correcta")
      break
    else:
      print("Contraseña incorrecta")
def tablaMultiplicar():
  numero = int(input("Ingrese un número: "))
  for i in range(1,13):
    print(f" {numero} x {i} = {numero*i}")
def variasFunciones():
  n1 = float(input("Ingresa un número: "))
  n2 = float(input("Ingresa otro número: "))
  def producto(n1,n2):
    return n1*n2
  resultado_producto = producto(n1,n2)
  def redondeo(resultado_producto):
    return round(resultado_producto)
  print(redondeo(resultado_producto))
def celciusFarenheit():
  def convertidor(Celcius):
    return Celcius*(9/5) + 32
  gradosCelcius = float(input("Ingrese la temperatura en Celcius: "))
  print(f"La temperatura en Farenheit es: {round(convertidor(gradosCelcius),2)}")
def funcionAleatorio():
  lista = []
  for i in range(10):
    lista.append(random.randint(1,100))
  print(lista)
  print(f"El segundo elemento de la lista es {lista[1]} y el sexto es {lista[5]}")
def IndiceMasaCorporal():
  def calculadoraIMC(peso,altura):
    return peso/(altura**2)
  peso = float(input("Ingresa tu peso en kg: "))
  altura = float(input("Ingresa tu altura en metros: "))
  IMC = calculadoraIMC(peso,altura)
  print(f"Tu imc es: {IMC}")
def listaIMC():
  listaEstudiantes = [16.43, 19.31, 10.25, 19.63, 17.85, 19.76, 23.64, 21.94, 21.3, 22.67, 16.48]
  contador = 1
  for i in listaEstudiantes:
    if i < 18.5:
      print(f"El estudiante numero {contador} tiene bajo peso con un IMC: {i}")
    contador += 1
def multiploDos():
  numero = int(input("Ingresa un número natural: "))
  if numero % 2 == 0:
    print(f"El número {numero} es múltiplo de 2")
  else:
    print(f"El número {numero} no es múltiplo de 2")
def sumaImpares():
  contador = 1
  suma = 0
  while contador < 51:
    if contador % 2 != 0:
      suma = suma + contador
    contador += 1
  print(f"La suma de los primeros 50 números impares es: {suma}")
def cadenas():
  cadena = input("Ingrese una cadena de por lo menos 10 caracteres: ")
  cadenaNueva = cadena[0] + cadena[4] + cadena[9]
  print(cadenaNueva)
def potenciasFor():
  número = input("Ingresa un número: ")
  for i in range(1,6):
    print(F"La potencia de {número} elevado a {i} es: {int(número)**i}")
def areaTriangulo():
  def calculadoraArea(b,h):
    return (b*h)/2
  base = float(input("Ingresa la base del triángulo: "))
  altura = float(input("Ingresa la altura del triángulo: "))
  print(f"El area del triángulo es {areaTriangulo(base,altura)}")