usuarios = {
      "Tania", 123,
      "Lucas", 321
}

# Dicionario pros pedido dos cara, mesma coisa que o cara ali em cima disse

pedidos = []

def inicio ():
      print('\nSeja bem-vindo ao FEIFOOD!\n')
      menuprincipal = input('Se for um novo usuário, digite C para se cadastrar. Caso já tenha logado, digite L para logar:\n')
      # Cadastro

      if menuprincipal == "C":
            nome = input('\nDigite seu nome de usuário: ')
            senha = input('\nDigite uma senha: ')
            if nome and senha in usuarios:
                  print("\nUsuário já presente, por favor, faça o login ao invés.")
                  inicio()
            else:
                  print("\nCadastro feito com sucesso, aproveite sua primeira vez!")
                  menu()

      # Login

      elif menuprincipal == "L":
            nome = input('\nDigite seu nome de usuário: ')
            senha = input('\nDigite uma senha: ')
            if nome and senha in usuarios:
                  print("\nLogin completo, aproveite!\n")
                  menu()
            else:
                  print("\nUsuário não encontrado, caso não há uma conta, cadastre-se!")
                  inicio()
      else:
            print("\nOpção inválida.")
            inicio()

      # Menu de yummers

def menu():
      print("\nSelecione a comida que deseja: \n")
      comidas = []

      print(comidas)
      escolha = input('\n')
      if escolha not in comidas:
            print("\nComida adicionada adicionada!")
            pedidos.append(pedidos)
            escolha2 = input("\nDeseja adicionar mais alguma comida? (S/N): \n")
            if escolha2 == "N":
                  avaliar()
            elif escolha2 == "S":
                  menu()
      else:
            print("\nPedido inválido ou já adicionado na lista")

def avaliar():
      print("\n5 estrelas RIGHT NOW!!!!!")

inicio()

# Dicionário para usuários lá, se tiver algo ai é só teste, tira sa merda depois

# Avaliar pedido