import pandas as pd
import sqlite3
from extracao_dados import webScrap

def lerPlanilha():

    webScrap()
    # Criando uma conexão com o banco de dados SQLite
    conn = sqlite3.connect('eventos.db')
    
    # Carregando os dados da planilha Excel
    excel_file = 'dados_site_shows.xlsx'
    excel_ingresso = "dodos_ingresso_show.xlsx"
    df = pd.read_excel(excel_file)
    df_ingresso = pd.read_excel(excel_ingresso)
    # Salvar os dados do DataFrame para o banco de dados
    df.to_sql('eventos', conn, if_exists='replace', index=False)
    df_ingresso.to_sql('ingresso', conn, if_exists='replace', index=False)
    # Fechando a conexão com o banco de dados
    conn.close()

    mostrarDados()

def mostrarDados():
    # Criando uma conexão com o banco de dados SQLite
    conn = sqlite3.connect('eventos.db')

    # Criando um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Executando uma consulta SQL para recuperar os dados da tabela 'eventos'
    cursor.execute("SELECT * FROM eventos LIMIT 10")

    result = cursor.fetchall()

    print("ID | EVENTO")
    for row in result:
        print(f"{row[0]} | Evento: {row[1]}")
    print("\n<<Mais>>")

    conn.close()

def mostrarTodosDados():
    # Criando uma conexão com o banco de dados SQLite
    conn = sqlite3.connect('eventos.db')

    # Criando um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Executando uma consulta SQL para recuperar os dados da tabela 'eventos'
    cursor.execute("SELECT * FROM eventos")

    result = cursor.fetchall()

    print("ID | EVENTO")
    for row in result:
        print(f"{row[0]} | Evento: {row[1]}")


    conn.close()

def mostrarEvento(evento):
    ev = evento
    # Criando uma conexão com o banco de dados SQLite
    conn = sqlite3.connect('eventos.db')

    # Criando um cursor para executar comandos SQL
    cursor = conn.cursor()


    cursor.execute(f"SELECT * FROM eventos WHERE id = {ev}")
    info = cursor.fetchall()
    # Executando uma consulta SQL para recuperar os dados da tabela 'eventos'
    cursor.execute(f"SELECT * FROM ingresso WHERE id = {ev}")

    result = cursor.fetchall()

    print(f"Evento: {info[0][1]} | Local: {info[0][2]} | Data: {info[0][3]}")
    for row in result:
        print(f" Ingresso: {row[1]} | Lote: {row[2]} | Tipo: {row[3]} | Valor: R${row[4]} | Disbolibilidade: {row[5]}")


    conn.close()