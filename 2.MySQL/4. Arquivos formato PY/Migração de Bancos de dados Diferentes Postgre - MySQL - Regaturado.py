# %%
from sqlalchemy import create_engine,VARCHAR,NUMERIC,INTEGER,DATE,DATETIME,String
import pandas as pd

#Conexoes

eng_postgre = create_engine('postgresql://postgres:*******@localhost:5432/python')
eng_mysql = create_engine("mysql+pymysql://root:12345@localhost/python")
query = """

select
id
,dt_ocorrencia
,uf
,regiao
,classificacao_da_ocorrencia
from public.anac_mapeamento

"""
df=pd.read_sql_query(query,eng_postgre) #transforma query em df

tabela_destino='anac_origem_postgre'

tipo_coluna={
  'id':INTEGER,
  'dt_ocorrencia':DATE,
  'uf':VARCHAR(30),
  'regiao':VARCHAR(15),
  'classificacao_da_ocorrencia': VARCHAR(30)

  }#inferir tipos de dados no banco destino

df.to_sql(name=tabela_destino, con=eng_mysql, if_exists='replace',dtype=tipo_coluna, index=False)


