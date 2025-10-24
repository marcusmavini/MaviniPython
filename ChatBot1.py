print("Olá! Tudo bem? Meu nome é MavBot")

#Nome
name = input('Qual seu nome? ')
print(f"{name}, seja bem-vindo!")

#Idade
print("Eu sou um bot e fui criado há 5 anos.")
age_input = input('Quantos anos você tem? ')
age = int(age_input)
age_difference = age - 5
print(f"Nossa! Apenas {age_difference} de diferença, gostei.")

#Cor
color_input = input('Eu adoro azul! Qual sua cor favorita? ')
if color_input.lower() == "azul":
    print("Mesma cor? Muito legal!! Somos irmãos de cores :D")
elif color_input.lower() == "amarelo":
    print("Amarelo é a cor do sol! Gosto bastante também.")
else:
    print(f"{color_input} é uma cor interessante!")

#Comida
food_input = input('Qual sua comida favorita? ')
if food_input.lower() == "pizza":
    print("Pizza é minha comida favorita também!")
else:
    print(f"{food_input} parece delicioso! Quem sabe eu experimente algum dia.")
    