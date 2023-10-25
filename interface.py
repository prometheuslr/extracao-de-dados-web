import excel

def userCLI():
    print("Web Scrapping de eventos\nPor João Nunes, João Lucas, Lucas Vinicius\n")

    # Exibindo os dados na tela
    excel.mostrarDados()

    userOpt = int(input("\n1 - Vasculhar por novos eventos | 2 - Sair\n>> "))

    userInput(userOpt)

    
def userInput(userOpt):
    match userOpt:
        case 1:
            # Chama função para vasculhar e atualizar banco de dados
            excel.lerPlanilha()
            userCLI()
        case 2:
            exit()