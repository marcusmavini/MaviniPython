print("Bem vindo ao Python Bank!")
print("=$=$=$=$=$=$=$=$")

## Cadastro
print("Vi que você é novo aqui! Vamos fazer o seu cadastro?")
print("Começaremos pelas INFORMAÇÕES PESSOAIS")
print("-----------------")
name = input("Qual seu nome? ")
email = input("Qual seu e-mail? ")
year = int(input("Ano de nascimento: "))
print("-----------------")

print("Agora vamos incluir seu USUÁRIO e SENHA")
print("-----------------")
username = input("Digite seu usuário: ")
print("A senha deve conter somente números e ter no máximo 6 digitos.")
password = input("Digite uma senha: ")

print("==================")
print("CADASTRO REALIZADO ✔")
print("==================")

## Validar Cadastro
print("Vamos entrar na sua conta!")
username_dig = input("> Usuário: ")
tentativas = 3
while username != username_dig:
    print("✖ INCORRETO! Tente novamente.")
    username_dig = input("> Usuário: ")

password_dig = input("> Senha (3 tentativas): ")
while password != password_dig:
    tentativas -= 1
    if tentativas == 0:
        print("ACESSO BLOQUEADO!")
        break
    print(f"✖ SENHA INCORRETA! {tentativas} restantes")
    password_dig = input("> Senha: ")
else:
    print("==================")
    print("Sucesso✔")  
    print("==================") 

bonus = float(year * 1.5)
print(f"Como você é um novo usuário, te daremos um bônus de R$ {bonus} para começar a movimentar a conta.")

## Adicionando dinheiro
print("Agora, vamos adicionar mais dinheiro a sua conta!")
print("❗Lembrando que no Python Bank, para adicionar centavos, usamos o ponto (.) e não a vírgula")
addMoney = float(input("Quanto você quer adicionar? R$ "))
money = addMoney + bonus
print(f"Saldo atual: R$ {money}")

print("Tudo certo por aqui!")
more = input("Deseja mais alguma coisa?(s/n) ")
print("Opções: 'saldo', 'depositar', 'sacar', 'conta'")
option = input("> ")

while more != "s":
    more = input("Deseja mais alguma coisa?(s/n) ")
    print("Opções: 'saldo', 'depositar', 'sacar', 'conta'")
    option = input("> ")
    if option == "saldo":
        print(f"Saldo Atual: {money}")
    elif option == "depositar":
        addMoney = input("Valor a ser depositado: R$ ")
        money += addMoney