print('Seja bem-vindo ao FEIFOOD!')
escolha = input('Se for um novo usuário, digite C para se cadastrar. Caso já tenha logado, digite L para se logar: ')

usuarios = {}

def menu():
      print("Selecione a comida que deseja:")
      comidas = {
            "Hamburguer": "R$30,00",
            "Hot Dog": "R$25,00",
            "Coxinha": "R$20,00"
      }
      print(comidas)

if escolha == "C":
        nome = input('Digite seu nome de usuário: ')
        if nome in usuarios:
            print("Usuário já cadastrado, tente novamente")
        else:
            senha = input('Digite uma senha: ')
            usuarios[nome] = senha
            print("Usuário cadastro com sucesso!")
            menu()
elif escolha == "L":
        nome = input('Digite seu nome de usuário: ')
        senha = input('Digite uma senha: ')
        if nome in usuarios and usuarios[nome] == senha:
            print("Login cadastrado com sucesso!")
            menu()

