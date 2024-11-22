from funcoes import *

try:
    while True:
        sistema()
        print("="*45)
        print()
        print("\tSeja Bem vindo ao BS Bank")
        print()
        print("  [1]  -  Cadastrar Conta")
        print("  [2]  -  Login em Conta")
        print()
        print("  [0]  -  Sair")
        print()
        print("="*45)
        print()
        try:  
            
            escolha = int(input("Escolha uma opção: "))

            match escolha:

                case 1:
                    cadastro()

                case 2:
                    login()

                case 0:
                    sistema()
                    break

                case _:
                    sistema()
                    print("Erro no Sistema, tente novamente!")  

        except Exception as e:
                os.system("cls")
                print(f"Erro no sistema, tente novamente\n{e}")
                os.system("pause")

except Exception as e:
            os.system("cls")
            print(f"Erro no sistema, tente novamente\n{e}")
            os.system("pause")