import schedule
import time 
import pandas as pd
import pyodbc 

def job():
  server = 'DESKTOP-33OODCP' 
  database = 'Python' 
  conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        f'SERVER={server};'
                        f'DATABASE={database};'
                        'Trusted_Connection=yes;')

  cursor = conexaoDB.cursor()   # criando cursor de comando 

  dados = pd.read_excel(r'C:\curso-eng-dados\Python-SGBDS\Origem de Dados\arquivos_excel\Categoria.xlsx')
  str(dados.columns).replace("'","")

  cursor.execute('truncate table [Categoria]') #executa tarefa de apgar dados
  cursor.commit()

  for index, linha in dados.iterrows():
      
      cursor.execute("Insert into [Categoria](ID,Categoria)values(?,?)",linha.id,linha.name) 
  cursor.commit()  
  cursor.close()    
  conexaoDB.close() 

schedule.every(10).seconds.do(job)
while True: #loop continuo
  schedule.run_pending() # Executa tarefas agendadas que estão prontas para serem executadas
  time.sleep(1)          # Pausa por 1 segndo antes de verificar novamente as taregfas agendadas



