import random
def sieteNumeros():
  lista = [1,2,3,4,5,6,7]
  print(lista[0])
  print(lista[1])
def sumaCinco():
  suma = 0
  for i in range(1,6):
    suma += i
  print(suma)
def comparaCuarenta():
  numero = int(input("Ingresa un número: "))
  if numero > 40:
    print("El número es mayor a 40")
  elif numero == 40:
    print("El número es igual a 40")
  else:
    print("El número es menor a 40")
def aprobado():
  nota = float(input("Ingresa tu nota"))
  if nota >= 4.0:
    print("Aprobaste")
  else:
    print("Reprobaste")
def mayoriaEdad():
  edad = input("Ingresa tu edad: ")
  if edad < 18:
    print("Eeres menor de edad")
  elif edad >= 18:
    print("Eres adulto")
  elif edad > 65:
    print("Eres adulto mayor")
def sumaNumeros():
  numeroUno = int(input("Ingresa un número: "))
  numeroDos = int(input("Ingresa otro número: "))
  suma = numeroUno + numeroDos
  print(suma)
def evaluaReal():
  real = float(input("Ingrese un número real: "))
  if real > 0:
    print("El número es positivo")
  elif real == 0:
    print("El número es 0")
  else:
    print("El número es negativo")
def parOImpar():
  numero = int(input("Ingresa un número: "))
  if numero % 2 == 0:
    print("El número es par")
  else:
    print("El número es impar")
def sumaCien():
  suma = 0
  contador = 1
  while contador < 101:
    suma = suma + contador
    contador += 1
  print(suma)
def usuarioContraseña():
  contraseña = "String"
  while True:
    contraseñaUsuario = input("Ingrese la contraseña: ")
    if contraseña == contraseñaUsuario:
      break
    else:
      print("Contraseña incorrecta")
def tablaMultiplicar():
  numero = int(input("Ingresa un número: "))
  for i in range(1,13):  
    print(numero*i)
def variasFunciones():
  numeroUno = int(input("Ingrese un número: "))
  numeroDos = int(input("Ingrese otro número: "))
  def producto(numeroUno, numeroDos):
    return numeroUno * numeroDos 
  resultado = producto(numeroUno, numeroDos)
  def redondeado(resultado):
    round(resultado)
    print(resultado)
def fACel():  
  def conversion(gradosCelsius):
    farenheit = gradosCelsius*(9/5) + 32
    print(round(farenheit))
  gradosCelsius = int(input("Ingresa los grados celsius: "))
  conversion(gradosCelsius)
def numerosAleatorios():
  lista = []
  while len(lista) < 11:
    numero = random.randint(1,100)
    lista.append(numero)
  print(lista)
  print(f"El segundo elemento es {lista[1]} y el sexto es {lista[5]}")
def IMC():
  def calculadoraIMC(peso, altura):
    return peso/(altura**2)
  masa = float(input("Ingrese su masa: "))
  altura = float(input("Ingrese su altura: "))
  IMC = calculadoraIMC(masa, altura)
  if IMC < 18.5:
    print("Bajo peso")
  elif IMC >= 18.5 and IMC <= 24.9:
    print("Peso normal")
  elif IMC >= 25 and IMC <= 29.9:
    print("Sobrepeso")
  else: 
    print("Obesidad")