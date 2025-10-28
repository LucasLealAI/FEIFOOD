print('Seja bem-vindo ao FEIFOOD!')
menuprincipal = input('Se for um novo usuário, digite C para se cadastrar. Caso já tenha logado, digite L para se logar: ')

# Dicionário para usuários lá, se tiver algo ai é só teste, tira sa merda depois

usuarios = {
      "Tania", 123,
      "Lucas", 321
}

# Dicionario pros pedido dos cara, mesma coisa que o cara ali em cima disse

pedidos = {}

# Menu de yummers

def menu():
      print("Selecione a comida que deseja:\n")
      comidas = {
            "Hamburguer": "R$30,00",
            "Hot Dog": "R$25,00",
            "Coxinha": "R$20,00",
            "Coca-Cola": "R$15,00"
      }
      print(comidas)
      escolha = print(input('\n'))
      if escolha in comidas:
            print("Hamburguer adicionado")
      else:
            print("Pedido inválido")

# Cadastro

if menuprincipal == "C":
        nome = input('Digite seu nome de usuário: ')
        senha = input('Digite uma senha: ')
        if nome in usuarios:
              print("Usuário já presente, por favor, faça o login ao invés.")
        elif senha in usuarios:
              print("Usuário já presente, por favor, faça o login ao invés.")
        else:
            print("Cadastro feito com sucesso, aproveite sua primeira vez!")
            menu()

# Login

elif menuprincipal == "L":
        nome = input('Digite seu nome de usuário: ')
        senha = input('Digite uma senha: ')
        if nome in usuarios:
            print("Login completo, aproveite!")
            menu()
        elif senha in usuarios:
              print("Login completo, aproveite!")
              menu()
        else:
              print("Usuário não encontrado, caso não há uma conta, cadastre-se!")
else:
      print("Opção inválida.")