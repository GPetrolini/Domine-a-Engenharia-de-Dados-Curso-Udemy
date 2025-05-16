# 4. ETL com Pandas

Este diretório faz parte do curso 'Domine a Engenharia de Dados' e contém estudos e exemplos práticos de processos ETL utilizando a biblioteca **Pandas** no Python.

## Estrutura dos Arquivos

* `extract.py`: Script para extração de dados de diferentes fontes.
* `transform.py`: Script para transformação de dados utilizando Pandas.
* `load.py`: Script para carregamento dos dados em um destino especificado.
* `data/`: Pasta contendo arquivos de dados utilizados nos exemplos.

## Requisitos e Dependências

* Python 3.10+
* Pandas
* Jupyter Notebook (opcional, para testes interativos)

Instale as dependências utilizando:

```bash
pip install -r requirements.txt
```

## Executando os Scripts

1. Extraia os dados:

```bash
python extract.py
```

2. Transforme os dados:

```bash
python transform.py
```

3. Carregue os dados:

```bash
python load.py
```

## Exemplo Básico

* O script `transform.py` aplica transformações comuns, como:

  * Conversão de tipos de dados
  * Remoção de valores nulos
  * Agrupamentos e agregações

Execute-o para visualizar o processo de transformação:

```bash
python transform.py
```

## Notas

* Verifique a pasta `data/` para visualizar os conjuntos de dados utilizados nos exemplos.
* Modifique os scripts para testar diferentes operações de ETL.

Para mais informações, consulte a [documentação oficial do Pandas](https://pandas.pydata.org/).
