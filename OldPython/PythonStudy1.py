# Verificar qual o tipo de dado
text = 'isso é uma STRING'
numero = 42
verdade = True
decimal = 42.5

print('Estes são os tipos de variáveis:')
print(type(text))
print(type(numero))
print(type(verdade))
print(type(decimal))

# Conversão de tipos
print('Convertendo Tipos:')
verdadeNum = int(verdade)
decimalInt = int(decimal)
numeroStr = str(numero)
print(verdadeNum)
print(decimalInt)
print(numero + numeroStr)


