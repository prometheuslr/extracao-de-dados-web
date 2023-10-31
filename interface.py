import excel
from os import system

def userCLI(n):
    match n:
        case 0:
            system('clear')
            print("Web Scrapping de eventos\nPor João Nunes, João Lucas, Lucas Vinicius\n")  

            # Exibindo os dados na tela
            try:
                excel.mostrarDados()
            except:
                print('Não existe eventos rastreados')
            userOpt = userInput(int(input("\n1 - Vasculhar por novos eventos | 2 - Mostrar todos os eventos | 3 - Escolher evento | 4 - Sair\n>> ")))
        case 1:
            system('clear')
            print("Web Scrapping de eventos\nPor João Nunes, João Lucas, Lucas Vinicius\n")  

            # Exibindo os dados na tela
            try:
                excel.lerPlanilha()
            except:
                print('Não existe eventos rastreados')
            userOpt = userInput(int(input("\n1 - Vasculhar por novos eventos | 2 - Mostrar todos os eventos | 3 - Escolher evento | 4 - Sair\n>> ")))
        case 2:
            system('clear')
            print("Web Scrapping de eventos\nPor João Nunes, João Lucas, Lucas Vinicius\n")  

            # Exibindo os dados na tela
            try:
                excel.mostrarTodosDados()
            except:
                print('Não existe eventos rastreados')
            userOpt = userInput(int(input("\n1 - Vasculhar por novos eventos | 2 - Mostrar todos os eventos | 3 - Escolher evento | 4 - Sair\n>> ")))
        case 3:
            userOpt = userInput(int(input("\nDigite o ID do evento\n>> ")))

def userInput(userOpt):
    match userOpt:
        case 1:
            # Chama função para vasculhar e atualizar banco de dados
            userCLI(1)
        case 2:
            # Mostra todos os dados do banco de dados
            userCLI(2)
        case 3:
            # Mostra todos os dados do banco de dados
            userCLI(3)
        case 3:
            exit()
        