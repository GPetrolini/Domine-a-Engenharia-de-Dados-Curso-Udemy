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
dados = pd.read_csv(r'C:\curso-eng-dados\Python-SGBDS\Origem de Dados\arquivos_csv\Clientes.csv',delimiter = ',')
dados.head()

# %%
# Converter colunas 
dados['created_at'] = pd.to_datetime(dados['created_at'])
dados['email'] = dados['email'].fillna('Sem registro')
dados['street'] = dados['street'].fillna('Sem info')
dados['number'] = dados['number'].fillna('Sem número')
dados['additionals'] = dados['additionals'].fillna('Sem registro')

# %%
for coluna in dados.columns:
  print(f"coluna: {coluna},Tipos de dados: {dados[coluna].dtypes} ")

# %%
str(dados.columns).replace("'","")

# %%
cursor.execute('truncate table [Clientes]') #executa tarefa de apgar dados
cursor.commit()

# %%
for index, linha in dados.iterrows():
  linha.email = str(linha.email) # converte para o tipo string antes da inserção
  linha.country = str(linha.country)
  linha.state = str(linha.state)
  linha.street = str(linha.street)
  linha.number = str(linha.number)
  linha.additionals = str(linha.additionals)

  cursor.execute("INSERT INTO [Clientes] (id,created_at,first_name,last_name,email,cell_phone,country,state,street,number,additionals) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
  ,linha.id,linha.created_at,linha.first_name,linha.last_name,linha.email,linha.cell_phone,linha.country,linha.state,linha.street,linha.number,linha.additionals)

cursor.commit()
cursor.close()
conexaoDB.close()

# %%



