print('Seja bem-vindo ao FEIFOOD!')
escolha = input('Se for um novo usuário, digite C para se cadastrar. Caso já tenha logado, digite L para se logar: ')

usuarios = {
      "Tania", 123,
      "Lucas", 321
}

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
        senha = input('Digite uma senha: ')
        if nome in usuarios:
              print("Usuário já presente, por favor, faça o login ao invés.")
        elif senha in usuarios:
              print("Usuário já presente, por favor, faça o login ao invés.")
        else:
            print("Cadastro feito com sucesso, aproveite sua primeira vez!")
            menu()
              
elif escolha == "L":
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