import pandas as pd
import sqlite3

def lerPlanilha():
    # Criando uma conexão com o banco de dados SQLite
    conn = sqlite3.connect('eventos.db')
    
    # Carregando os dados da planilha Excel
    excel_file = 'eventos.xlsx'
    df = pd.read_excel(excel_file)

    # Salvar os dados do DataFrame para o banco de dados
    df.to_sql('eventos', conn, if_exists='replace', index=False)

    # Fechando a conexão com o banco de dados
    conn.close()

def mostrarDados():
    # Criando uma conexão com o banco de dados SQLite
    conn = sqlite3.connect('eventos.db')

    # Criando um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Executando uma consulta SQL para recuperar os dados da tabela 'eventos'
    cursor.execute("SELECT * FROM eventos")

    result = cursor.fetchall()

    print("Nome, Data e Valor")
    for row in result:
        print(row)

    conn.close()