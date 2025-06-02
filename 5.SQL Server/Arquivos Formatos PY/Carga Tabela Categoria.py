# %%
import pandas as pd
import pyodbc 

server = 'DESKTOP-33OODCP' 
database = 'Python' 
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()   # criando cursor de comando 

# %%
dados = pd.read_excel(r'C:\curso-eng-dados\Python-SGBDS\Origem de Dados\arquivos_excel\Categoria.xlsx')
str(dados.columns).replace("'","")
dados.head()

# %%
cursor.execute('truncate table [Categoria]') #executa tarefa de apgar dados
cursor.commit()

# %%
for index, linha in dados.iterrows():
    
    cursor.execute("Insert into [Categoria](ID,Categoria)values(?,?)",linha.id,linha.name) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server
cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao


