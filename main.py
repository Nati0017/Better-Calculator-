def main():
  print("Hello learners!")

if __name__ =="main":
  main()

def addmultiplenumbers(numeros):
  suma = 0
  for i in numeros:
    suma = suma + i
  return suma

print(addmultiplenumbers([1,2,3]))

def multiplymultiplenumbers(numeros):
  multiplicacion = 1
  for i in numeros:
    multiplicacion = multiplicacion * i
  return multiplicacion

print(multiplymultiplenumbers([4,5,6]))

def isiteven(numeros):
  if numeros %2 == 0 and type(numeros) == int:
    return True
  else:
    return False

print(isiteven(6))

def isitaninteger(numeros):
  if type(numeros) == int:
    return True
  else:
    return False

print(isitaninteger(7.9))